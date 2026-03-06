# Neurodivergent Enablement Indicators (NEI)

**A taxonomy and indicator framework for observing the organizational infrastructure that enables neurodivergent workers.**

---

## Overview

The Neurodivergent Enablement Indicators (NEI) framework provides a structured, versioned set of observable signals that describe how well an organization's infrastructure supports neurodivergent workers.

NEI is not a survey instrument or a self-assessment tool. It is a **specification framework** — a set of defined indicators, a taxonomy of domains, and a governance model for evolving those definitions over time through open collaboration.

---

## Core Concepts

| Concept | Description |
|---|---|
| **Indicator** | An observable signal of organizational infrastructure. |
| **Taxonomy** | A domain hierarchy that organizes indicators into meaningful groups. |
| **Proposal** | A formal change request that introduces or modifies indicators or taxonomy. |
| **Release** | A versioned, stable snapshot of standard indicators used for evaluation. |

---

## Identifier Formats

| Entity | Format | Example |
|---|---|---|
| Indicator concept | `NDI-xxxxxx` | `NDI-3bvh2b` |
| Indicator version | `NDI-xxxxxx-vN` | `NDI-3bvh2b-v2` |
| Proposed indicator | `NDI-xxxxxxP-vN-NDP-xxxxx` | `NDI-3bvh2bP-v1-NDP-00001` |
| Candidate indicator | `NDI-xxxxxxC-vN-NDP-xxxxx` | `NDI-3bvh2bC-v1-NDP-00001` |
| Taxonomy release | `NDT-<semver>` | `NDT-1.0.0` |
| Proposal | `NDP-xxxxx` | `NDP-00001` |
| Standard release | `NDR-<semver>` | `NDR-1.0.0` |

---

## Indicator Lifecycle

```
Proposed  →  Candidate  →  Standard
```

- **Proposed**: Submitted via a pull request proposal. The indicator is under active discussion.
- **Candidate**: Accepted for inclusion pending final review and validation.
- **Standard**: Approved and included in a numbered release.

---

## Evidence Categories

Each indicator may support one or more evidence types:

| Category | Description |
|---|---|
| `inferred` | Observed via public signals (reviews, job descriptions, reports, filings). |
| `declared` | The organization publicly states the practice exists. |
| `validated` | Evidence submitted to and verified by an accredited verifier. |

---

## Repository Structure

```
nei/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── GOVERNANCE.md
│
├── docs/
│   ├── framework.md          # Conceptual overview and design rationale
│   ├── methodology.md        # How indicators are developed and validated
│   └── evidence_sources.md   # Approved source types per evidence category
│
├── indicators/
│   ├── concepts/             # One YAML file per indicator concept (NDI-xxxxxx.yaml)
│   └── versions/             # One YAML file per indicator version (NDI-xxxxxx-vN.yaml)
│
├── taxonomy/
│   ├── nodes/                # NDT-<version>-nodes.csv — domain node table
│   └── edges/                # NDT-<version>-edges.csv — indicator-domain relationships
│
├── proposals/
│   └── NDP-template.md       # Template for submitting a new proposal
│
├── releases/
│   └── NDR-template.yaml     # Template for a standard release manifest
│
└── tools/
    ├── id_generation.py      # Deterministic NDI ID generation
    └── validation_scripts.py # Repository integrity validation
```

---

## Concept vs. Version

Every indicator exists at two levels:

| Level | File | Purpose |
|---|---|---|
| **Concept** | `indicators/concepts/NDI-xxxxxx.yaml` | Stable definition of what the indicator represents. Never changes once assigned an ID. |
| **Version** | `indicators/versions/NDI-xxxxxx-vN.yaml` | The specific criteria used to assess the indicator at a point in time. A new version is created whenever criteria change. |

This separation means:

- The concept is permanent — the same ID always refers to the same idea.
- The criteria are versioned — evaluations reference specific versions for reproducibility.
- Citing an indicator in a release always pins both the concept and the criteria version.

---

## Taxonomy: The Only Source of Domain Relationships

**Domain membership and indicator relationships live exclusively in taxonomy tables.**

Indicator files (`indicators/concepts/`, `indicators/versions/`) do **not** contain domain assignments. This means:

- An indicator can belong to multiple domains without changing its definition.
- Domain reorganizations do not require modifying indicator files.
- Taxonomy can evolve on its own versioning cycle.

Taxonomy is stored as two CSV tables per taxonomy version:

| File | Description |
|---|---|
| `taxonomy/nodes/NDT-<version>-nodes.csv` | All nodes: root, domains, and indicators |
| `taxonomy/edges/NDT-<version>-edges.csv` | All relationships between nodes |

Relationship types include: `parent_of`, `contains`, `related_to`, `mitigates`, `reinforces`, `depends_on`.

---

## Candidate vs. Standard Releases

| Stage | Identifier format | Use |
|---|---|---|
| **Candidate release** | `NDR-<semver>C-NDP-<seed>` | Under review; not for formal evaluation |
| **Standard release** | `NDR-<semver>` | Approved; suitable for formal evaluation |

A Standard release manifest must reference **only Standard indicator versions** and a **Standard taxonomy version**. Candidate releases may reference Candidate indicators during their review period.

The current candidate release is [`NDR-0.1.0C-NDP-seed`](releases/NDR-0.1.0C-NDP-seed.yaml) — 30 indicators across 15 domains.

The current standard release is [`NDR-1.0.0`](releases/NDR-1.0.0.yaml) — 7 indicators across 6 domains.

---

## Getting Started

- To **understand the framework**, read [`docs/framework.md`](docs/framework.md).
- To **propose a new indicator or change**, read [`CONTRIBUTING.md`](CONTRIBUTING.md) and use the template in [`proposals/NDP-template.md`](proposals/NDP-template.md).
- To **evaluate an organization against a release**, use the release manifest in [`releases/`](releases/).
- To **generate a valid indicator ID**, use [`tools/id_generation.py`](tools/id_generation.py).

---

## Licensing

The NEI taxonomy and indicators are licensed under **Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)**.

Commercial use requires a license from atypical.business. See [`LICENSE`](LICENSE) for full terms.

---

## Governance

See [`GOVERNANCE.md`](GOVERNANCE.md) for the proposal process, lifecycle definitions, and release approval procedures.

---

*Maintained by [atypical.business](https://atypical.business) — licensing@atypical.business*
