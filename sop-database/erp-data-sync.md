---
description: Runbook for ERP-connected operating data across NetSuite, Xero, QuickBooks, and manual imports.
icon: plug
---

# ERP Data Sync

Commenda's operating promise depends on clean source data. This SOP gives operators and agents a shared way to describe ERP connection status.

| State | Meaning | Next action |
| --- | --- | --- |
| Connected | Credentials valid and latest sync completed. | Continue monitoring. |
| Needs mapping | Data imports, but account or tax fields need mapping. | Assign implementation owner. |
| Client blocked | Client has not granted access or exported required files. | Trigger client follow-up. |
| Fallback upload | Temporary spreadsheet or CSV process active. | Add expiry date and migration owner. |

## Standard mapping fields

* Entity and subsidiary identifier.
* Country and tax registration fields.
* Transaction date, currency, and amount.
* Tax category and product/service classification.
* Source system record ID.

{% hint style="warning" %}
Agents can summarize ERP sync state, but they should not infer tax treatment from incomplete mappings.
{% endhint %}
