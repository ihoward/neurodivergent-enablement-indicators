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

## Getting Started

- To **understand the framework**, read [`docs/framework.md`](docs/framework.md).
- To **propose a new indicator or change**, read [`CONTRIBUTING.md`](CONTRIBUTING.md) and use the template in [`proposals/NDP-template.md`](proposals/NDP-template.md).
- To **evaluate an organization against a release**, use the release manifest in [`releases/`](releases/).
- To **generate a valid indicator ID**, use [`tools/id_generation.py`](tools/id_generation.py).

---

## Licensing

The NEI taxonomy and indicators are licensed under **Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)**.

Commercial use requires a license from atypical.biz. See [`LICENSE`](LICENSE) for full terms.

---

## Governance

See [`GOVERNANCE.md`](GOVERNANCE.md) for the proposal process, lifecycle definitions, and release approval procedures.

---

*Maintained by [atypical.biz](https://atypical.biz) — licensing@atypical.biz*
