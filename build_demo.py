from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent
REPO = "commenda-ops-demo-site-20260702"
RAW = f"https://raw.githubusercontent.com/gitbook-demo-sites/{REPO}/main"


def write(path: str, content: str) -> None:
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(dedent(content).strip() + "\n", encoding="utf-8")


def yaml(space: str) -> None:
    write(
        f"{space}/.gitbook.yaml",
        """
        root: ./
        structure:
          readme: README.md
          summary: SUMMARY.md
        """,
    )


def vars_file(space: str) -> None:
    write(
        f"{space}/.gitbook/vars.yaml",
        """
        product_name: Commenda
        demo_name: Commenda Operations Knowledge Base
        review_stage: First-draft demo
        primary_audience: Operations, compliance, finance, and service teams
        """,
    )


def summary(space: str, lines: list[str]) -> None:
    write(f"{space}/SUMMARY.md", "# Table of contents\n\n" + "\n".join(lines))


def card(icon: str, title: str, desc: str, href: str) -> str:
    return (
        f'<tr><td><i class="fa-{icon}"></i></td><td><strong>{title}</strong></td>'
        f'<td>{desc}</td><td><a href="{href}">{title}</a></td></tr>'
    )


for slug in ["home", "sop-database", "process-notes", "agent-governance"]:
    yaml(slug)
    vars_file(slug)

write(
    "README.md",
    """
    # Commenda operations demo site

    First-draft GitBook demo content for Commenda. Each top-level folder is a GitBook space for import into a multi-section demo site.
    """,
)

write(".gitignore", ".DS_Store\nThumbs.db\n*.swp\n*.swo\n.idea/\n.vscode/\n")

write(
    "assets/commenda-ops-cover.svg",
    """
    <svg xmlns="http://www.w3.org/2000/svg" width="1600" height="520" viewBox="0 0 1600 520" role="img" aria-label="Commenda Operations Knowledge Base">
      <rect width="1600" height="520" fill="#F7F4EF"/>
      <rect width="1600" height="18" fill="#111827"/>
      <circle cx="1230" cy="168" r="218" fill="#16A34A" opacity=".13"/>
      <circle cx="1350" cy="314" r="185" fill="#2563EB" opacity=".10"/>
      <rect x="1054" y="118" width="298" height="72" rx="10" fill="#FFFFFF" stroke="#D6D3CC"/>
      <rect x="1084" y="148" width="64" height="12" rx="6" fill="#111827"/>
      <rect x="1165" y="148" width="144" height="12" rx="6" fill="#16A34A"/>
      <rect x="1054" y="214" width="360" height="72" rx="10" fill="#FFFFFF" stroke="#D6D3CC"/>
      <rect x="1084" y="244" width="80" height="12" rx="6" fill="#111827"/>
      <rect x="1184" y="244" width="190" height="12" rx="6" fill="#2563EB"/>
      <rect x="1054" y="310" width="254" height="72" rx="10" fill="#FFFFFF" stroke="#D6D3CC"/>
      <rect x="1084" y="340" width="72" height="12" rx="6" fill="#111827"/>
      <rect x="1174" y="340" width="88" height="12" rx="6" fill="#16A34A"/>
      <text x="96" y="185" font-family="Arial, Helvetica, sans-serif" font-size="86" font-weight="700" fill="#111827" letter-spacing="0">Commenda</text>
      <text x="100" y="251" font-family="Arial, Helvetica, sans-serif" font-size="31" fill="#3D3D3D">Versioned SOPs, process notes, and agent-ready operating knowledge</text>
      <rect x="100" y="323" width="264" height="44" rx="4" fill="#16A34A"/>
      <text x="124" y="352" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#FFFFFF">Operations knowledge base</text>
    </svg>
    """,
)

