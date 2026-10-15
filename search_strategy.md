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

## Inclusion priorities
Matched-programme RCTs (same molecule/dose/duration/estimand) > harmonised/IPD or single-protocol cohorts > human physiology (clamps, tracers, calorimetry, ad libitum intake, fMRI) > observational cohorts > animal/cellular mechanism.

## Known retrieval gaps
- Embase, Cochrane CENTRAL, conference abstracts not searched.
- Supplementary appendices of most NEJM/Lancet trials not accessible (subgroups by baseline HbA1c, background therapy, sex).
- No formal search for unpublished IPD analyses or regulatory (FDA/EMA) review documents.
