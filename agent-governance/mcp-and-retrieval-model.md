---
description: How GitBook content can be exposed to internal agents through MCP-ready retrieval.
icon: plug-circle-bolt
---

# MCP and Retrieval Model

GitBook can act as the maintained knowledge surface while agents retrieve only the content they are allowed to use.

## Retrieval flow

{% stepper %}
{% step %}
### User asks an operational question

The agent identifies the intent: SOP lookup, status lookup, exception handling, or summarization.
{% endstep %}

{% step %}
### Agent retrieves reviewed content

The agent queries GitBook content first, then authenticated systems only when current status data is needed.
{% endstep %}

{% step %}
### Agent applies source priority

Approved SOPs outrank process notes. Deprecated pages are ignored unless the user asks for history.
{% endstep %}

{% step %}
### Agent answers with traceability

Every answer includes source status, escalation conditions, and confidence.
{% endstep %}
{% endstepper %}

## Example retrieval labels

* `source_type: approved_sop`
* `process_area: global_entity_operations`
* `agent_safe: true`
* `requires_auth_data: false`
* `escalate_if: source_conflict`