write(
    "assets/commenda-wordmark.svg",
    """
    <svg xmlns="http://www.w3.org/2000/svg" width="460" height="120" viewBox="0 0 460 120" role="img" aria-label="Commenda">
      <rect width="460" height="120" fill="#F7F4EF"/>
      <circle cx="58" cy="60" r="31" fill="#16A34A"/>
      <path d="M45 59c10-18 28-18 39 0" fill="none" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round"/>
      <text x="108" y="72" font-family="Arial, Helvetica, sans-serif" font-size="40" font-weight="700" fill="#111827">Commenda</text>
    </svg>
    """,
)

write(
    "home/README.md",
    f"""
    ---
    description: A searchable, governed operating layer for Commenda SOPs, process notes, and AI agent answers.
    icon: house
    cover: "{RAW}/assets/commenda-ops-cover.svg"
    coverY: 0
    layout:
      width: wide
      cover:
        visible: true
        size: hero
      title:
        visible: true
      description:
        visible: true
      tableOfContents:
        visible: false
      outline:
        visible: false
      pagination:
        visible: true
    ---

    # Commenda Operations Knowledge Base

    A versioned database for the workflows behind global entity management, indirect tax, transfer pricing, ERP integrations, and filing operations.

    Commenda's public story is about turning inherited international expansion complexity into clean infrastructure. This demo shows the internal knowledge layer that makes that promise operational: every SOP has an owner, every process note has a source, every change has a version trail, and every answer is safe for humans and agents to reuse.

    {{% hint style="info" %}}
    Demo assumption: this is a purpose-built first draft based on Commenda's public positioning and Louis's note that the team is extremely ops heavy. It is not a migration of Commenda's private internal content.
    {{% endhint %}}

    ## Start from the job

    <table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
    {card("list-check", "Run the SOP database", "Standardized operating procedures for entity launch, filings, ERP sync, and client delivery.", "https://app.gitbook.com/s/XSPACE_SOPS/")}
    {card("clipboard-list", "Use process notes", "Living notes for country playbooks, exceptions, service handoffs, and internal decisions.", "https://app.gitbook.com/s/XSPACE_NOTES/")}
    {card("robot", "Prepare agent answers", "Metadata, answer rules, review workflow, and MCP-ready knowledge contracts.", "https://app.gitbook.com/s/XSPACE_AGENT/")}
    {card("route", "Review the demo map", "How this draft maps Commenda's public operating model into a GitBook site.", "demo-map.md")}
    </tbody></table>

    ## Why this matters for Commenda

    {{% columns %}}
    {{% column %}}
    **The operating problem**

    Global compliance delivery depends on repeatability. If entity records, filing steps, local exceptions, ERP dependencies, and transfer-pricing evidence live across spreadsheets, Slack, docs, and personal notes, the burden moves back onto operators.
    {{% endcolumn %}}
    {{% column %}}
    **The GitBook story**

    GitBook turns SOPs and process notes into a maintained knowledge system: reviewed pages, Git-backed history, changelogs, AI Assistant, page feedback, markdown export, and MCP access for agents.
    {{% endcolumn %}}
    {{% endcolumns %}}

    ## Demo moments

    * Search for a client onboarding task and land on the current SOP, not an old process note.
    * Ask the assistant "what changes when a filing deadline is missed?" and get a grounded answer from reviewed pages.
    * Show how a process note graduates into a controlled SOP with an owner, evidence requirements, and change history.
    * Show how agents can retrieve compact, permission-aware operating instructions rather than scraping loose documents.
    """,
)

summary(
    "home",
    [
        "* [Home](README.md)",
        "* [Demo map](demo-map.md)",
        "* [Operating model](operating-model.md)",
        "* [Review checklist](review-checklist.md)",
    ],
)

