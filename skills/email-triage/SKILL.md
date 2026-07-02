---
name: email-triage
description: "Triage an email inbox into a small action queue. Use when the user asks to process, clean up, rank, label, archive, or draft replies for email."
user-invocable: true
argument-hint: "<mailbox scope, label policy, or triage goal>"
---

# Email Triage

Turn an inbox into a short ranked queue.
The inbox is not storage.
Every processed thread gets one visible outcome:

- archive it
- draft a reply
- put it in needs attention

Optional mechanics such as tasks, snooze, and follow-up tracking must remove the email from Inbox.
Do not create extra daily folders for those mechanics.

## Safety

Never do these without explicit approval:

- send email
- delete email
- unsubscribe
- report spam
- block a sender
- agree to a call, price, deadline, refund, sponsorship, partnership, contract, public commitment, or money commitment

Drafting is allowed.
Mark commitment-bearing drafts as needing careful review.

## Labels

Use the smallest useful label set.
Default labels:

- `Action/Needs Attention`: the user must decide or do something.
- `Action/Draft Replies`: a draft exists and the user must review, send, edit, or ignore it.

Optional label:

- `Action/Sponsorships`: sponsorship, brand deal, paid collaboration, creator campaign, or product-review outreach that should leave Inbox but remain easy to review.

Do not use `Handled`.
Handled mail is archived.
Gmail search is the archive.

Do not create category labels for newsletters, receipts, notifications, promotions, read-later, finance, customer, or product ops unless the user explicitly asks.
Classify those in the report instead.

## Workflow

1. Read mailbox constraints, existing labels, user rules, and any local SOP before acting.
2. Record the starting Inbox count when the tool exposes it.
3. Search recent Inbox first.
4. Search older Inbox only when the user asks for backlog cleanup or a weekly pass.
5. Process each selected thread once.
6. Choose exactly one outcome per thread:
   - archive: no user action needed
   - draft: create or propose a reply, label `Action/Draft Replies`, keep in Inbox
   - needs attention: label `Action/Needs Attention`, keep in Inbox
   - optional sponsorship bucket: label `Action/Sponsorships`, archive
7. Archive obvious newsletters, promotions, notifications, receipts, cold outreach, FYI, and old low-risk messages.
8. Draft replies when the correct response is inferable.
9. Ask only when acting would require a commitment, private context, or a risky judgment.
10. Record the ending Inbox count when available.

## Decision Rules

Use `Action/Needs Attention` only when the user must personally act, decide, approve, pay, schedule, review, or provide private context.

Use `Action/Draft Replies` when the next action is only reviewing a prepared reply.

Use `Action/Sponsorships` when sponsorship-style mail should leave Inbox but stay grouped for optional review.

Archive when:

- no reply is needed
- a sent reply means the next move belongs to someone else
- a task was created elsewhere
- a dated item was snoozed or scheduled elsewhere
- the message is old and not clearly active
- the message is generic marketing, a newsletter, FYI, a receipt, a notification, or low-value cold outreach

Uncertainty is not a permanent outcome.
If unsure, propose the smallest safe resolution: archive, draft, task, or needs attention.

## Aging

When previous-run memory is available:

- Escalate messages still in `Action/Needs Attention` after 3 runs.
- For each stale item, propose one resolution: archive, draft reply, task, or keep with reason.
- Do not let flagged mail rot without a recommendation.

## Sender Memory

When automation memory is available, track sender patterns:

- repeatedly archived newsletters
- repeated cold outreach
- trusted senders
- sponsorship or sales agencies
- senders that usually need the user

Use this memory to propose future filters or batch archive rules.
Do not create filters, unsubscribe, block, or report spam without approval.

## Report

Lead with the work queue, not an audit log.

Report shape:

```md
Email triage complete.

Needs you today: <N>

1. <Sender> - <subject>
   Recommended action: <reply/decide/pay/schedule/review/archive/task>
   Why: <one short reason>

Drafts ready: <N>
- <Sender> - <subject>: <what the draft says>

Archived: <N>
Sponsorships bucketed: <N>
Inbox: <start> -> <end>

Blocked or uncertain:
- <only real blockers>
```

Keep the report short.
Mention labels created or changed only when useful.
