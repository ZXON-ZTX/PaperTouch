# Optional expert editing for computer science and security

Load this only when the user explicitly requests PaperTouch's expert mode, CS/security expert-style editing, or the equivalent in Chinese. It edits existing English prose. The original whitelist mode remains the default and its E1–E6 rules remain unchanged.

The aim is precise, field-appropriate expression of the author's existing work. This is a source-grounded editorial guide, not parameter training, a single author's voice, a human-authorship classifier, or a detector-score optimization procedure.

## Scope and working procedure

Use the supplied text, current task and any supplied author/venue guide to identify the target paragraph or section, its rhetorical purpose, and the permitted changes. A clear request for expert editing authorizes grammar, wording and local sentence-level cohesion inside that scope. Preserve paragraph boundaries and order, headings, tables, lists, quotations, code, mathematics, terminology, identifiers, numbers, units, citation/support relationships, and non-English passages. Structural revision, translation, drafting missing sections and scientific-claim correction require separate explicit authorization.

Read enough adjacent context to resolve references. Extract the existing actor/action/object, conditions, comparisons, research status and degree of certainty before editing. Improve only a demonstrable expression problem; keep a clear passage unchanged. Do not impose a sentence-length target, adjective quota, fixed abstract template or requirement to edit each paragraph. An intentional author preference takes precedence over a generic style preference, while evidence and protected content still take precedence over style.

After editing, compare each proposition with the source, including its negation and scope. A planned evaluation must remain planned; a potentially useful component must not become one that has been implemented. Missing evidence may be flagged outside the manuscript when the requested output allows it, but is not permission to erase an author's claim or insert support. Return the requested edited passage; provide reasons or a comparison only when asked. Audit-only requests do not produce a replacement manuscript. Do not add citations to the style-learning papers to a user's manuscript.

## Editorial principles and their limits

These are conditional editorial choices in expert mode, not new E-rules. Evidence locations and sampling limits are in [style-evidence.md](style-evidence.md); bibliographic records are in [style-sources.json](style-sources.json).

| ID | Choice when it resolves a real problem | What must stay intact |
|---|---|---|
| S1 | Put an already stated research object and its technical obstacle where the reader can identify them. Replace a vague referent with its existing antecedent when unambiguous. | No invented gap, motivation, deployment context or novelty claim. Never force every introduction to use the same opening. |
| S2 | Give actions to the appropriate actor: authors evaluate, an implementation checks, an attacker controls. Active `we` and passive constructions are both available. | Actor, agency, tense and completion state. Do not replace an implementation with a proposed method, or an assumption with a measured result. |
| S3 | Express threat assumptions using the existing adversary's access, knowledge, control, goal and exclusions. Keep the distinction between on-path/off-path, privileged/unprivileged, trusted/untrusted and pre-/post-authentication. | Every capability restriction, trust boundary, attacker goal and out-of-scope case. Do not fill a missing threat model from a standard attack scenario. |
| S4 | Connect an already stated design decision to the constraint or invariant it addresses. Prefer the actual operation to an empty assertion of sophistication. | Mechanism, ordering, proof obligation, conditions and tradeoff. Do not turn a functional description into a correctness or security guarantee. |
| S5 | In evaluation prose, clarify the question being answered and the relationship between target, baseline, workload and metric using information already supplied. | Versions, hardware, seeds, repeated runs, aggregation, denominators and comparison conditions. A testbed, simulation and production deployment must remain distinct. |
| S6 | Keep observation, interpretation and formal proof separate. State an observed result with its sample/condition; preserve the author's calibration of any explanation or generalization. | `may`, `suggests`, `we observed`, non-significance and other original certainty markers in meaning. Do not mechanically weaken valid theorems or strengthen empirical evidence. |
| S7 | State a known limitation as the specific boundary it places on a claim. Distinguish unsupported environments, prototype limitations and unknown generalizability. | Negative findings, excluded attacks, measurement bias, future work and failed cases. Do not delete limitations to make the contribution sound stronger. |
| S8 | Use connectors for actual contrast, cause, addition and reference. Make an ambiguous link explicit only when its relation is already in the source. | No added causality, fabricated contrast or stock transition between every sentence. `However`, `in this paper` and `in order to` are not prohibited expert-mode phrases. |
| S9 | Repeat a technical name when needed to keep its referent stable. Repair an ambiguous pronoun using a term already established by the author. | Defined terms, model-role names, symbols, acronyms, variant names and identifiers. Never rotate technical synonyms merely for variety. |
| S10 | Remove a genuine local redundancy or repair cumbersome grammar when the proposition is unchanged. Keep readable technical detail even when a sentence is long. | No compression of necessary parallel methods, conditions or evidence. Sentence rhythm and lexical variety are not independent reasons to rewrite. |

## Adapt to section and study type

Use only the row applicable to the given text. The table describes editorial focus, not a required outline or permission to insert missing content.

| Section/type | Editorial focus |
|---|---|
| Abstract | Keep the existing problem, technical response, principal evidence and scope legible. Never manufacture a metric or convert a measured subset into an Internet-wide claim. |
| Introduction / related work | Clarify the stated gap and contribution; preserve attribution and distinctions among prior approaches. A literature gap is not established by stronger wording. |
| Threat / security model | Preserve capabilities, trust assumptions, attacker goals and exclusions. Some measurement/user studies have methodological assumptions rather than an attacker model; do not invent one. |
| Design / implementation | Explain what each existing component does and why under the stated constraints. Preserve prototype status, ordering and invariants. |
| Evaluation / measurement | Make the original question, setup and comparison interpretable. Maintain the distinction among a vulnerable observation, a validated vulnerability, an exploit, prevalence and generalizability. |
| Discussion / limitations | Preserve the mechanism-to-evidence boundary, uncertainty and failure cases. A conjectured explanation remains conjectured. |
| User / privacy study | Keep reported perception separate from observed behavior, associations separate from causes, and participants separate from all users. |
| AI security | Preserve attacker knowledge/control, clean vs poisoned data, benign vs adversarial performance, IID/non-IID assumptions and the exact attack/defense setting. |
| Formal claim | Preserve definitions, quantifiers, premises and the proof/empirical distinction. This systems-heavy corpus does not justify prescribing mathematical proof style. |
| Rebuttal | Improve the expression of the actual answer and supplied evidence. Do not claim an experiment, artifact release or revision was completed if it is only proposed. Rebuttal writing was not directly sampled in this corpus. |

## Tools and acceptance

`scripts/apply_edits.py` remains exclusively an E1–E6 patch applicator. Do not give it an S-ID, relabel a broader rewrite as an E-rule, or relax its guards to force an expert edit through. Use the appropriate text/document editing tools and a separate source/result comparison for expert mode; preserve original files unless direct editing is authorized.

Verify scope, propositions, research status, protected spans and author preferences before delivering. For Word/PDF, use suitable document tools and separately inspect layout/revisions; the corpus work does not establish document-format support. A style-guide-consistent edit is not proof of human authorship, scientific correctness, acceptance probability or a reduced AI/similarity score.