write(
    "home/demo-map.md",
    """
    ---
    description: Map Commenda's public operating themes into this first-draft GitBook demo.
    icon: route
    ---

    # Demo Map

    Commenda's public site emphasizes certainty of process, certainty of compliance, and certainty of service. This demo turns those promises into an internal documentation model.

    <table data-view="cards"><thead><tr><th width="48"></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody>
    <tr><td><i class="fa-diagram-project"></i></td><td><strong>Standardized workflow</strong></td><td>Every subsidiary launch and compliance engagement follows a repeatable path.</td><td><a href="https://app.gitbook.com/s/XSPACE_SOPS/entity-launch-sop.md">Entity launch SOP</a></td></tr>
    <tr><td><i class="fa-calendar-check"></i></td><td><strong>Tracked obligations</strong></td><td>Filing deadlines, owners, confirmations, and exception paths are visible.</td><td><a href="https://app.gitbook.com/s/XSPACE_SOPS/compliance-calendar-triage.md">Compliance calendar triage</a></td></tr>
    <tr><td><i class="fa-plug"></i></td><td><strong>ERP-connected operations</strong></td><td>NetSuite, Xero, QuickBooks, and data-quality handoffs become documented runbooks.</td><td><a href="https://app.gitbook.com/s/XSPACE_SOPS/erp-data-sync.md">ERP data sync</a></td></tr>
    <tr><td><i class="fa-robot"></i></td><td><strong>Agent-ready knowledge</strong></td><td>Pages carry status, source, owner, and escalation rules so AI agents answer within guardrails.</td><td><a href="https://app.gitbook.com/s/XSPACE_AGENT/agent-answer-contract.md">Agent answer contract</a></td></tr>
    </tbody></table>

    ## Spaces

    * **Home**: executive framing, demo map, and review checklist.
    * **SOP Database**: controlled operating procedures with owners and versioning.
    * **Process Notes**: evolving notes that capture local context before they become SOPs.
    * **Agent Governance**: how AI Assistant and external agents consume knowledge safely.
    """,
)

write(
    "home/operating-model.md",
    """
    ---
    description: The operating model behind a versioned SOP and process-note database.
    icon: network-wired
    ---

    # Operating Model

    A strong Commenda knowledge base separates controlled procedures from exploratory notes while keeping both searchable.

    {% stepper %}
    {% step %}
    ### Capture the raw process

    Operators document what happened in a process note: jurisdiction nuance, client-specific constraints, manual checks, and open questions.
    {% endstep %}

    {% step %}
    ### Promote repeatable work into SOPs

    Once a pattern repeats, it moves into the SOP Database with an owner, review date, evidence requirements, and escalation path.
    {% endstep %}

    {% step %}
    ### Version every meaningful change

    Changes are reviewed through GitBook change requests or Git Sync. The changelog explains what changed, who approved it, and which agent answers are affected.
    {% endstep %}

    {% step %}
    ### Let agents retrieve, not improvise

    AI Assistant and MCP-connected agents cite reviewed pages, respect status labels, and escalate when a process note is not yet approved.
    {% endstep %}
    {% endstepper %}
    """,
)

write(
    "home/review-checklist.md",
    """
    ---
    description: Review checklist for the first demo pass.
    icon: clipboard-check
    ---

    # Review Checklist

    Use this page as the walkthrough script for the first internal review.

    | Area | What to check | Strong signal |
    | --- | --- | --- |
    | Information architecture | Do the spaces match how Commenda operators think? | Louis can demo the site without explaining the nav first. |
    | SOP structure | Are owner, status, evidence, and escalation fields prominent enough? | A new operator can tell what is safe to execute. |
    | Process notes | Does the draft show how notes can mature into controlled SOPs? | The distinction between notes and SOPs feels clear. |
    | Agent readiness | Do AI/MCP pages explain how agents should use this content? | The demo supports both human search and agent retrieval. |
    | Branding | Does it feel close enough to Commenda for sales review? | The site feels tailored without pretending to be production content. |
    """,
)

summary(
    "sop-database",
    [
        "* [SOP Database](README.md)",
        "",
        "## Global operations",
        "* [Entity launch SOP](entity-launch-sop.md)",
        "* [Compliance calendar triage](compliance-calendar-triage.md)",
        "* [ERP data sync](erp-data-sync.md)",
        "",
        "## Tax and reporting",
        "* [Indirect tax filing cycle](tax-and-reporting/indirect-tax-filing-cycle.md)",
        "* [Transfer pricing evidence pack](tax-and-reporting/transfer-pricing-evidence-pack.md)",
        "",
        "## Service delivery",
        "* [Client handoff and scope control](service-delivery/client-handoff-and-scope-control.md)",
        "* [Exception escalation path](service-delivery/exception-escalation-path.md)",
    ],
)

