# NEI Methodology

This document describes how indicators are developed, validated, and retired within the NEI framework.

---

## Indicator Development Process

### 1. Concept Identification

An indicator concept begins with the identification of an observable organizational signal. A good indicator:

- Describes something the organization **does or has**, not something it values or intends
- Is observable without relying on self-report from neurodivergent employees
- Is distinct from existing indicators (no duplication)
- Can be assessed using at least one evidence category

### 2. Name Normalization

The normalized name is the canonical representation of the concept used to generate the indicator ID. Normalization rules:

1. Convert to lowercase
2. Remove all characters that are not letters, digits, or spaces
3. Collapse multiple spaces to a single space
4. Trim leading and trailing whitespace

Example:

```
Input:    "Administrative Processes Simplified (Expense Reporting)"
Normalized: "administrative processes simplified expense reporting"
```

The normalized name must remain stable once an ID is generated. If the concept is substantially renamed, a new ID should be generated.

### 3. ID Generation

Indicator IDs are generated deterministically from the normalized name:

```
sha256(normalized_name)  →  base32_encode  →  lowercase  →  first 6 chars  →  prefix NDI-
```

See `tools/id_generation.py` for the reference implementation.

### 4. Criteria Development

For each supported evidence category, criteria describe **what a reviewer would look for** when assessing whether the indicator is present.

Criteria should be:

- **Specific** — what exactly is being looked for?
- **Observable** — can a reviewer determine this without asking the organization?
- **Graded** — where possible, criteria may specify levels of presence (e.g., partial vs. full)

Criteria must not:

- Require access to information unavailable to the intended evaluator
- Rely on employee sentiment or self-report
- Reference organizational values or stated intentions without observable evidence

### 5. Citation

Indicator version files include two citation lists:

- `citations.supporting` — research or literature that supports the indicator's relevance to neurodivergent enablement
- `citations.dissenting` — research or arguments that complicate or challenge the indicator

Both lists should be maintained honestly. Dissenting citations are not grounds for rejection — they are part of an intellectually honest framework.

---

## Versioning Rules

### When to create a new version

A new version (`NDI-xxxxxx-v(N+1)`) must be created when:

- Criteria for any evidence category change
- A previously supported evidence category is removed
- A new evidence category is added and criteria defined

### When NOT to create a new version

- Fixing a typo in a description (use an erratum proposal)
- Adding a citation (citations may be added to existing version files via proposal)
- Changing taxonomy assignments (taxonomy is separate from indicator files)

### Version immutability

Once an indicator version reaches Standard status, its file must not be modified. All changes require a new version.

---

## Concept Retirement

If an indicator concept becomes obsolete (e.g., the underlying practice no longer exists or has been superseded), it may be **retired**:

1. A proposal documents the rationale for retirement.
2. The concept file is updated to mark the concept as retired.
3. Future releases do not include retired concepts.
4. Existing releases that reference the indicator remain valid for evaluations conducted under them.

---

## Taxonomy Development

### Domain proposal

New domains are proposed with:

- A domain name and description
- A rationale for why existing domains are insufficient
- An initial set of indicators to be assigned to the new domain

### Domain retirement

Domains may be merged, split, or retired via proposal. Indicators assigned to a retired domain must be reassigned or retired simultaneously.

### Relationship types

The taxonomy edge table uses a `relationship` column. Current relationship types:

| Relationship | Meaning |
|---|---|
| `member_of` | The indicator belongs to this domain |

Additional relationship types may be proposed via governance process.

---

## Evaluation Methodology

### Selecting a release

Evaluations must specify the release version used (`NDR-<version>`). An evaluation conducted without a pinned release version is not reproducible.

### Evidence collection

Evaluators collect evidence for each indicator in the release manifest according to the criteria in the indicator version file.

Evidence is categorized as:

- `inferred` — collected from public sources without organizational input
- `declared` — collected from organizational public statements
- `validated` — submitted by the organization to an accredited verifier

### Scoring

NEI does not define a scoring methodology. Scoring is left to the evaluator or platform conducting the evaluation. The framework defines what is observable; it does not define how observations aggregate to a score or rating.

---

## Quality Standards for Proposals

A proposal that does not meet these standards will be returned for revision:

- [ ] Indicator name is distinctive and not duplicative of an existing concept
- [ ] Normalized name is specified
- [ ] ID has been generated using the reference tool
- [ ] At least one evidence category is specified with concrete criteria
- [ ] At least one supporting citation is provided
- [ ] The proposal explains how the indicator relates to neurodivergent enablement specifically
