---
description: Contract for how agents should answer operational questions from the knowledge base.
icon: file-signature
---

# Agent Answer Contract

## Allowed answer types

| Request | Agent can answer? | Required source |
| --- | --- | --- |
| "What is the current SOP for entity launch?" | Yes | Approved SOP |
| "Which filing obligations are at risk?" | Yes, with authenticated data | Compliance calendar and approved SOP |
| "Can we accept this out-of-scope tax request?" | No | Escalate to account owner and specialist |
| "Summarize this country note." | Yes, as context | Reviewed or raw note with status label |

## Required response shape

```text
Short answer:
Source status:
Relevant SOP or note:
Evidence required:
Escalation conditions:
Confidence:
```

## Stop conditions

* The source page is deprecated.
* The answer requires legal or tax interpretation not present in an approved page.
* Customer-specific data is missing, stale, or unauthorized.
* Two reviewed sources conflict.