write(
    "sop-database/README.md",
    """
    ---
    description: Controlled SOPs for repeatable Commenda operations.
    icon: list-check
    ---

    # SOP Database

    This space models GitBook as a versioned database for operational procedures. Each SOP has metadata that makes it useful to humans and agents.

    | Field | Purpose |
    | --- | --- |
    | Owner | Accountable team or role. |
    | Status | Draft, approved, under review, deprecated, or country-specific. |
    | Review cadence | How often the SOP must be revalidated. |
    | Evidence | Required proof that the process was completed. |
    | Escalation | When an operator or agent must stop and ask for human review. |

    {% hint style="success" %}
    Demo angle: the "database" is not a separate tool. It is structured GitBook content with search, history, review workflow, page feedback, markdown export, and AI retrieval.
    {% endhint %}
    """,
)

write(
    "sop-database/entity-launch-sop.md",
    """
    ---
    description: Standard workflow for launching a new global entity engagement.
    icon: diagram-project
    ---

    # Entity Launch SOP

    | Metadata | Value |
    | --- | --- |
    | Owner | Global Operations |
    | Status | Approved demo SOP |
    | Review cadence | Quarterly |
    | Primary systems | Commenda platform, CRM, compliance calendar, ERP connector |
    | Agent-safe? | Yes, when client-specific fields are supplied by an authorized system |

    ## Objective

    Move a new entity from intake to operational readiness with a complete record, assigned owners, known obligations, and connected finance data.

    {% stepper %}
    {% step %}
    ### Confirm scope and jurisdiction

    Validate the entity type, country, expected activity, filing obligations, tax registration needs, and service package.
    {% endstep %}

    {% step %}
    ### Create the operating record

    Create the entity profile, attach onboarding evidence, and link the customer account, subsidiary, and billing owner.
    {% endstep %}

    {% step %}
    ### Assign obligations

    Add statutory deadlines, tax registrations, indirect tax checks, transfer-pricing requirements, and recurring reporting tasks.
    {% endstep %}

    {% step %}
    ### Connect source systems

    Confirm whether NetSuite, Xero, QuickBooks, or a manual upload flow will supply transaction and reporting data.
    {% endstep %}

    {% step %}
    ### Publish readiness summary

    Send a client-facing summary only after the internal record includes scope, owners, dates, and open risks.
    {% endstep %}
    {% endstepper %}

    ## Escalate when

    * The jurisdiction has an unconfirmed filing path.
    * ERP access is blocked beyond the first implementation week.
    * The client requests a service outside the signed scope.
    * Any legal or tax interpretation is missing documented specialist review.
    """,
)

write(
    "sop-database/compliance-calendar-triage.md",
    """
    ---
    description: Triage flow for filing deadlines, upcoming obligations, and missed-deadline risk.
    icon: calendar-check
    ---

    # Compliance Calendar Triage

    | Metadata | Value |
    | --- | --- |
    | Owner | Compliance Operations |
    | Status | Approved demo SOP |
    | Review cadence | Monthly |
    | Agent-safe? | Read-only unless connected to authenticated calendar data |

    ## Daily triage

    1. Filter obligations due in the next 14 days.
    2. Confirm owner and current state: not started, waiting on client, ready to file, filed, confirmed.
    3. Attach source evidence for any status change.
    4. Escalate obligations at risk of missing deadline.

    {% tabs %}
    {% tab title="On track" %}
    Keep the obligation in the normal queue. The operator confirms status when filing evidence is attached.
    {% endtab %}

    {% tab title="Blocked by client" %}
    Add the missing data request, date of request, next follow-up date, and whether client leadership has been notified.
    {% endtab %}

    {% tab title="Deadline risk" %}
    Open an escalation note with jurisdiction, deadline, owner, reason for risk, and recommended mitigation.
    {% endtab %}
    {% endtabs %}

    ## Evidence checklist

    * Filing period and jurisdiction.
    * Responsible owner.
    * Source data version.
    * Filing confirmation or exception reason.
    * Client communication record when applicable.
    """,
)

