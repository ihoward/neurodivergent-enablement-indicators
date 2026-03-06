# Contributing to the Neurodivergent Enablement Indicators (NEI)

Thank you for your interest in contributing. NEI is a community-governed framework and improvements come through open, structured proposals.

---

## What You Can Contribute

- **New indicators** — propose a new observable signal not yet in the framework
- **Modified indicators** — propose changes to criteria, evidence categories, or citations for an existing indicator
- **Taxonomy changes** — propose new domains, new domain relationships, or reclassification of indicators
- **Documentation improvements** — clarify methodology, evidence source definitions, or governance procedures
- **Citations** — add supporting or dissenting research citations to existing indicators

---

## Contribution Process

All substantive changes to indicators, versions, or taxonomy are introduced via a **Proposal (NDP)**.

### Step 1 — Open an Issue (optional but encouraged)

Before writing a full proposal, open an issue to describe the change you are considering. This allows early discussion before investment in a full write-up.

Label your issue with one of:
- `new-indicator`
- `modify-indicator`
- `taxonomy-change`
- `documentation`

### Step 2 — Write a Proposal

Copy the template from [`proposals/NDP-template.md`](proposals/NDP-template.md).

Assign your proposal a sequential ID: `NDP-xxxxx` (e.g., `NDP-00001`).

Save your proposal as `proposals/NDP-xxxxx.md`.

### Step 3 — Generate Indicator IDs (if applicable)

If your proposal introduces a new indicator concept, generate a canonical ID using:

```
python tools/id_generation.py "your normalized indicator name"
```

Include the generated ID in your proposal.

### Step 4 — Submit a Pull Request

Open a pull request that includes:

- Your proposal file under `proposals/`
- Any new or modified indicator files under `indicators/concepts/` or `indicators/versions/`
- Any taxonomy changes under `taxonomy/nodes/` or `taxonomy/edges/`

Title your pull request: `[NDP-xxxxx] Short description of change`

### Step 5 — Review and Discussion

Proposals are open for community comment. Maintainers will facilitate discussion and determine when a proposal is ready to advance.

Lifecycle stages:

| Stage | Meaning |
|---|---|
| **Proposed** | PR open, under discussion |
| **Candidate** | Accepted in principle, undergoing final review |
| **Standard** | Merged and included in a numbered release |

---

## File Conventions

### Indicator concepts

File: `indicators/concepts/NDI-xxxxxx.yaml`

Use the exact format specified in the concept template. Do not embed taxonomy assignments — those belong in the taxonomy edge tables.

### Indicator versions

File: `indicators/versions/NDI-xxxxxx-vN.yaml`

Increment the version number when criteria change. Do not modify an existing version file — create a new one.

### Taxonomy

Node and edge changes are made in the appropriate CSV files under `taxonomy/nodes/` and `taxonomy/edges/`.

---

## Style Guidelines

- Write indicator titles as noun phrases, not imperatives.
- Descriptions should be observable and neutral — avoid advocacy language.
- Evidence criteria should describe what a reviewer would look for, not what the organization should do.
- All text is written in plain English. No jargon without definition.

---

## Code of Conduct

This project follows a standard contributor code of conduct. Be respectful, specific, and evidence-oriented in all discussions. Personal attacks, dismissiveness toward lived experience, and bad-faith argumentation will not be tolerated.

---

*Questions? Contact us at [licensing@atypical.business](mailto:licensing@atypical.business)*
