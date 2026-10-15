# T2D and attenuated weight loss during incretin-based therapy — review workspace

Narrative, mechanism-led review (not a systematic review) asking whether people with type 2 diabetes lose less weight on incretin-based therapy than people without diabetes, and why.

## Deliverables
| File | Content |
|---|---|
| **`paper/T2D_weight_loss_review.pdf`** | **Single typeset paper: full review, figures, tables, numbered references, supplementary appendix** |
| `manuscript/manuscript.md` (+ `.docx`, `.html`) | Assembled manuscript with numbered citations and bibliography (built, do not edit by hand) |
| `manuscript/sections/*.md` | Source sections (edit these; citations as `[@KEY]`) |
| `manuscript/outline.md` | Approved architecture |
| `Peripheral Incretin Signalling in T2DM.docx` | Author-supplied source document integrated as Section 5; every claim verified and eleven corrected (see `quality_control.md`) |
| `references/bibliography.md`, `references/references.json` | Vancouver-style bibliography generated from PubMed esummary |
| `references/verified_log.md` | Source-by-source verification log (population, numbers, access level) |
| `evidence/clinical_trials.csv` | Structured clinical extraction (Table 1 superset) |
| `evidence/matched_pairs.csv` | Matched comparisons and ratios (generated) |
| `evidence/mechanistic_studies.csv` | Study-level mechanistic extraction |
| `evidence/claim_evidence_ledger.csv` | Major claims → sources → verification status |
| `figures/` | Figure 1 (clinical phenotype), Figure 2 (integrative model), PNG + SVG + source |
| `analysis/derived.py` | All derived numbers (ratios, normoglycaemic estimate, energy scenarios) |
| `quality_control.md` | Limitations, unverified items, analyses not performed |
| `search_strategy.md` | Databases, queries, dates, access limits |

## Rebuild
```
python3 analysis/derived.py            # derived numbers + evidence/matched_pairs.csv
python3 figures/make_figures.py        # figures (needs matplotlib)
python3 analysis/build_manuscript.py   # numbering + bibliography (needs eutils.ncbi.nlm.nih.gov or cached esummary)
cd manuscript && pandoc manuscript.md -o manuscript.docx --resource-path=.:.. && cd ..
python3 analysis/build_paper.py && node analysis/render_pdf.js   # typeset paper (needs playwright + chromium)
```
`references/fulltext/` holds legally obtained open-access repository copies (STEP 1, SURMOUNT-2) used for verification; do not redistribute.
