.PHONY: validate

validate:
	python3 scripts/validate.py
	git diff --check
