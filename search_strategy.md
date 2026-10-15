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
- **Bariatric surgery as a parallel**: searches for an attenuated weight-loss phenotype by preoperative diabetes status did not retrieve a matched comparison of the quality required; this potentially informative parallel is therefore not used.
- **Immunogenicity / anti-drug antibodies** as an exposure explanation: nothing retrieved that stratified efficacy by diabetes status.
- **Heart rate variability or autonomic function as a predictor of GLP-1 receptor agonist weight response**: no studies retrieved. This absence is the basis for proposed study 7 in Table 4.

## Known retrieval gaps
- Embase, Cochrane CENTRAL, conference abstracts not searched.
- Supplementary appendices of most NEJM/Lancet trials not accessible (subgroups by baseline HbA1c, background therapy, sex).
- No formal search for unpublished IPD analyses or regulatory (FDA/EMA) review documents.
