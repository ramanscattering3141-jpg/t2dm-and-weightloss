# Search strategy and retrieval (conducted 15 October 2026)

**Type:** structured, targeted retrieval for a narrative review. No PRISMA screening, no duplicate independent screening, no risk-of-bias tool; not exhaustive.

## Sources and tools
- PubMed/MEDLINE via PubMed MCP connector (search, metadata, PMC full text, citation matching).
- ClinicalTrials.gov via MCP connector (trial registration/eligibility; posted results not returned by the tool).
- Unpaywall API, Europe PMC, Crossref, NCBI E-utilities (enabled mid-project by network allowlisting).
- Open-access repository copies (UCL Discovery, Ulster Pure). Publisher sites (nejm.org, thelancet.com, Wiley) returned 403 to automated access.

## Strategy
1. **Known-item retrieval** of landmark trials and physiology papers by citation (journal/volume/page/author), then verification of every record's abstract.
2. **Targeted searches** (examples):
   - `orforglipron[Title] AND (N Engl J Med[Journal] OR Lancet[Journal])`
   - `cagrilintide semaglutide REDEFINE`
   - `STEP-HFpEF pooled analysis semaglutide diabetes status weight`
   - `semaglutide prediabetes normoglycemia STEP trials glycemic status`
   - `tirzepatide prediabetes obesity 176 weeks diabetes prevention SURMOUNT-1`
   - `maridebart cafraglutide obesity phase 2 type 2 diabetes`
   - `(GLP-1 receptor agonist OR liraglutide OR semaglutide OR exenatide) AND energy expenditure AND (indirect calorimetry OR respiratory chamber) AND type 2 diabetes AND randomized`
   - `(GLP-1 receptor agonist ...) AND gastric emptying AND baseline gastric emptying AND type 2 diabetes AND scintigraphy`
   - `tirzepatide[Title] AND (energy intake OR appetite OR food intake) AND obesity`; `Martin CK[Author] AND tirzepatide`
   - Title-restricted searches for "(diabetes) AND (attenuated|less|lower) AND (weight loss)" — returned no dedicated comparative meta-analysis.
3. **Backward/forward tracking** from pivotal trials and pooled analyses (e.g., STEP-HFpEF pool, Perreault 2022).
4. **Peripheral incretin signalling (second round, 15 October 2026)**, prompted by the author-supplied document `Peripheral Incretin Signalling in T2DM.docx`. All 21 unique references in that document were resolved by citation matching (journal/volume/first page/author) and every record's abstract was then verified against the claim it was used for. Additional targeted searches extended the axis beyond the document:
   - `Calanna secretion of glucagon-like peptide-1 type 2 diabetes systematic review meta-analysis`; same for GIP
   - `vagotomy AND GLP-1 AND food intake` (yielded the human truncal vagotomy study and the non-vagal counter-evidence)
   - `GLP-1 receptor expression nodose ganglion diabetes obesity rodent`
   - `plasma dipeptidyl peptidase-4 activity increased type 2 diabetes compared controls`
   - `cardiovascular autonomic neuropathy prevalence type 2 diabetes review`
   - `diabetic gastroparesis prevalence scintigraphy type 2 diabetes cohort`
   - `semaglutide pharmacokinetics renal impairment hepatic impairment`
   - `(bile acid OR TGR5 OR GPBAR1) AND (GLP-1 secretion) AND (type 2 diabetes) AND human`
   - `(short-chain fatty acid OR microbiota) AND (GLP-1 secretion OR enteroendocrine) AND type 2 diabetes`
   - `(L-cell density OR enteroendocrine cell number) AND (type 2 diabetes OR obesity) AND human intestinal biopsy`
   - `preoperative diabetes predicts less weight loss after bariatric surgery`
   - `(semaglutide OR tirzepatide OR liraglutide) AND (antibodies OR immunogenicity) AND (efficacy OR exposure)`

## Inclusion priorities
Matched-programme RCTs (same molecule/dose/duration/estimand) > harmonised/IPD or single-protocol cohorts > human physiology (clamps, tracers, calorimetry, ad libitum intake, fMRI) > observational cohorts > animal/cellular mechanism.

