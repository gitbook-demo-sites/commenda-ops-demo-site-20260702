---
description: Proposed metadata fields for SOPs, notes, and agent-readable content.
icon: tags
---

# Knowledge Metadata Schema

```yaml
id: SOP-GEO-001
title: Entity Launch SOP
source_type: approved_sop
owner: global_operations
status: approved
last_reviewed: 2026-07-02
review_cadence: quarterly
agent_safe: true
requires_auth_data: false
escalation_owner: regional_specialist
related_systems:
  - commenda_platform
  - compliance_calendar
  - erp_connector
```

## Why this helps

* Humans can scan ownership and status.
* Agents can prefer current approved content.
* Reviewers can find stale pages before operations drift.
* Sales can demo a credible "versioned database" without leaving GitBook.
