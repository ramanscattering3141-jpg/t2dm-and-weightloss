# Quality-control report

## Verification performed
- **Bibliography:** all 124 cited references resolve to PubMed records with DOIs. The bibliography was generated programmatically from NCBI esummary. For UKPDS 33 the PubMed record has no DOI, so the DOI was derived from the publisher PII and is flagged as such.
- **Per-source verification:** for every source, the population, design and the specific numbers used in the text were checked against the abstract (all sources) or the full text. The log is in `references/verified_log.md`, and claims are mapped in `evidence/claim_evidence_ledger.csv`.
- **Full texts read:** STEP 1 and SURMOUNT-2 including its supplement (open-access repository copies), the STEP-HFpEF pooled analysis, Perreault 2022, Rodriguez 2024 and Hall 2011 (PMC).
- **Corrections made during audit:**
  - (i) A cross-drug comparison of efficacy estimands (tirzepatide vs semaglutide) was removed.
  - (ii) An overstatement that liraglutide 0.6 mg "normalised HbA1c" was corrected to "improved glycaemia".
  - (iii) An unsourced claim that agonists "reset" the appetite set point was relabelled as an untested interpretation.

## Corrections made while integrating the peripheral-signalling source document (Section 5)

The author-supplied document `Peripheral Incretin Signalling in T2DM.docx` was verified source by source against PubMed. All 21 of its unique references resolved to PubMed records. Eleven of its claims required correction before use, and these corrections are reflected in Section 5 and logged in `evidence/claim_evidence_ledger.csv` (C37-C58):

1. **Reduced GLP-1 secretion in T2D was presented as established.** Two meta-analyses (22 and 23 trials) find incretin secretion preserved on average in T2D, with reduction predicted by HbA1c and fasting glucose rather than by diabetes status [CALANNA_GLP1, CALANNA_GIP]. Section 5.2 now presents the individual studies and the meta-analyses together, and the graded-with-glycaemia reading replaces the uniform-deficit reading.
2. **DPP-4 "hyperactivity" in metabolic syndrome.** Neither cited source establishes that DPP-4 activity is higher than in people without diabetes. Zheng 2015 is cross-sectional within newly diagnosed T2D with no non-diabetic comparator; Malin 2013 is a 12-week exercise intervention in 14 people that measured neither GLP-1 nor body weight. The claim was narrowed to a within-T2D association with insulin resistance.
3. **Willard 2017 was described as pharmacological DPP-4 reduction normalising active GLP-1.** It is a genetic neprilysin-deficiency study in mice; lower DPP-4 activity was an associated finding, not an intervention. Reframed as evidence for neprilysin as a second degradative route.
4. **Duchen 1980 was described as "individuals with diabetes".** It is five post-mortem cases of early-onset *insulin-dependent* (type 1) diabetes with established clinical autonomic failure. Now stated explicitly, with its limited transfer to T2D populations.
5. **Lee 2012 was described as mice.** The study used UCD-T2DM *rats*, compared against prediabetic rats, not "prediabetic control mice".
6. **Malbert 2021 anatomical site.** The reduction in GLP-1 receptor binding potential was between the *splenic vein and the entrance of the liver*, not "between the porta hepatis and left gastric vein". Species is not stated in the abstract, so the porcine model is not asserted.
7. **Knauf 2008 receptor dependence.** The abolition of the response was demonstrated with *central* exendin 9-39 infusion and in GLP-1 receptor knockout mice; this is central, not portal, receptor dependence. The finding that high-fat feeding prevented the response entirely was not used in the source document and has been added, being more relevant.
8. **Autonomic neuropathy prevalence.** The figure of 18.6% at diagnosis is verified [BONORA2020]. The source document's "20 to 40% of those with known disease" could not be verified from the cited source and is not used; the reported range is instead given as very wide and test-dependent [AGASHE2018].
9. **The Nishizawa/Edgerton findings cut against the document's own thesis.** The source document states them correctly but treats them as compatible with a peripheral explanation of attenuated weight loss. Because the portal afferent receptor is not engaged by exendin-4 or exenatide, loss of endogenous portal signalling in T2D would lower the baseline rather than blunt the drug. Section 5.4 states this as the principal problem for the hypothesis.
10. **Numeric physiology claims drawn from reviews were dropped.** The document's "50-70% of the total postprandial insulin response", "more than 50% of an intravenous bolus inactivated within two minutes" and "half-life approximately 1-2 minutes" come from review articles whose abstracts do not contain them. Section 5.1 makes these points qualitatively, citing the reviews, and Section 3 retains the verified primary figures (36% vs 73% incretin contribution [NAUCK1986]).
11. **Hepatoportal emphasis.** The document frames the vagal route as hepatoportal. Hayes 2011 shows the common hepatic branch is not required, while complete subdiaphragmatic deafferentation is; the route is therefore described as paracrine signalling on gastrointestinal vagal afferents.