## Peripheral-axis lines searched that yielded nothing usable
These were searched and are reported for completeness; none produced a source that met the inclusion priorities for a claim about diabetes status and weight response to an incretin agonist.
- **Bile acid / TGR5 signalling** and **microbiome / short-chain fatty acids** as determinants of L-cell secretion in T2D: the retrieved literature concerns metformin's gut pharmacology and mechanism reviews rather than any comparison relevant to agonist response. Only the metformin-background point was retained.
- **Enteroendocrine / L-cell density in human T2D intestinal biopsies**: no human study comparing L-cell density by diabetes status with a weight or agonist-response endpoint was retrieved. The reduced ileal L-cell number used in Section 5.7 is from a rodent diet-induced obesity model.
- **Bariatric surgery as a parallel**: direct searches did not retrieve a usable matched comparison. The reference trail of Hall 2026 subsequently supplied one [COURCOULAS2015], which is now cited in Section 2.5 for the direction of the association. This is a retrieval failure of the original search, recorded here rather than silently repaired.
- **Immunogenicity / anti-drug antibodies** as an exposure explanation: nothing retrieved that stratified efficacy by diabetes status.
- **Heart rate variability or autonomic function as a predictor of GLP-1 receptor agonist weight response**: no studies retrieved. This absence is the basis for proposed study 7 in Table 4.

## Third round: Hall 2026 and its evidence trail (16 October 2026)
Prompted by a reader query about a preprint published after the first draft. Retrieval:
- Web search identified `Why Do Patients with Type 2 Diabetes Lose Less Weight on GLP-1s? A Mathematical Modeling Analysis`, bioRxiv 10.64898/2026.09.08.750112.
- Metadata confirmed via the bioRxiv API (`api.biorxiv.org/details/biorxiv/...`) and Europe PMC (PPR1316883). Full text retrieved from the posted preprint HTML after repeated HTTP 429 rate limiting.
- Its reference list was then mined and each relevant source resolved by citation matching and verified against its PubMed abstract. This supplied: the STEP UP / STEP UP T2D matched pair, the non-incretin generality evidence (naltrexone-bupropion, lorcaserin, phentermine-topiramate, bariatric surgery, formula diets), the within-T2D HbA1c gradient, and the model's own inputs (ADAG, renal threshold, the energy-expenditure coefficient).
- This round materially changed the review's conclusions and corrected a sign error in proposed study 6 (see `quality_control.md`).

**Note on preprint retrieval:** bioRxiv rate-limits automated access aggressively. Metadata is reliably available through its API; full text required repeated retries. Preprints are not indexed in PubMed, so the PubMed-only strategy declared above would not have found this paper. That is a structural gap in the search, now explicit.

## Fourth round: intake-expenditure coupling (16 October 2026)
Prompted by a reader pointing out that energy intake rises with energy expenditure, which the energy-balance arithmetic of Section 9 had treated as independent. Searches:
- `Doucet compensation energy deficits exercise diet review`
- `Blundell energy expenditure drives energy intake fat-free mass resting metabolic rate appetite`
- `resting metabolic rate fat-free mass determinants of energy intake tonic drive to eat`
This round identified a construction error in our own scenario arithmetic rather than a gap in the literature retrieved; see `quality_control.md`. It is recorded here because the original search strategy never covered the energy-compensation literature at all, despite that literature bearing directly on every quantitative claim in Section 9.

## Known retrieval gaps
- Embase, Cochrane CENTRAL, conference abstracts not searched.
- **The energy-compensation and appetite-control literatures were not searched in the original strategy**, which was built around diabetes and incretin terms. They were added only in the fourth round. Other adjacent literatures may be similarly missing.
- **Preprint servers (bioRxiv, medRxiv) were not searched systematically.** Hall 2026 was found only because a reader asked about it. Any other relevant preprint remains unretrieved.
- Supplementary appendices of most NEJM/Lancet trials not accessible (subgroups by baseline HbA1c, background therapy, sex).
- No formal search for unpublished IPD analyses or regulatory (FDA/EMA) review documents.
