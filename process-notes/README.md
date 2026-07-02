---
description: A workspace for evolving notes that should remain searchable without pretending to be final SOPs.
icon: clipboard-list
---

# Process Notes

Not every useful piece of knowledge should become an SOP immediately. Process notes are where operators capture reality before the process is stable.

{% hint style="warning" %}
Agent rule: process notes can provide context, but agents should prefer approved SOPs when instructions conflict.
{% endhint %}

## Note lifecycle

| Stage | Meaning | Agent behavior |
| --- | --- | --- |
| Raw note | Captured from an implementation or support event. | Context only. |
| Reviewed note | Validated by a subject-matter owner. | Can be cited with status. |
| SOP candidate | Pattern appears repeatable. | Suggest related SOP, do not execute. |
| Promoted | Moved into SOP Database. | Use SOP as source of truth. |
