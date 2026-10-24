# Evidence grading and claim control

## Categories, not pseudo-precision

Use one status per claim, qualified by source quality, date and scope:

- **Verified**: directly demonstrated by reliable primary documentation or an independently executed check within the stated scope; not a universal guarantee.
- **Supported**: credible evidence favors the claim, but key parts have not been independently tested.
- **Mixed / context-dependent**: some aspects supported, others contradicted or dependent on unstated conditions.
- **Contradicted**: reliable evidence establishes the claim is inaccurate for the stated time/scope.
- **Unsubstantiated**: no adequate supporting evidence located after documented searching; this does not prove falsehood.
- **Unknown / inaccessible**: critical sources unavailable or not examined; no verdict.
- **Opinion / interpretation**: a preference or defensible reading, not a literal factual test.

Optional confidence is qualitative and explained: high/medium/low, never an invented probability. Keep **time-of-check** and **version** separate from the source's publication date.

## Source ladder

Primary artifacts (official release log, code commit, test output, signed filing, benchmark runner) generally outrank retellings for **what was published or run**. Independent corroboration matters for whether it was **true**. First-party material can verify *what the company claimed* without verifying *the claim itself*. Reviews, Reddit experiences and anecdotes should be attributed and contextualized; avoid treating a few reports as prevalence estimates. AI-generated summaries never substitute for opening original sources.

Examples:

- A changelog saying "hidden model names" verifies the changelog's statement about product behavior, not necessarily the behavior of every released build.
- A scored patch file may support **regrading**, but doesn't demonstrate the original agent generation is **reproducible**. Distinguish these.
- "We couldn't find a public CLI" describes the **search result**, not the universal absence of a CLI.
- "Model not disclosed" does not justify naming an assumed underlying model.
- A chart comparing scores under different settings can be *potentially misleading* even when the scores are correctly disclosed, but avoid inferring deceptive intent.
- A benchmark developed against an eval can support conclusions about **that** eval's independence; do not transfer the limitation to unrelated datasets without evidence.
- An updated product document can supersede an earlier post; report both chronology and current status.

## Source record fields

`source_id | canonical_url | title | publisher | published_at | observed_at | source_type | affiliation_or_dependency | accessed/full_text? | supporting_claim_ids | remarks`

Claim record fields:

`claim_id | precise_claim | claimant | first_seen_at | evaluated_as_of | scope/version | status | best_support_source_ids | best_counter_source_ids | direct_test? | key_limitations | impact_on_user`

Rules:

- Do not assert exact source/claim totals without maintaining the ledger.
- Preserve links to individual replies, PR comments, and changelog anchors where accessible.
- Mark user-supplied screenshots/quotes as user-supplied; do not assert their origin was independently verified until checked.
- Archive links supplement canonical live sources, not replace them automatically.
- Attribute all quoted language and avoid unnecessary lengthy copyrighted reproduction.
- Give a correction trail when your investigation reverses an earlier conclusion.
