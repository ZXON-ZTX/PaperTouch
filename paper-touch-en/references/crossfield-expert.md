# Cross-disciplinary references for expert editing

Use these profiles only after the user selects expert mode. Identify the discipline and the paragraph's purpose from the manuscript or stated target. Apply the relevant profile alongside the shared preservation contract in [expert-editing.md](expert-editing.md). They add no whitelist rules, new editing permissions, compulsory sections, scientific validation or claims of domain-wide stylistic coverage.

The user-supplied classic-paper collection was a discovery list, not evidence that every link was verified or every paper read. Actual metadata checks, source versions, access failures and reading locations are recorded in [crossfield-sources.json](crossfield-sources.json). The small accessible sample supports case-based editorial references, not a universal expert voice or proof that a rewrite sounds human.

## Select the rhetorical task before changing prose

- **Derivation or model:** make the existing definitions, assumptions and logical transitions legible. Preserve quantifiers, boundary conditions, limiting regimes and approximation status. A derived bound is not a measured outcome.
- **Experiment or observation:** clarify the existing setup → observation → interpretation relationship. Preserve the experimental unit, controls, statistics, uncertainty and sample scope. Do not manufacture missing procedural detail.
- **Mechanism or review:** distinguish a proposed explanation, a demonstrated mechanism and the author's judgment. Keep attribution and appropriate qualifications. A persuasive review is not itself experimental validation.

These are optional ways to resolve an actual expression problem, not templates that every paragraph must follow. A clear paragraph can remain unchanged. The classic sources' ornate wording, typography, historical reporting practices and translated prose are not prescribed for contemporary manuscripts.

## Field profiles

| Profile | Useful editorial focus | Distinctions to preserve |
|---|---|---|
| Mechanics / control | Connect an existing physical idealization or invariant to the derivation, then make clear how a stated test relates to it. Put the author's model restriction near the claim it qualifies when local editing permits. | Small vs finite strain; plane stress vs plane strain; elastic vs plastic response; necessary vs sufficient conditions; calculated stability vs observed motion; approximation vs exact limiting case. No invented validity range. |
| Communications / signal processing | Keep definitions of the channel, rate or quantity stable before describing a result. Make a stated theorem's premises and limiting operation easy to follow; keep simulation evidence separate from a theoretical guarantee. | Symmetric capacity vs unrestricted capacity; binary-input/memoryless assumptions; finite length vs asymptotic behavior; strict inequalities; probability bounds; algorithmic complexity vs measured time. Do not generalize a result by deleting a channel condition. |
| Biomedical / biological methods | Preserve the progression from the material or construct actually studied to the measurement, inference and application claim. Clarify the referent of a model/structure/assay rather than treating them as interchangeable evidence. | Prediction vs experimental structure; structural compatibility vs established biological function; construct/mutant vs wild type; experimental unit and technical vs biological replicates; in vitro/animal/clinical settings. Only the first four distinctions have direct examples in this narrow structural/computational sample; replicate and translational safeguards are editorial protections, not corpus-frequency findings. |
| Chemistry / materials | Tie a claim to the stated chemical system, conditions or theoretical approximation. Keep a review's proposed synthesis strategy distinct from the evidence for an individual reaction or mechanism. | Ground-state/nondegenerate assumptions and approximation regimes; reaction conditions, compound identity, oxidation state and stereochemical notation; isolated yield vs conversion vs purity; suggested pathway vs demonstrated intermediate. The sample is a DFT paper and a synthesis review, not a representative experimental-chemistry corpus. |
| Physics / theoretical computation | Preserve the chain from stated observable/model to inference and its uncertainty. Make explicit which conclusions depend on priors or an idealized computational model, using only information already supplied. | Statistical vs systematic uncertainty; confidence interval vs credible region; local vs global significance; consistency vs unique identification; conjecture vs theorem; hypothetical quantum resource vs demonstrated hardware. Preserve the author's original calibration rather than mechanically weakening strong, supported claims. |
| Civil / energy / environment / aeronautical models | Clarify the stated model assumptions, prescribed inputs, boundary conditions and comparison with observations. Keep a modeled equilibrium response distinct from a time-dependent or regional forecast. | Isotropy, linearity and small-strain assumptions; ideal flow vs boundary-layer effects; modeled vs measured quantities; fixed vs evolving humidity; included vs omitted feedbacks; tested geometry and scale. The examples are historical consolidation, aeronautical and climate models, not coverage of all these engineering subfields or present-day design standards. |

## Located examples informing these profiles

IDs resolve to source/version records in crossfield-sources.json. These are paraphrased editorial observations, not text or results to insert into a user's manuscript. Page numbers include any cover in the retrieved file; XML block numbers refer to the documented local extraction.

| Sources and locations | Observation used in the profile |
|---|---|
| X006, PDF pp1–2; X025, author-manuscript pp1/3 | Explicit restrictions delimit approximate analysis; a theoretical model and a constructed demonstration serve different roles. |
| X026, corrected reprint pp1–3; X033, PDF pp1–2 (notation visually checked on p1) | Definitions, the permitted channel class and asymptotic premises are integral to the claim, not expendable background. |
| X071, XML blocks3/4/35; X072, XML blocks5/6/14/23 | Comparative accuracy, model applicability and structure-to-function inference are presented with different evidence and qualifications. |
| X077, PDF pp1–2/5; X083, PDF pp2–4 | A formal ground-state result and a research programme argued in a review require different treatment of certainty and scope. |
| X102, PDF pp1–3; X103, PDF pp2–3; X113, PDF pp1–2/6; X121, expanded manuscript pp1–3 | Measurements retain uncertainty and model dependence; a theoretical algorithm is described under a hypothetical resource model. |
| X126, NASA-hosted report pp2/4/6; X138, scanned PDF pp1/18; X123, public reprint transcription around Introduction/basic assumptions | Idealizations, prescribed quantities and empirical interpretation remain identifiable. Scanned/OCR text is not reliable authority for repairing notation. |

## Editing limits and practical use

If the discipline is not represented, use only the shared generic principles and any supplied author/venue guide; do not invent a field-specific norm. Mixed-domain papers may need more than one profile for different paragraphs, not a forced global voice. Do not impose an attacker model, software baseline or benchmark narrative on biology, mechanics or chemistry simply because the original PaperTouch corpus was security-focused.

Missing sample sizes, controls, uncertainty definitions or simulation conditions may need author input when material to the requested result. A language-editing request does not authorize inserting a plausible value, reconstructing a damaged formula from OCR, inventing causal support, removing an unsupported original claim or conducting a new scientific review. Preserve the original statement and, when needed, flag the precise unresolved issue outside the manuscript in the requested format.

The E1–E6 patch helper is still exclusively for whitelist mode. S-guidance and these field profiles are not acceptable patch rule IDs. Source paper PDFs, extracted full text and screenshots are local reading material and are not redistributed; original rights remain with the respective holders.
