# NDP-xxxxx — [Short title of proposal]

**Proposal ID:** NDP-xxxxx
**Status:** Proposed
**Submitted by:** [Name or GitHub handle]
**Date submitted:** YYYY-MM-DD
**Related issues:** #[issue number] (if applicable)

---

## Summary

[One to three sentences describing what this proposal does and why.]

---

## Proposal Type

Select all that apply:

- [ ] New indicator concept
- [ ] New indicator version (modifies existing criteria)
- [ ] Add citations to existing indicator version
- [ ] Taxonomy change (new domain, reclassification, retirement)
- [ ] Documentation change

---

## Affected Entities

List the indicator, taxonomy, or documentation files affected by this proposal.

| Entity ID | File | Change Type |
|---|---|---|
| NDI-xxxxxx | `indicators/concepts/NDI-xxxxxx.yaml` | Create |
| NDI-xxxxxx-v1 | `indicators/versions/NDI-xxxxxx-v1.yaml` | Create |

---

## For New Indicator Concepts

### Normalized Name

```
[lowercase, stripped of punctuation, spaces collapsed]
```

### Generated ID

```
NDI-xxxxxx
```

Generated using: `python tools/id_generation.py "normalized name"`

### Title

[Noun phrase describing the indicator]

### Description

[Observable, neutral description of what the indicator represents. 2–5 sentences.]

### Evidence Categories

- [ ] inferred
- [ ] declared
- [ ] validated

---

## For New or Modified Indicator Versions

### Version

`NDI-xxxxxx-vN`

### Criteria

**Inferred:**

[What a researcher or analyst would look for in public sources. Be specific.]

**Declared:**

[What the organization would need to have publicly stated.]

**Validated:**

[What an accredited verifier would confirm.]

### Citations

**Supporting:**

- [Author(s). (Year). Title. Journal/Publisher. URL]

**Dissenting:**

- [Author(s). (Year). Title. Journal/Publisher. URL]

---

## For Taxonomy Changes

### Change Description

[Describe the proposed change to domains or domain assignments.]

### Affected Taxonomy Version

`NDT-x.x.x` → `NDT-x.x.x` (new version to be created)

### Node Changes

| Action | node_id | node_type | label |
|---|---|---|---|
| Add/Remove | | | |

### Edge Changes

| Action | source_id | relationship | target_id |
|---|---|---|---|
| Add/Remove | | | |

---

## Rationale

[Explain why this change is warranted. Include evidence of need, theoretical basis, or community demand. Reference the methodology document where relevant.]

---

## Open Questions

[List any unresolved questions you are raising for community discussion.]

---

## Files Included in This Proposal

- [ ] `proposals/NDP-xxxxx.md` (this file)
- [ ] `indicators/concepts/NDI-xxxxxx.yaml`
- [ ] `indicators/versions/NDI-xxxxxx-vN.yaml`
- [ ] `taxonomy/nodes/NDT-x.x.x-nodes.csv`
- [ ] `taxonomy/edges/NDT-x.x.x-edges.csv`

---

*Proposal submitted per the process described in [CONTRIBUTING.md](../CONTRIBUTING.md).*
