#!/usr/bin/env python3
"""Validate this repository's Agent Skills without third-party dependencies."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
OPENAI_FIELD_RE = re.compile(r'^  ([a-z_]+): "(.*)"$')
ALLOWED_FRONTMATTER = {"name", "description"}


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def parse_frontmatter(path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n(.*)\Z", text, re.DOTALL)
    if not match:
        fail(errors, path, "expected YAML frontmatter followed by a Markdown body")
        return {}, ""

    fields: dict[str, str] = {}
    for line_number, line in enumerate(match.group(1).splitlines(), start=2):
        field = re.fullmatch(r"([a-z][a-z0-9-]*):\s*(.+)", line)
        if not field:
            fail(errors, path, f"line {line_number} is not a simple frontmatter field")
            continue
        key, raw_value = field.groups()
        if key in fields:
            fail(errors, path, f"duplicate frontmatter field {key!r}")
            continue
        try:
            value = ast.literal_eval(raw_value) if raw_value.startswith(('"', "'")) else raw_value
        except (SyntaxError, ValueError):
            fail(errors, path, f"could not parse frontmatter field {key!r}")
            continue
        if not isinstance(value, str):
            fail(errors, path, f"frontmatter field {key!r} must be a string")
            continue
        fields[key] = value

    return fields, match.group(2)


def validate_openai_metadata(skill_dir: Path, skill_name: str, errors: list[str]) -> None:
    path = skill_dir / "agents" / "openai.yaml"
    if not path.is_file():
        fail(errors, path, "missing Codex UI metadata")
        return

    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "interface:":
        fail(errors, path, "must start with interface:")
        return

    required = {"display_name", "short_description", "default_prompt"}
    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:], start=2):
        match = OPENAI_FIELD_RE.fullmatch(line)
        if not match:
            fail(errors, path, f"line {line_number} must be a quoted interface field")
            continue
        key, value = match.groups()
        if key not in required:
            fail(errors, path, f"unsupported interface field {key!r}")
            continue
        if key in fields:
            fail(errors, path, f"duplicate interface field {key!r}")
            continue
        fields[key] = value

    missing = required - fields.keys()
    if missing:
        fail(errors, path, f"missing fields: {', '.join(sorted(missing))}")
    if "short_description" in fields and not 25 <= len(fields["short_description"]) <= 64:
        fail(errors, path, "short_description must be 25-64 characters")
    if "default_prompt" in fields and f"${skill_name}" not in fields["default_prompt"]:
        fail(errors, path, f"default_prompt must mention ${skill_name}")


def validate_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        target = target.strip("<>").split("#", 1)[0]
        if not target or re.match(r"^[a-z]+://", target) or target.startswith("mailto:"):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            fail(errors, path, f"broken relative link: {target}")


def main() -> int:
    errors: list[str] = []
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))

    if not skill_files:
        errors.append("skills: no SKILL.md files found")

    for path in skill_files:
        fields, body = parse_frontmatter(path, errors)
        skill_name = path.parent.name

        unknown = fields.keys() - ALLOWED_FRONTMATTER
        missing = ALLOWED_FRONTMATTER - fields.keys()
        if unknown:
            fail(errors, path, f"unsupported frontmatter fields: {', '.join(sorted(unknown))}")
        if missing:
            fail(errors, path, f"missing frontmatter fields: {', '.join(sorted(missing))}")

        name = fields.get("name", "")
        description = fields.get("description", "")
        if not NAME_RE.fullmatch(name) or len(name) > 64:
            fail(errors, path, "name must be 1-64 lowercase letters, numbers, or single hyphens")
        if name != skill_name:
            fail(errors, path, f"name {name!r} must match parent directory {skill_name!r}")
        if not description or len(description) > 1024:
            fail(errors, path, "description must be 1-1024 characters")
        if not body.strip():
            fail(errors, path, "Markdown body is empty")
        if len(body.splitlines()) > 500:
            fail(errors, path, "Markdown body exceeds 500 lines")
        if f"(skills/{skill_name}/SKILL.md)" not in readme:
            fail(errors, ROOT / "README.md", f"missing skill link for {skill_name}")

        validate_openai_metadata(path.parent, skill_name, errors)
        validate_links(path, errors)

    for path in [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "AGENTS.md"]:
        if not path.is_file():
            fail(errors, path, "missing repository documentation")
        else:
            validate_links(path, errors)

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_files)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
