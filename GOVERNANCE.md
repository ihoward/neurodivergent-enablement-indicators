# NEI Governance

This document describes how the Neurodivergent Enablement Indicators (NEI) framework is governed — how proposals are submitted, how indicators advance through their lifecycle, how releases are approved, and how the community participates.

---

## Principles

1. **Openness** — All changes are proposed and discussed publicly via pull requests.
2. **Versioning** — Indicators and taxonomy are versioned. Approved content is never silently modified.
3. **Reproducibility** — A numbered release pins a specific set of standard indicators, ensuring evaluations are comparable across time.
4. **Separability** — Taxonomy relationships are stored separately from indicator definitions. Indicators can be reclassified without changing their criteria.
5. **Evidence orientation** — Criteria must be grounded in observable evidence, not intentions or stated values.

---

## Roles

### Maintainers

Maintainers are responsible for:

- Facilitating proposal discussion
- Advancing proposals through lifecycle stages
- Approving and publishing releases
- Maintaining documentation quality

Maintainers are appointed by atypical.business. The list of current maintainers is in [`docs/framework.md`](docs/framework.md).

### Contributors

Any person may submit a proposal or comment on an open proposal. Contributions are governed by the terms in [`CONTRIBUTING.md`](CONTRIBUTING.md) and the project license in [`LICENSE`](LICENSE).

---

## Proposal Lifecycle

### Submission

A proposal is submitted as a pull request containing a completed `NDP-xxxxx.md` file in the `proposals/` directory.

Proposals may:

- Create a new indicator concept and initial version
- Modify the criteria of an existing indicator (creating a new version)
- Add citations to an existing indicator version
- Change taxonomy relationships (domain assignments)
- Propose a new taxonomy domain

### Review

Once submitted, a proposal enters the **Proposed** stage. Any community member may comment.

Maintainers may request clarification, evidence, or rewrites. The proposer is expected to respond within a reasonable timeframe.

### Candidate Stage

A maintainer may advance a proposal to **Candidate** when:

- The proposal is complete and well-specified
- No blocking objections remain unresolved
- At least one maintainer has reviewed and approved

Indicator files are updated to reflect the Candidate identifier format:

```
NDI-xxxxxxC-vN-NDP-xxxxx
```

### Standard Stage

A proposal advances to **Standard** when:

- The Candidate stage has been open for at least 14 days with no blocking objections
- A maintainer merges the pull request

Indicator files are updated to their final Standard format:

```
NDI-xxxxxx-vN
```

The associated proposal file is retained in `proposals/` as a permanent record.

---

## Indicator Versioning

An indicator version is immutable once it reaches Standard status. If criteria must change:

1. A new proposal must be submitted.
2. A new version file is created: `NDI-xxxxxx-v(N+1).yaml`
3. The previous version file is not modified.

This preserves the ability to reproduce historical evaluations against older releases.

---

## Taxonomy Versioning

The taxonomy version is updated when:

- A new domain is added
- An existing domain is renamed or retired
- Indicator-to-domain assignments change in aggregate

Taxonomy versions follow semantic versioning:

- **Patch** (`NDT-x.x.1`): Minor reclassification, no structural change
- **Minor** (`NDT-x.1.0`): New domain added
- **Major** (`NDT-2.0.0`): Structural reorganization

Each taxonomy version is recorded as a new pair of CSV files in `taxonomy/nodes/` and `taxonomy/edges/`.

---

## Release Approval

A release (`NDR-<version>`) is a versioned snapshot of the framework used for formal evaluation.

### Release criteria

A release manifest must:

- Reference exactly one Standard taxonomy version
- Reference only Standard indicator versions (no Proposed or Candidate)
- Include a complete list of indicator IDs to be evaluated

### Release process

1. A maintainer opens a release pull request with a new manifest in `releases/`.
2. The release is open for 14 days of community review.
3. At least two maintainers must approve.
4. The release is merged and tagged in the repository.

Releases are never modified after publication. A new release supersedes previous ones for new evaluations, but old releases remain valid for evaluations conducted under them.

---

## Dispute Resolution

If a contributor believes a decision was made incorrectly:

1. Open an issue describing the objection and the evidence for reconsideration.
2. Maintainers will review and respond within 30 days.
3. If unresolved, the matter is escalated to atypical.business for final determination.

---

## Amendments to Governance

Changes to this document follow the same proposal process as indicator changes and require approval of at least two maintainers.

---

*Maintained by [atypical.business](https://atypical.business)*
