# Corpus and evidence for the optional expert mode

## What was actually studied

The corpus target is 100 distinct, publicly downloadable conference papers: 60 USENIX Security papers (2019/2021/2022), 20 NDSS 2022 papers, 10 OSDI 2022 papers and 10 NSDI 2021 papers. The fixed split is 80 development papers and 20 held-out papers. Bibliography, retrieval status, splits and PDF hashes are recorded in [style-sources.json](style-sources.json). Two inaccessible/poorly extracted initial entries were replaced in the same venue/topic/split using title-hash order, with the exclusion recorded.

Full-text acquisition and automatic phrase/section analysis are distinct from human-like close reading. The authoring agent inspected 76 located section windows across 26 development papers (79,600 extracted characters), focusing on abstracts, threat assumptions, evaluation and limitations. This does not mean every page of all 100 papers received a full semantic review. Automatically assigned topic tags and section labels are retrieval aids and may be imperfect.

The study deliberately uses a historical, systems-heavy open-access sample. Dates do not prove the text was written without assistance. Venue acceptance does not establish one universal expert style, flawless prose or scientifically correct claims. IEEE S&P, ACM CCS, journals, most other CS disciplines, recent work and rebuttals are not represented directly. No personal author voice, model weights, AI detector, human-reader experiment or publication outcome was trained or measured.

## Evidence map

Paper IDs below resolve in style-sources.json. Page numbers refer to the downloaded PDF, including any publisher cover. These entries are paraphrased editorial observations, not quotations, templates or findings to transfer into a manuscript. The choices are editorial inferences from samples, not measured universal norms.

| Principle | Located examples | Observed editorial move |
|---|---|---|
| S1: problem and obstacle | sec21-04, PDF p2; nsdi21-09, p2; osdi22-06, p2 | Establish the task or system constraint before explaining the technical response; identify what prior approaches make difficult. |
| S2: actor and research status | sec22-01, pp2/5; sec19-02, p3; osdi22-09, pp5/10 | Attribute capabilities and work to the correct entity; keep implementation, assumption and evaluated platform distinct. |
| S3: threat and trust boundaries | sec22-16, p4; ndss22-03, p3; ndss22-01, p4; osdi22-09, p5 | State access, control, knowledge and exclusions. Different assumptions can support prevention and detection claims. |
| S4: mechanism and invariant | sec22-16, pp2/8; osdi22-06, p2; sec22-08, pp6/10 | Explain why a mechanism fits its stated constraint; distinguish a design invariant from its performance measurement. |
| S5: evaluation question and comparison | sec21-19, p8; sec21-16, p8; nsdi21-02, p11; sec19-02, p11 | Relate experimental setup and baselines to specific questions rather than listing favorable numbers without context. |
| S6: observation vs inference | sec22-26, pp9/16; ndss22-06, p14; osdi22-09, p10 | Bound empirical claims by the tested sample and setting; a platform used as a proxy need not provide the same security enforcement. |
| S7: limitations and scope | sec21-04, p16; sec21-02, p14; sec19-02, p3; sec21-19, p13 | Explain what an implementation cannot yet model or what has not been evaluated, without treating all limitations as global failure. |
| S8: contextual cohesion | sec22-29, pp2/14; ndss22-08, p1; sec21-19, p8 | Transitions connect a particular gap, design response or evaluation purpose. Familiar academic phrases occur in legitimate prose. |
| S9: stable referents | sec22-16, p4; ndss22-17, p6; ndss22-14, p4 | Repeated attacker, component and model-role names preserve exact relationships across definitions and steps. |
| S10: local clarity without forced variety | sec22-27, pp2/5/11; sec21-04, p10; ndss22-01, p11 | Preserve the actual participant population or metric definition; improve a confusing sentence without replacing technical specificity. |

Additional inspected development material: sec21-08 (PDF pp2/12/13/15), sec21-14 (pp2/4/6), sec19-08 (pp2/6/14), ndss22-18 (pp1/2), nsdi21-09 (pp2/11/21). A window found by an automatic "limits" query can be an implementation constraint or a statement about prior work, not a study-wide limitations section; it is not treated as such without reading the context.

## Validation interpretation

The held-out set is paper-disjoint, not guaranteed author- or research-group-disjoint. It is reserved for checking whether the frozen editorial principles remain useful without forcing every section into one pattern. It is not a blind human preference test or an estimate of scientific-writing quality. Controlled invented paragraphs separately exercise mode routing and scientific-content preservation; they are not new experimental results. See the distribution's verification record for completed checks and their limits.

Corpus PDFs and full extracted text remain local study material and are not redistributed in the skill or release. The package includes source links, hashes, aggregate observations and paraphrased notes. Original paper copyrights remain with their respective holders; the skill's MIT license does not relicense those papers.