write(
    "sop-database/erp-data-sync.md",
    """
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
    """,
)

write(
    "sop-database/tax-and-reporting/indirect-tax-filing-cycle.md",
    """
    ---
    description: Operating checklist for VAT, GST, and sales tax filing cycles.
    icon: receipt
    ---

    # Indirect Tax Filing Cycle

    ## Cycle stages

    {% stepper %}
    {% step %}
    ### Validate exposure

    Confirm active jurisdictions, thresholds, registrations, and filing frequency.
    {% endstep %}

    {% step %}
    ### Collect transaction data

    Pull ERP data, review missing mappings, and confirm any manual adjustments.
    {% endstep %}

    {% step %}
    ### Prepare filing package

    Generate the draft return, attach evidence, and flag unusual movement against prior periods.
    {% endstep %}

    {% step %}
    ### File and confirm

    File through the correct channel, attach confirmation, and mark the obligation complete.
    {% endstep %}
    {% endstepper %}

    ## Agent answer rules

    * Safe: answer "what is the current filing status?" from the calendar and filing evidence.
    * Unsafe: answer "what tax treatment applies?" unless a reviewed jurisdiction page says so.
    * Escalate: any missing source data, registration uncertainty, or late filing risk.
    """,
)

write(
    "sop-database/tax-and-reporting/transfer-pricing-evidence-pack.md",
    """
    ---
    description: Evidence requirements for transfer-pricing documentation workflows.
    icon: folder-open
    ---

    # Transfer Pricing Evidence Pack

    Transfer-pricing work needs a durable evidence trail. This demo page shows how GitBook can turn that trail into a repeatable checklist.

    | Evidence type | Required content |
    | --- | --- |
    | Entity profile | Legal name, country, ownership, functional role. |
    | Intercompany transaction | Counterparty, transaction type, period, value, method. |
    | Source data | ERP export or approved data extract reference. |
    | Review note | Specialist review, date, and scope limitations. |
    | Client confirmation | Approval, questions, or unresolved data request. |

    {% hint style="info" %}
    Process notes can hold country nuance while this SOP holds the standard evidence pack. That keeps global consistency without flattening local complexity.
    {% endhint %}
    """,
)

write(
    "sop-database/service-delivery/client-handoff-and-scope-control.md",
    """
    ---
    description: Standard handoff from sales or onboarding into service delivery.
    icon: handshake
    ---

    # Client Handoff and Scope Control

    ## Required handoff fields

    * Customer account and legal entities.
    * Signed scope and excluded services.
    * Countries covered.
    * ERP and data-source expectations.
    * Known risks and specialist dependencies.
    * Communication owner and escalation path.

    ## Scope drift checks

    Before accepting new work, confirm whether it is included in the signed scope. Examples that need review:

    * New jurisdiction added after launch.
    * New filing type not included in the service package.
    * Advisory request that changes from operational delivery to tax interpretation.
    * Urgent manual filing caused by missing source data.
    """,
)

write(
    "sop-database/service-delivery/exception-escalation-path.md",
    """
    ---
    description: Escalation path for operational exceptions, compliance risk, and unclear ownership.
    icon: triangle-exclamation
    ---

    # Exception Escalation Path

    | Exception | First owner | Escalate to |
    | --- | --- | --- |
    | Deadline risk | Compliance Operations | Regional specialist and client owner |
    | Missing ERP access | Implementation owner | Client executive sponsor |
    | Out-of-scope request | Service owner | Account owner and legal/tax reviewer |
    | Unclear local rule | Regional specialist | Tax lead |
    | Agent confidence gap | Knowledge owner | Human reviewer |

    ## Required escalation note

    ```text
    Client:
    Entity:
    Jurisdiction:
    Obligation or process:
    Current blocker:
    Deadline:
    Evidence attached:
    Recommended next step:
    Human owner:
    ```
    """,
)

