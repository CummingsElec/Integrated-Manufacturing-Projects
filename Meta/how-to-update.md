# How to Update This Portfolio

Quick reference for maintaining the projects showcase repository.

---

## Quick Checklist

When updating a project:

- [ ] Update `projects/<project>/README.md` with new details
- [ ] Update `projects.json` with any changed metadata
- [ ] Update the top-level `README.md` if the summary changed
- [ ] Verify no sensitive info was accidentally added

---

## Adding a New Project

### 1. Create the Project Folder

```powershell
mkdir projects\new-project-name
```

### 2. Create the Project README

Create `projects/new-project-name/README.md` with this structure:

```markdown
# Project Name

**One-Line Tagline**

> Brief description

---

## Problem Statement
What problem does this solve?

## High-Level Architecture
Include a text diagram if helpful.

## Tech Stack
Table of technologies used.

## Core Features
Bullet points of main capabilities.

## Current Status
Production / Active Development / Prototype

## My Contributions
What you designed and implemented.

## Business Value
Measurable outcomes and impact.
```

### 3. Update projects.json

Add an entry to the `projects` array:

```json
{
  "id": "new-project-name",
  "name": "Display Name",
  "full_name": "Full Formal Name",
  "tagline": "One sentence description",
  "description": "2-3 sentence overview",
  "status": "active_development",
  "tech_stack": ["Tech1", "Tech2"],
  "categories": ["category1", "category2"],
  "highlights": ["Key feature 1", "Key feature 2"],
  "folder": "projects/new-project-name"
}
```

### 4. Update the Top-Level README

Add to the "Projects at a Glance" table:

```markdown
| [**New Project**](projects/new-project-name/) | Description | Tech Stack | Status |
```

Add a summary section under "Project Summaries".

### 5. Update Last Modified Date

In `projects.json`, update:

```json
"last_updated": "YYYY-MM-DD"
```

---

## Updating an Existing Project

### Status Change

1. Update `status` in `projects.json`
2. Update "Current Status" section in project README
3. Update top-level README table if needed

### Adding Features

1. Add to `highlights` array in `projects.json`
2. Update "Core Features" in project README
3. Optionally update the project summary in top-level README

### Tech Stack Changes

1. Update `tech_stack` in `projects.json`
2. Update "Tech Stack" table in project README
3. Update "Technical Highlights" in top-level README if cross-cutting

---

## Removing a Project

1. Delete `projects/<project-name>/` folder
2. Remove entry from `projects.json`
3. Remove from top-level README (table + summary)
4. Update `last_updated` date

---

## Security Checklist

Before committing, verify none of these appear:

| ❌ Never Include | ✅ Safe to Include |
|-----------------|-------------------|
| IP addresses | Generic descriptions ("internal network") |
| Credentials/tokens | Technology names |
| Internal URLs | Architecture diagrams (sanitized) |
| Customer names | Feature lists |
| Repo URLs | Business outcomes |
| Ticket numbers | Status information |
| Vendor account IDs | Tech stack details |

### Quick Grep Check

```powershell
# Check for IPs
Select-String -Pattern "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" -Path *.md,projects\**\*.md

# Check for common secrets patterns
Select-String -Pattern "(password|api_key|token|secret)" -Path *.md,projects\**\*.md
```

---

## Keeping Things in Sync

The three files that must stay aligned:

| File | Contains |
|------|----------|
| `README.md` | Human-readable overview, project table, summaries |
| `projects.json` | Machine-readable manifest, used by scripts |
| `projects/*/README.md` | Detailed per-project documentation |

**Rule of thumb:** If you update one, check if the others need updates too.

---

## Running the Summary Script

To print a formatted summary of all projects:

```powershell
python scripts\print_projects.py
```

This reads `projects.json` and outputs a formatted list—useful for quick reference or sharing.

---

## Version Control Tips

### Commit Message Format

```
[project-name] Brief description of change

- Detail 1
- Detail 2
```

Examples:
- `[cerberus] Update status to production`
- `[portfolio] Add new project: widget-factory`
- `[all] Update tech stack sections for accuracy`

### Branching (Optional)

For major updates, consider branching:

```powershell
git checkout -b update/project-name
# Make changes
git commit -m "[project-name] Description"
git checkout main
git merge update/project-name
```

---

## Questions?

This portfolio is maintained by Jacob Yount. For questions about the structure or update process, refer to the source READMEs in the private repositories for authoritative information.

