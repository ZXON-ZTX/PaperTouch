# English academic whitelist

These are six permitted editing operations, not an authorship detector. Each needs an identifiable local trigger AND all its exceptions checked. When several rules overlap, use the earliest rule that resolves the problem; do not stack edits on the same span. Examples are editing fixtures, never research evidence to insert into a manuscript.

## E1. Empty emphasis preface

Trigger: the exact preface `It is worth noting that`, `It is important to note that`, or `It should be emphasized that` introduces an assertion and adds no essential emphasis, attribution or logical relation. Remove only the shell, adjusting the following initial letter when needed.

Before: `It is worth noting that the samples were stored at 4 °C.`
After: `The samples were stored at 4 °C.`

Keep it if a supplied style guide deliberately requires the emphasis, if a reader warning actually depends on it, or if it is quoted. Do not treat all importance claims, warnings or caveats as empty. Do not replace a whole sentence or erase an otherwise substantive author judgment.

## E2. Two explicitly wordy function phrases

Trigger: `in order to` can be replaced by `to` without changing purpose or grammar; `due to the fact that` can be replaced by `because` without changing a causal statement. These are the complete phrase pairs for this rule, not invitations to simplify every formal expression.

Before: `The samples were randomized in order to reduce allocation bias.`
After: `The samples were randomized to reduce allocation bias.`

Keep author-prescribed wording, quotations, defined expressions and any occurrence whose grammatical attachment becomes ambiguous. Retain genuine `When...` conditions, `In terms of...` scope restrictions and legitimate passive constructions. Chinese translationese rules are not English syntax rules.

## E3. A redundant light verb around the same research action

Trigger: `performed an analysis of`, `conducted an evaluation of`, or `performed a comparison of` names only the corresponding act and can become `analyzed`, `evaluated`, or `compared` with unchanged tense, actor, purpose and arguments.

Before: `We conducted an evaluation of the encoder on the test split.`
After: `We evaluated the encoder on the test split.`

Keep a named method or defined object (`analysis of covariance`, `comparative evaluation protocol`), reported speech, or any construction where the noun denotes a distinct product. Preserve modality: `will conduct an evaluation` must not become a completed `evaluated`. Do not remove nominalizations generally or convert passive to active just for style. Adjust arguments only where the same relation is unambiguous; otherwise skip.

## E4. Immediately stacked additive connectors

Trigger: two adjacent additive markers (`Furthermore, additionally,`, `Moreover, in addition,`, or an equally explicit adjacent pair from Furthermore/Moreover/Additionally/in addition) perform the same addition relation. Remove the second marker only; keep the assertion and first marker.

Before: `Furthermore, additionally, we released the configuration files [3].`
After: `Furthermore, we released the configuration files [3].`

This is not a ban on sentence-initial connectors. Keep a contrast, condition, time or consequence marker (`however`, `therefore`, `when`, `meanwhile`), connectors in different sentences, legitimate parallel methods/results, and every numbered step. Do not vary technical names or sentence lengths to manufacture irregularity.

## E5. Two synonymous approximation markers on one numeric estimate

Trigger: `approximately about` or `roughly around` both modify the same immediately following numeric estimate. Retain the first approximation marker and the original value/unit; remove only the duplicate second marker.

Before: `The fitted value was approximately about 0.8 and may vary by site.`
After: `The fitted value was approximately 0.8 and may vary by site.`

Keep distinct uncertainties (`may be approximately`), formal terms (`approximate Bayesian computation`), spatial `around`, different quantities, author-prescribed wording and any ambiguous case. Never remove the remaining approximation, hedge or comparison. Do not turn approximate values into exact ones, introduce numbers, calculate new quantities or move measurements to another sentence.

## E6. Redundant ornamental occupational persona

Trigger: a tool `acts as/is like` a praise-laden imagined occupation (`a tireless assistant`, `a wise mentor`, `a faithful companion`) and the same clause already states the complete actual function. Replace only the ornamental framing by that supplied function; preserve every operational limit and measurable property.

Before: `The checker acts as a tireless assistant that flags missing citations.`
After: `The checker flags missing citations.`

Keep assistant/critic/teacher/student as actual model roles, named architectures, system agents or study conditions; keep a defined metaphor that conveys information not otherwise stated. If the persona implies an independent uptime, reliability or interaction claim that cannot be retained faithfully, skip rather than silently deleting it. Do not invent a capability, a person, a speed or a certainty claim to make the replacement concrete.

## Not in this whitelist

Keep genuine `not X but Y` contrasts and exclusions; numbered academic headings; meaningful colons and em dashes; mathematical minus/range signs; within-sentence parallel lists; repetitive terminology; passive methods; formal nominalizations; long or uniformly sized sentences; research questions; theoretical proofs; and cautious `suggests`/`may` statements. No English frequency thresholds or approved-vocabulary blacklist is supplied. Broader editorial concerns may be reviewed separately if explicitly requested, but are not grounds to change text in this pass.
