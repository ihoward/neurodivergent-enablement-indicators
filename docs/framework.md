# NEI Framework Overview

## Purpose

The Neurodivergent Enablement Indicators (NEI) framework exists to make observable what is typically invisible: the organizational infrastructure that enables — or fails to enable — neurodivergent workers.

NEI does not measure neurodivergent identity. It measures organizations. Specifically, it documents signals of structural practices, policies, physical environments, and governance arrangements that either create or remove barriers for people with ADHD, autism, dyslexia, dyscalculia, dyspraxia, and related cognitive profiles.

The framework is designed to support:

- **External research and journalism** — using inferred evidence from public sources
- **Organizational self-assessment** — using declared evidence from internal policies
- **Third-party accreditation** — using validated evidence submitted to verifiers

---

## What NEI Is Not

- NEI is not a survey of neurodivergent employees about their experience.
- NEI is not a compliance checklist.
- NEI is not a certification program (though certifications may be built on top of it).
- NEI does not measure disability accommodations in the legal sense.

---

## Core Entities

### Indicators

An indicator describes an **observable signal** of organizational infrastructure. Indicators are:

- Stated at the conceptual level (the concept file)
- Versioned when their criteria change (the version files)
- Organized by evidence category: inferred, declared, or validated

Indicators describe what exists in the organization — not what the organization intends, claims to value, or aspires to become.

**Canonical identifier format:** `NDI-xxxxxx`

The six-character suffix is derived deterministically from the normalized indicator name using SHA-256 and base32 encoding. This means the same concept always produces the same ID, regardless of when it is created.

### Taxonomy

The taxonomy organizes indicators into **domains** — coherent areas of organizational practice.

Taxonomy is stored as structured tables, not embedded in indicator files. This separation means:

- Indicators can be reclassified without modifying their criteria
- An indicator can belong to multiple domains
- Taxonomy versions can evolve independently of indicator versions

**Taxonomy identifier format:** `NDT-<semver>`

### Proposals

All changes to indicators and taxonomy are introduced via **proposals**. A proposal is a formal document that describes the change, the rationale, the evidence basis, and any affected files.

**Proposal identifier format:** `NDP-xxxxx`

Proposals are numbered sequentially and retained permanently as a record of framework evolution.

### Releases

A release is a **versioned, stable snapshot** of the framework. A release manifest references exactly one taxonomy version and a specific list of standard indicator versions.

Releases define the version of the framework used for a given evaluation. Evaluations conducted against a released standard are reproducible.

**Release identifier format:** `NDR-<semver>`

---

## Identifier Design

All identifiers in NEI are designed to be:

- **Deterministic** — the same concept always produces the same ID
- **Stable** — IDs do not change when names are updated
- **Versioned** — version numbers are explicit and incremental
- **Self-describing** — the lifecycle stage is visible in the identifier during development

During development, an indicator's identifier encodes its lifecycle stage and the proposal that introduced it:

```
NDI-xxxxxxP-vN-NDP-xxxxx    # Proposed
NDI-xxxxxxC-vN-NDP-xxxxx    # Candidate
NDI-xxxxxx-vN               # Standard
```

Once an indicator reaches Standard, the lifecycle suffix is removed and the identifier is stable.

---

## Evidence Architecture

NEI recognizes three evidence categories that reflect the practical reality of how organizations can be observed:

| Category | Description | Who Can Observe |
|---|---|---|
| `inferred` | Observable via public signals without organizational cooperation | Researchers, journalists, analysts |
| `declared` | The organization publicly states the practice exists | The organization itself, or anyone with access to public statements |
| `validated` | Evidence submitted to and verified by an accredited verifier | Accredited third parties |

Not all indicators support all evidence categories. Each indicator version specifies criteria for each supported category.

---

## Taxonomy Domains

The initial taxonomy organizes indicators into six domains:

| Domain ID | Domain Name |
|---|---|
| `NDT-zk3lhx` | Administrative Accessibility |
| `NDT-wcjtfz` | Performance Evaluation |
| `NDT-znf2v5` | Organizational Clarity |
| `NDT-xyrxwd` | Sensory Environment |
| `NDT-6zfsxi` | Governance and Justice |
| `NDT-dxjmnq` | Support Infrastructure |

These domains are defined in the taxonomy node table for each taxonomy version.

---

## Current Maintainers

| Name | Organization | Role |
|---|---|---|
| atypical.business team | atypical.business | Primary maintainer |

*To propose a maintainer addition, open a governance proposal per [`GOVERNANCE.md`](../GOVERNANCE.md).*

---

## Design Rationale

### Why deterministic IDs?

Deterministic IDs mean two contributors who independently describe the same concept will generate the same ID. This prevents fragmentation and makes merging proposals easier.

### Why separate taxonomy from indicators?

Organizational categories are contested. What belongs under "accessibility" vs. "culture" vs. "governance" is a judgment call that will change over time. Separating taxonomy from indicators means those judgments can be revised without invalidating indicator criteria or historical evaluations.

### Why immutable versions?

If a standard indicator version could be silently modified, any evaluation conducted against it would be unreproducible. Immutability is the foundation of a reliable standards framework.

### Why three evidence categories?

The three categories reflect different evaluator relationships to the organization. A journalist has access to inferred evidence only. An HR team has access to declared evidence. An accredited verifier has access to validated evidence. A framework that conflates these produces criteria that are unusable for most evaluators.
