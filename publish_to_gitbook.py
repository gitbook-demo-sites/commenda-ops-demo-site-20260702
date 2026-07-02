import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "https://api.gitbook.com/v1"
REPO = "commenda-ops-demo-site-20260702"
REPO_OWNER = "gitbook-demo-sites"
REPO_URL = f"https://github.com/{REPO_OWNER}/{REPO}.git"

SPACES = [
    {
        "key": "HOME",
        "sentinel": "XSPACE_HOME",
        "folder": "home",
        "title": "Home",
        "emoji": "1f3e0",
        "icon": "house",
        "path": "home",
        "description": "Demo framing, operating model, and review checklist.",
    },
    {
        "key": "SOPS",
        "sentinel": "XSPACE_SOPS",
        "folder": "sop-database",
        "title": "SOP Database",
        "emoji": "1f4cb",
        "icon": "list-check",
        "path": "sop-database",
        "description": "Versioned SOPs for entity launch, filings, ERP sync, and service delivery.",
    },
    {
        "key": "NOTES",
        "sentinel": "XSPACE_NOTES",
        "folder": "process-notes",
        "title": "Process Notes",
        "emoji": "1f5d2",
        "icon": "clipboard-list",
        "path": "process-notes",
        "description": "Living notes for country nuance, internal decisions, and field research.",
    },
    {
        "key": "AGENT",
        "sentinel": "XSPACE_AGENT",
        "folder": "agent-governance",
        "title": "Agent Governance",
        "emoji": "1f916",
        "icon": "robot",
        "path": "agent-governance",
        "description": "AI answer rules, MCP retrieval model, metadata, review workflow, and changelog.",
    },
]


def api(method: str, path: str, body=None, expected=(200, 201, 204)):
    token = os.environ["GITBOOK_TOKEN"]
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        BASE + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            text = resp.read().decode()
            payload = json.loads(text) if text else None
            if resp.status not in expected:
                raise RuntimeError(f"{method} {path} returned {resp.status}: {text}")
            return resp.status, payload
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode()
        raise RuntimeError(f"{method} {path} returned {exc.code}: {detail}") from exc


def git_commit_push(message: str):
    subprocess.run(["git", "add", "."], cwd=ROOT, check=True)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    if diff.returncode == 0:
        return
    subprocess.run(["git", "commit", "-m", message], cwd=ROOT, check=True)
    subprocess.run(["git", "push"], cwd=ROOT, check=True)