summary(
    "process-notes",
    [
        "* [Process Notes](README.md)",
        "",
        "## Country and jurisdiction notes",
        "* [Country note template](country-notes/country-note-template.md)",
        "* [Ireland entity readiness note](country-notes/ireland-entity-readiness-note.md)",
        "",
        "## Internal decisions",
        "* [Process note to SOP promotion](internal-decisions/process-note-to-sop-promotion.md)",
        "* [Service exception log](internal-decisions/service-exception-log.md)",
        "",
        "## Field research",
        "* [ERP integration notes](field-research/erp-integration-notes.md)",
        "* [Client operating profile](field-research/client-operating-profile.md)",
    ],
)

write(
    "process-notes/README.md",
    """
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
    """,
)

write(
    "process-notes/country-notes/country-note-template.md",
    """
    ---
    description: Template for jurisdiction-specific process notes.
    icon: globe
    ---

    # Country Note Template

    ```yaml
    country:
    owner:
    status: raw | reviewed | sop-candidate | promoted
    last_reviewed:
    related_sops:
    client_examples:
    agent_safe: context-only
    ```

    ## Operating context

    Summarize why this jurisdiction behaves differently from the global SOP.

    ## Filing and registration nuance

    Capture deadlines, portal behavior, evidence requirements, and local partner dependencies.

    ## Known exceptions

    List cases where the operator should pause instead of following the default SOP.

    ## Promotion criteria

    Explain what must be true before this note becomes an approved SOP page.
    """,
)

write(
    "process-notes/country-notes/ireland-entity-readiness-note.md",
    """
    ---
    description: Example reviewed process note for Ireland entity-readiness work.
    icon: flag
    ---

    # Ireland Entity Readiness Note

    | Metadata | Value |
    | --- | --- |
    | Status | Reviewed demo note |
    | Owner | Regional specialist |
    | Agent-safe? | Context only |
    | Related SOP | Entity launch SOP |

    ## Context

    Ireland is often part of an EMEA expansion path. The operator should confirm whether the entity is intended for sales operations, contracting, hiring, or finance consolidation before applying the generic launch checklist.

    ## Watch points

    * Confirm whether entity setup is part of a larger EMEA operating model.
    * Separate incorporation tasks from ongoing compliance calendar setup.
    * Validate ERP entity mapping before the first filing cycle.
    * Capture any transfer-pricing dependency before marking readiness complete.

    ## Promotion path

    This note should become a country-specific SOP only after Commenda validates the repeatable workflow with enough customer implementations.
    """,
)

write(
    "process-notes/internal-decisions/process-note-to-sop-promotion.md",
    """
    ---
    description: Decision log for turning notes into approved SOPs.
    icon: arrow-up-right-dots
    ---

    # Process Note to SOP Promotion

    A note graduates into the SOP Database when it is repeatable, owned, reviewed, and safe to operationalize.

    ## Promotion checklist

    * The process has occurred at least three times or is strategically important.
    * A named owner accepts responsibility for future updates.
    * Required evidence is clear.
    * Escalation conditions are explicit.
    * Conflicts with existing SOPs have been resolved.
    * Agent behavior is specified.

    ## Change request summary

    ```text
    Source note:
    New SOP page:
    Owner:
    Reviewer:
    What changed:
    Pages or agent prompts affected:
    Rollback plan:
    ```
    """,
)

write(
    "process-notes/internal-decisions/service-exception-log.md",
    """
    ---
    description: Example log for service exceptions that may become operating rules.
    icon: list-ul
    ---

    # Service Exception Log

    | Date | Exception | Interim handling | Candidate SOP update |
    | --- | --- | --- | --- |
    | 2026-07-02 | Client requested added jurisdiction during first filing cycle. | Account owner confirms scope before operations accepts work. | Add scope drift check to handoff SOP. |
    | 2026-07-02 | ERP mapping incomplete but filing deadline approaching. | Regional specialist approves fallback upload. | Add expiry date to fallback upload state. |
    | 2026-07-02 | Agent found conflicting notes on deadline risk. | Agent escalates to knowledge owner. | Add source priority rule to Agent Answer Contract. |
    """,
)

