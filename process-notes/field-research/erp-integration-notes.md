---
description: Field notes for ERP data integrations and handoff risks.
icon: database
---

# ERP Integration Notes

## Common implementation patterns

<table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
<tr><td><i class="fa-cloud-arrow-down"></i></td><td><strong>Native connector</strong></td><td>Preferred when available. Operations can rely on recurring sync state.</td><td><a href="../README.md">Process Notes</a></td></tr>
<tr><td><i class="fa-file-csv"></i></td><td><strong>Managed export</strong></td><td>Acceptable fallback with source, period, and expiry date.</td><td><a href="../README.md">Process Notes</a></td></tr>
<tr><td><i class="fa-triangle-exclamation"></i></td><td><strong>Manual entry</strong></td><td>Risky for ongoing compliance. Requires owner and migration path.</td><td><a href="../README.md">Process Notes</a></td></tr>
</tbody></table>

## Open question

Should the agent answer from an ERP sync state if the underlying data freshness is older than the filing-cycle threshold? This should be a governance rule before production use.
