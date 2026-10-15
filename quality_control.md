# Quality-control report

## Verification performed
- **Bibliography:** all 94 cited references resolve to PubMed records with DOIs. The bibliography was generated programmatically from NCBI esummary. For UKPDS 33 the PubMed record has no DOI, so the DOI was derived from the publisher PII and is flagged as such.
- **Per-source verification:** for every source, the population, design and the specific numbers used in the text were checked against the abstract (all sources) or the full text. The log is in `references/verified_log.md`, and claims are mapped in `evidence/claim_evidence_ledger.csv`.
- **Full texts read:** STEP 1 and SURMOUNT-2 including its supplement (open-access repository copies), the STEP-HFpEF pooled analysis, Perreault 2022, Rodriguez 2024 and Hall 2011 (PMC).
- **Corrections made during audit:**
  - (i) A cross-drug comparison of efficacy estimands (tirzepatide vs semaglutide) was removed.
  - (ii) An overstatement that liraglutide 0.6 mg "normalised HbA1c" was corrected to "improved glycaemia".
  - (iii) An unsourced claim that agonists "reset" the appetite set point was relabelled as an untested interpretation.

## Sources accessed at abstract level only (numbers limited to the abstract)
STEP 2, SURMOUNT-1, SCALE Obesity and Prediabetes, SCALE Diabetes, REDEFINE 1 and 2, ATTAIN-1 and 2, STEP-HFpEF and STEP-HFpEF DM (individually), STEP 6, OASIS 1, PIONEER PLUS, both retatrutide phase 2 trials, maridebart cafraglutide, Strathe 2023, and most physiology papers (Wing 1987, Bogardus 1986, Rave 2006, Heise 2022/2023, Ravussin 2025, Mäkimattila 1999, Carlson 1993).

## Items not verified or unresolved
1. **STEP 2:** the value for the 1.0 mg arm and the baseline weight/BMI were not in the abstract and are not stated in the manuscript.
2. **Strathe 2023:** whether diabetes status or HbA1c reduced the modelled maximal weight response is not verified, because the full text was blocked by the publisher. The manuscript states this explicitly.
3. **STEP 6:** the subgroup by diabetes status is not in the abstract and was not used.
4. **Baseline characteristics (sex, age, background therapy) of several trials:** these are not reported in their abstracts, so between-programme composition differences are described only where verified (STEP 1, SURMOUNT-2, ATTAIN-2, maridebart cafraglutide, STEP-HFpEF pool).
5. **Glycogen–water contribution:** this is general-physiology inference without a cited human measurement in this context, and it is labelled as inference.
6. **Hypoglycaemia-avoidant eating** with sulfonylureas or insulin is presented as a hypothesis, without a supporting primary source.
7. **"No study has compared appetite suppression by diabetes status"** and **"no study measured muscle glucose uptake, oxidation, glycogen and total EE together"** are absence-of-evidence statements. They are limited by the scope of the search (PubMed only).

## Derived values and assumptions
- **Matched-pair ratios** (`analysis/derived.py`): these are ratios of published ETDs. Pairs are not independent (two doses come from the same trials), and no meta-analytic pooling or confidence intervals were computed for the ratios.
- **STEP 1 normoglycaemic estimate (~−15.9%):** this assumes the overall mean is the subgroup-size-weighted average of the subgroup means, and it ignores differences in imputation.
- **Energy scenarios (Table 2):** glycosuria reductions of 10/25/45 g/day and REE reductions of 0/40/90 kcal/day are assumptions anchored to measured studies in other settings. The conversion uses Hall 2011 (≈23.9 kcal/day per kg at steady state; exponential approach with a 1-year half-time). The scenarios are not predictions for any trial.

## Analyses not performed
- Formal meta-analysis or meta-regression of the T2D × treatment interaction.
- Risk-of-bias assessment (RoB 2) and GRADE certainty rating.
- Adjustment of matched comparisons for age, sex, BMI or background therapy (requires IPD).
- Searches of Embase, Cochrane and regulatory documents (FDA/EMA reviews may contain subgroup analyses).

## Access limitations
- Publisher sites (NEJM, Lancet, Wiley, figshare) refused automated access (HTTP 403 or bot challenge) even after network allowlisting.
- Supplementary appendices for most trials were therefore unavailable.
- Supplying the PDFs of STEP 2, SURMOUNT-1, REDEFINE 1/2, ATTAIN-1/2 and the STEP-HFpEF trials would allow verification of baseline composition and subgroup analyses (for example, weight response by baseline HbA1c or sulfonylurea use). This is the most valuable next step for strengthening Section 2.5.
