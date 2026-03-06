# NEI Examples

Annotated examples mapping real-world workplace text to NEI indicators.

## Purpose

These examples serve three purposes:

1. **Illustrative** — show how NEI indicators map to observable signals in practice
2. **Evaluation** — provide test cases for tools and pipelines that apply NEI
3. **Training signal** — demonstrate correct indicator identification, evidence layer attribution, and reasoning

## Schema

Each example file is a JSON object following this schema:

```json
{
  "example_id": "EX-00001",
  "source_type": "glassdoor_review | job_posting | policy_document | news_article | employee_handbook | synthetic",
  "source_description": "Brief description of the source (no identifying information)",
  "text": "The verbatim or lightly anonymised source text",
  "indicators": [
    {
      "indicator_id": "NDI-xxxxxx",
      "version": "NDI-xxxxxx-v1",
      "title": "Indicator title",
      "evidence_layer": "inferred | declared | validated",
      "signal": "positive | negative | neutral",
      "evidence_basis": "What in the text maps to this indicator",
      "reasoning": "Why this indicator applies and how the text satisfies or fails the criteria"
    }
  ],
  "non_indicators": [
    {
      "description": "Something that might seem like an indicator but isn't",
      "reason": "Why it doesn't meet NEI criteria"
    }
  ],
  "notes": "Optional: caveats, ambiguities, or edge cases in this example"
}
```

### Field definitions

| Field | Description |
|---|---|
| `example_id` | Sequential identifier: `EX-00001`, `EX-00002`, etc. |
| `source_type` | Category of source material |
| `signal` | `positive` = practice present, `negative` = practice absent, `neutral` = signal exists but direction unclear |
| `evidence_basis` | The specific text or observation that triggers the indicator |
| `reasoning` | Full explanation of how the evidence maps to the indicator criteria |
| `non_indicators` | Counter-examples: things that look relevant but don't qualify |

## Files

Each example is a separate JSON file named `EX-{id}.json`.

## Contributing examples

Examples should use real-world text where possible, with minimal anonymisation. Synthetic examples are acceptable but should be clearly labelled as `source_type: synthetic`. All examples must include at least one `reasoning` explanation.

Submit examples as pull requests following the process in [CONTRIBUTING.md](../CONTRIBUTING.md).