def replace_sentinels(space_ids: dict[str, str]):
    replacements = {item["sentinel"]: space_ids[item["key"]] for item in SPACES}
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in replacements.items():
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: GITBOOK_TOKEN=... python3 publish_to_gitbook.py <gitbook_org_id>")

    org_id = sys.argv[1]
    _, site = api(
        "POST",
        f"/orgs/{org_id}/sites",
        {"type": "ultimate", "title": "Commenda Operations Knowledge Base", "visibility": "share-link"},
    )
    site_id = site["id"]
    api(
        "PATCH",
        f"/orgs/{org_id}/sites/{site_id}",
        {
            "title": "Commenda Operations Knowledge Base",
            "visibility": "share-link",
            "basename": "commenda-operations-knowledge-base",
        },
    )

    created = {"org": org_id, "site": site_id, "spaces": {}, "sections": {}, "site_spaces": {}, "site_object": site}
    for item in SPACES:
        _, space = api(
            "POST",
            f"/orgs/{org_id}/spaces",
            {"title": item["title"], "emoji": item["emoji"], "empty": True, "editMode": "live"},
        )
        space_id = space["id"]
        created["spaces"][item["key"]] = space_id
        _, section = api(
            "POST",
            f"/orgs/{org_id}/sites/{site_id}/sections",
            {"spaceId": space_id, "title": item["title"], "icon": item["icon"], "draft": False},
        )
        section_id = section["id"]
        site_space_id = section["siteSpaces"][0]["id"]
        created["sections"][item["key"]] = section_id
        created["site_spaces"][item["key"]] = site_space_id
        api(
            "PATCH",
            f"/orgs/{org_id}/sites/{site_id}/sections/{section_id}",
            {
                "path": item["path"],
                "description": item["description"],
                "draft": False,
                "defaultSiteSpace": site_space_id,
            },
        )

    api(
        "PATCH",
        f"/orgs/{org_id}/sites/{site_id}",
        {"defaultSiteSection": created["sections"]["HOME"], "defaultSiteSpace": created["site_spaces"]["HOME"]},
    )

    replace_sentinels(created["spaces"])
    (ROOT / "gitbook-created.json").write_text(json.dumps(created, indent=2) + "\n", encoding="utf-8")
    git_commit_push("Resolve Commenda GitBook space links")

    imports = {}
    for item in SPACES:
        status, _ = api(
            "POST",
            f"/spaces/{created['spaces'][item['key']]}/git/import",
            {
                "url": REPO_URL,
                "ref": "refs/heads/main",
                "repoProjectDirectory": item["folder"],
                "repoTreeURL": f"https://github.com/{REPO_OWNER}/{REPO}/tree/main",
                "repoCommitURL": f"https://github.com/{REPO_OWNER}/{REPO}/commit",
                "force": True,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
            expected=(204,),
        )
        imports[item["key"]] = {"status": status, "space": created["spaces"][item["key"]], "folder": item["folder"]}
    (ROOT / "gitbook-import-results.json").write_text(json.dumps(imports, indent=2) + "\n", encoding="utf-8")

    logo = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO}/main/assets/commenda-wordmark.svg"
    customization = {
        "title": "Commenda Operations Knowledge Base",
        "localizedTitle": {},
        "internationalization": {"locale": "en"},
        "styling": {
            "theme": "clean",
            "primaryColor": {"light": "#16A34A", "dark": "#22C55E"},
            "infoColor": {"light": "#2563EB", "dark": "#93C5FD"},
            "successColor": {"light": "#16A34A", "dark": "#22C55E"},
            "warningColor": {"light": "#B45309", "dark": "#F59E0B"},
            "dangerColor": {"light": "#DC2626", "dark": "#F87171"},
            "tint": {"color": {"light": "#F7F4EF", "dark": "#111827"}},
            "corners": "rounded",
            "depth": "flat",
            "links": "accent",
            "font": "Inter",
            "monospaceFont": "IBMPlexMono",
            "icons": "regular",
            "background": "plain",
            "sidebar": {"background": "filled", "list": "line"},
            "codeTheme": {
                "default": {"light": "default-light", "dark": "default-dark"},
                "openapi": {"light": "default-light", "dark": "default-dark"},
            },
            "search": "prominent",
        },
        "favicon": {"icon": {"light": logo, "dark": logo}},
        "header": {
            "preset": "default",
            "logo": {"light": logo, "dark": logo},
            "links": [
                {"title": "SOP Database", "to": {"kind": "space", "space": created["spaces"]["SOPS"]}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "Process Notes", "to": {"kind": "space", "space": created["spaces"]["NOTES"]}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "Agent Governance", "to": {"kind": "space", "space": created["spaces"]["AGENT"]}, "style": "link", "links": [], "localizedTitle": {}},
                {"title": "Commenda", "to": {"kind": "url", "url": "https://www.commenda.io/"}, "style": "button-secondary", "links": [], "localizedTitle": {}},
            ],
        },
        "footer": {
            "logo": {"light": logo, "dark": logo},
            "groups": [
                {
                    "title": "Demo sections",
                    "localizedTitle": {},
                    "links": [
                        {"title": "Home", "to": {"kind": "space", "space": created["spaces"]["HOME"]}, "localizedTitle": {}},
                        {"title": "SOP Database", "to": {"kind": "space", "space": created["spaces"]["SOPS"]}, "localizedTitle": {}},
                        {"title": "Process Notes", "to": {"kind": "space", "space": created["spaces"]["NOTES"]}, "localizedTitle": {}},
                        {"title": "Agent Governance", "to": {"kind": "space", "space": created["spaces"]["AGENT"]}, "localizedTitle": {}},
                    ],
                },
                {
                    "title": "Sources",
                    "localizedTitle": {},
                    "links": [
                        {"title": "Source repo", "to": {"kind": "url", "url": f"https://github.com/{REPO_OWNER}/{REPO}"}, "localizedTitle": {}},
                        {"title": "Commenda website", "to": {"kind": "url", "url": "https://www.commenda.io/"}, "localizedTitle": {}},
                    ],
                },
            ],
            "copyright": "Commenda Operations Knowledge Base - first-draft GitBook demo.",
        },
        "themes": {"default": "light", "toggeable": True},
        "pdf": {"enabled": True},
        "feedback": {"enabled": True},
        "ai": {
            "mode": "assistant",
            "suggestions": [
                "What is the current entity launch SOP?",
                "How should we triage a filing deadline risk?",
                "When can a process note become an approved SOP?",
                "What should an agent do if two sources conflict?",
                "Which evidence is required for a transfer pricing pack?",
            ],
        },
        "advancedCustomization": {"enabled": True},
        "trademark": {"enabled": True},
        "externalLinks": {"target": "self"},
        "pagination": {"enabled": True},
        "pageActions": {"externalAI": True, "markdown": True, "mcp": True, "items": ["assistant", "markdown", "external-ai", "mcp", "pdf"]},
        "git": {"showEditLink": False},
        "privacyPolicy": {"url": "https://www.commenda.io/privacy-policy"},
        "socialPreview": {"url": f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO}/main/assets/commenda-ops-cover.svg"},
        "socialAccounts": [],
        "insights": {"trackingCookie": True},
    }
    _, customized = api("PUT", f"/orgs/{org_id}/sites/{site_id}/customization", customization)
    (ROOT / "gitbook-customization-result.json").write_text(json.dumps(customized, indent=2) + "\n", encoding="utf-8")

    publish_status, publish = api("POST", f"/orgs/{org_id}/sites/{site_id}/publish")
    share_status, share = api("POST", f"/orgs/{org_id}/sites/{site_id}/share-links", {"name": "Commenda operations demo review"})
    final = {
        "publish_status": publish_status,
        "publish": publish,
        "share_status": share_status,
        "share": share,
        "published_url": share["urls"]["published"],
        "app_url": publish["urls"]["app"],
        "preview_url": publish["urls"]["preview"],
        "repo": f"https://github.com/{REPO_OWNER}/{REPO}",
    }
    (ROOT / "gitbook-publish-share.json").write_text(json.dumps(final, indent=2) + "\n", encoding="utf-8")
    git_commit_push("Add Commenda GitBook publish artifacts")
    print(json.dumps(final, indent=2))


if __name__ == "__main__":
    main()