Material added beyond the source document, from new searches: human truncal vagotomy evidence [PLAMBOECK2013]; non-vagal counter-evidence [ZHANGRITTER2011]; route refinement [HAYES2011]; the only agonist-response study with measured peripheral changes [DUCA2013]; the two secretion meta-analyses; neprilysin; background metformin as a confounder acting opposite to the hypothesis [MCCREIGHT2016]; heterogeneity and frequent acceleration of gastric emptying in diabetes [CHEDID2019]; oral semaglutide bioavailability in T2D [OVERGAARD2021PK]; NTS preproglucagon circuit characterisation [HOLT2019].

## Sources accessed at abstract level only (numbers limited to the abstract)
STEP 2, SURMOUNT-1, SCALE Obesity and Prediabetes, SCALE Diabetes, REDEFINE 1 and 2, ATTAIN-1 and 2, STEP-HFpEF and STEP-HFpEF DM (individually), STEP 6, OASIS 1, PIONEER PLUS, both retatrutide phase 2 trials, maridebart cafraglutide, Strathe 2023, and most physiology papers (Wing 1987, Bogardus 1986, Rave 2006, Heise 2022/2023, Ravussin 2025, Mäkimattila 1999, Carlson 1993).

## Items not verified or unresolved
1. **STEP 2:** the value for the 1.0 mg arm and the baseline weight/BMI were not in the abstract and are not stated in the manuscript.
2. **Strathe 2023:** whether diabetes status or HbA1c reduced the modelled maximal weight response is not verified, because the full text was blocked by the publisher. The manuscript states this explicitly.
3. **STEP 6:** the subgroup by diabetes status is not in the abstract and was not used.
4. **Baseline characteristics (sex, age, background therapy) of several trials:** these are not reported in their abstracts, so between-programme composition differences are described only where verified (STEP 1, SURMOUNT-2, ATTAIN-2, maridebart cafraglutide, STEP-HFpEF pool).
5. **Glycogen–water contribution:** this is general-physiology inference without a cited human measurement in this context, and it is labelled as inference.
6. **Hypoglycaemia-avoidant eating** with sulfonylureas or insulin is presented as a hypothesis, without a supporting primary source.
7. **"No study has compared appetite suppression by diabetes status"**, **"no study measured muscle glucose uptake, oxidation, glycogen and total EE together"** and **"no study has measured endogenous incretin secretion, DPP-4 activity or autonomic function as predictors of weight response to an agonist"** are absence-of-evidence statements. They are limited by the scope of the search (PubMed only).
8. **Section 5 rests mainly on animal data.** Of the mechanisms in Section 5, only the secretion meta-analyses, the DPP-4 associations, the autonomic neuropathy prevalence, the gastric emptying distribution, the pharmacokinetics and the vagotomy study are human. The portal sensing, route-definition, neuropathy-function and agonist-response findings are all animal, in four different species, and none measured body weight.
9. **No human study has given a long-acting agonist to people differing in vagal function.** The central proposition of Section 5 is therefore untested in the population and with the drug class it concerns. Study 9 in Table 4 is the direct test.
10. **The receptor mediating hepatic vagal reception of portal GLP-1 has never been molecularly identified** [NISHIZAWA2000]. Statements about it are necessarily pharmacological inferences from antagonist and agonist insensitivity in anaesthetised rats.

## Derived values and assumptions
- **Matched-pair ratios** (`analysis/derived.py`): these are ratios of published ETDs. Pairs are not independent (two doses come from the same trials), and no meta-analytic pooling or confidence intervals were computed for the ratios.
- **STEP 1 normoglycaemic estimate (~−15.9%):** this assumes the overall mean is the subgroup-size-weighted average of the subgroup means, and it ignores differences in imputation.
- **Energy scenarios (Table 2):** glycosuria reductions of 10/25/45 g/day and REE reductions of 0/40/90 kcal/day are assumptions anchored to measured studies in other settings. The conversion uses Hall 2011 (≈23.9 kcal/day per kg at steady state; exponential approach with a 1-year half-time). The scenarios are not predictions for any trial.

## Analyses not performed
- Formal meta-analysis or meta-regression of the T2D × treatment interaction.
- Any quantitative apportionment of the weight-loss gap to peripheral versus central mechanisms. Section 5 deliberately reaches no numeric estimate, because no input to such a calculation has been measured in either population on treatment.
- Risk-of-bias assessment (RoB 2) and GRADE certainty rating.
- Adjustment of matched comparisons for age, sex, BMI or background therapy (requires IPD).
- Searches of Embase, Cochrane and regulatory documents (FDA/EMA reviews may contain subgroup analyses).

## Access limitations
- Publisher sites (NEJM, Lancet, Wiley, figshare) refused automated access (HTTP 403 or bot challenge) even after network allowlisting.
- Supplementary appendices for most trials were therefore unavailable.
- Supplying the PDFs of STEP 2, SURMOUNT-1, REDEFINE 1/2, ATTAIN-1/2 and the STEP-HFpEF trials would allow verification of baseline composition and subgroup analyses (for example, weight response by baseline HbA1c or sulfonylurea use). This is the most valuable next step for strengthening Section 2.5.