write(
    "process-notes/field-research/erp-integration-notes.md",
    """
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
    """,
)

write(
    "process-notes/field-research/client-operating-profile.md",
    """
    ---
    description: Template for summarizing a customer's operating setup without exposing private data.
    icon: id-card-clip
    ---

    # Client Operating Profile

    Use this template to summarize the operating context that affects SOP choice.

    | Field | Example value |
    | --- | --- |
    | Expansion stage | Entering first EMEA market |
    | ERP system | NetSuite |
    | Filing model | VAT registration and recurring filing |
    | Advisory dependency | Transfer pricing review required |
    | Service risk | Missing source-system access |

    ## Agent redaction rule

    Agents can use the profile to route a user to the right SOP, but should not expose customer-specific identifiers unless the request is authenticated and authorized.
    """,
)

summary(
    "agent-governance",
    [
        "* [Agent Governance](README.md)",
        "",
        "## Agent-ready knowledge",
        "* [Agent answer contract](agent-answer-contract.md)",
        "* [MCP and retrieval model](mcp-and-retrieval-model.md)",
        "* [Knowledge metadata schema](knowledge-metadata-schema.md)",
        "",
        "## Review and change history",
        "* [Review workflow](review-workflow.md)",
        "* [Changelog](changelog.md)",
    ],
)

write(
    "agent-governance/README.md",
    """
    ---
    description: Guardrails for AI Assistant, external agents, and operational knowledge retrieval.
    icon: robot
    ---

    # Agent Governance

    Commenda's public positioning mentions clear legal guardrails for AI agents. This space shows how GitBook can support that: human-readable SOPs, metadata, answer policy, and MCP-ready access patterns in one place.

    ## Source priority

    1. Approved SOPs.
    2. Reviewed process notes.
    3. Raw notes, only for context.
    4. External systems, only through authenticated connectors.

    {% hint style="danger" %}
    Agents must not convert a raw note into an operational instruction. If approved SOPs and notes conflict, agents cite the conflict and escalate.
    {% endhint %}
    """,
)

write(
    "agent-governance/agent-answer-contract.md",
    """
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
    """,
)

write(
    "agent-governance/mcp-and-retrieval-model.md",
    """
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
    """,
)

write(
    "agent-governance/knowledge-metadata-schema.md",
    """
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
    """,
)

write(
    "agent-governance/review-workflow.md",
    """
    ---
    description: Review workflow for safe operational and agent-ready changes.
    icon: code-pull-request
    ---

    # Review Workflow

    ## Change types

    | Change | Reviewer | Required before merge |
    | --- | --- | --- |
    | SOP copy cleanup | SOP owner | No process change. |
    | SOP behavior change | SOP owner and regional specialist | Changelog entry and affected-agent review. |
    | New process note | Note owner | Status label and related SOP link. |
    | Agent rule change | Knowledge owner and technical owner | Test prompt and stop condition review. |

    ## Review checklist

    * Does the page identify source status?
    * Does the change affect a customer-facing promise?
    * Are escalation conditions still clear?
    * Should the AI Assistant starter prompts change?
    * Is the changelog entry useful to operators?
    """,
)

write(
    "agent-governance/changelog.md",
    """
    ---
    description: Sample changelog for SOP and agent-governance changes.
    icon: clock-rotate-left
    layout:
      width: wide
    ---

    # Changelog

    {% updates %}
    {% update title="Added agent answer contract" date="2026-07-02" %}
    Defined safe answer types, stop conditions, and the required response shape for operational AI answers.
    {% endupdate %}

    {% update title="Promoted entity launch workflow to SOP" date="2026-07-02" %}
    Added the first approved demo SOP for new global entity launch, including scope, obligations, ERP setup, and readiness summary.
    {% endupdate %}

    {% update title="Created process-note lifecycle" date="2026-07-02" %}
    Added raw, reviewed, SOP candidate, and promoted statuses so notes can stay useful without becoming uncontrolled instructions.
    {% endupdate %}
    {% endupdates %}
    """,
)
