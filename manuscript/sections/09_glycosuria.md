## 9. Glycosuria, glycaemic correction and net energy balance

### 9.1 The premise

When plasma glucose exceeds the renal reabsorptive capacity, glucose is lost in urine and its energy leaves the body. In people with T2D under stepped hyperglycaemic clamps, urinary glucose excretion rose from 0.06 mmol/min at 7.8 mmol/L to 0.77 mmol/min at 13.3 mmol/L. Glycosuria persisted down to 7.8 mmol/L, and the threshold varied between people from 7.7 to 12.2 mmol/L [@RAVE2006]. Restoring glycaemia closes this energy leak. The energy is then retained, acting like an increase in intake, but only in people who were glycosuric, and only in the arm whose glycaemia improves.

### 9.2 Measured magnitudes

Three human studies measured the energy involved directly.

* In obese Pima Indians with T2D, 6 weeks of sulfonylurea lowered fasting glucose from 253 to 144 mg/dL and urinary glucose from 128 to 11 g/day. Resting metabolic rate per kilogram of fat-free mass also fell. To keep weight constant, daily intake had to be cut from 3070 to 2784 kcal [@BOGARDUS1986].
* In type 1 diabetes, intensive insulin therapy under constant intake reduced glycosuria from 428 to 39 mmol/day. Whole-room calorimetry showed a 5% (118 kcal/day) fall in 24-hour energy expenditure, and weight increased by 2.6 kg, almost all of it fat [@CARLSON1993].
* In insulin-treated T2D, improved glycaemia was an independent determinant of lower basal metabolic rate. The authors concluded that better glycaemic control promotes weight gain by reducing both metabolic rate and glucosuria [@MAKIMATTILA1999].

The reverse experiment confirms that urinary glucose energy matters to weight. SGLT2 inhibition with empagliflozin caused about 206 kcal/day of glycosuric loss, which predicted an 11.3 kg weight loss. Observed loss was 3.2 kg because calculated intake rose by about 13% [@FERRANNINI_G2015]. With canagliflozin, intake rose by about 100 kcal/day for each kilogram lost [@POLIDORI2016].

### 9.3 A formal model: Hall 2026

The most direct quantitative treatment of this question is a modelling study that appeared while this review was in preparation [@HALL2026]. It is the closest existing approach to proposed study 2 in Table 4, conducted *in silico* rather than by measurement.

The design is the important part. A previously validated model of human energy balance dynamics [@HALL2024] was fitted to the semaglutide response of participants *without* diabetes in STEP UP [@STEPUP], estimating the parameters that describe how semaglutide affects appetite and energy intake. Those appetite parameters were then **held fixed** and the model applied to STEP UP T2D [@STEPUP_T2D], adding only two diabetes-specific terms:

* **Urinary glucose excretion**, computed from estimated glomerular filtration rate, the renal threshold for glucose reabsorption [@POLIDORI2013] and plasma glucose derived from measured HbA1c via the ADAG equations [@NATHAN2008]. Mean eGFR in STEP UP T2D was 92 mL/min/1.73 m², so a normal renal threshold of 180 mg/dL was assumed.
* **Energy expenditure**, reduced by 3.5 kcal/day per mg/dL fall in fasting plasma glucose, a coefficient derived from cross-sectional data in which resting energy expenditure in obese T2D was better predicted when fasting glucose was included, and in which poor glycaemic control corresponded to an REE elevation of up to 8% [@GOUGEON2002].

Because appetite parameters were not refitted, any weight-loss gap the model reproduces is attributable to those two energetic terms alone, and any residual is not. The reported result is that the attenuation in patients not on background SGLT2 inhibitor therapy was **partially explained** by the UGE and expenditure changes [@HALL2026]. The author's conclusion is that these effects "can substantially offset negative energy balance," and that they "may partially explain" the gap — not that they account for it.

**The SGLT2 inhibitor prediction.** The model's most striking and counterintuitive output is that patients on *stable background* SGLT2 inhibitor therapy should show the **greatest** attenuation of weight loss. The logic is that an SGLT2 inhibitor lowers the renal threshold (modelled as 110 mg/dL), raising baseline UGE by roughly 100 g/day. Starting from that elevated baseline, semaglutide-induced glycaemic improvement produces a correspondingly larger fall in UGE, and so a larger energy offset. Crucially, the model predicts the opposite for *simultaneous initiation* of an SGLT2 inhibitor and an incretin agent, which should yield greater weight loss than either alone. Stable background therapy and co-initiation therefore move weight response in opposite directions — a distinction with direct implications for trial design and for interpreting the roughly 30% of STEP UP T2D participants who were on background SGLT2 inhibitors.

**What the model does not settle.** It is a simulation, not a measurement, and a preprint that has not been peer reviewed. The study is funded by AstraZeneca and the author is an employee of that company [@HALL2026]; this does not invalidate the analysis, whose assumptions are stated explicitly and are independently checkable, but it should be recorded. Its own stated limitations are substantial and align closely with the gaps identified elsewhere in this review: aggregate trial means rather than individual participant data; the renal threshold estimated from the literature rather than measured; real uncertainty about the magnitude and variability of the expenditure effect; sensitivity to the choice of HbA1c-to-average-glucose equation, with DCCT-derived equations predicting substantially greater baseline UGE and hence greater attenuation; HbA1c being a lagging indicator, which may distort early trajectories; the trial not reporting results separately by background SGLT2 inhibitor status, so the two simulations were averaged 30:70; and a higher proportion of women in STEP UP than in STEP UP T2D (~74% vs ~52%), a known modifier of weight response. The author's own recommendation is that future studies directly measure dynamic changes in UGE and energy expenditure to test the predictions.

One discrepancy should be flagged. The weight losses quoted in the preprint for STEP UP (approximately 18% and 21% at 72 weeks for 2.4 mg and 7.2 mg) and STEP UP T2D (approximately 11% and 14%) exceed the treatment-policy values in the primary publications (−15.6% and −18.7%; −13.2% for 7.2 mg) [@STEPUP; @STEPUP_T2D]. This is consistent with the model having been fitted to a trial-product or on-treatment estimand, but the preprint does not state which estimand was simulated. Table 1 uses the published treatment-policy values throughout.

### 9.4 Our own scenario estimates

None of the incretin trials measured urinary glucose or energy expenditure directly. Independently of the model above, we built transparent scenario estimates to bound the effect from measured inputs (Table 2; analysis/derived.py). Each assumes a *differential* reduction in glycosuria between drug and placebo arms, plus a differential fall in resting energy expenditure, persisting over the trial. We used 3.75 kcal per gram of glucose and the energy–weight relationship of Hall and colleagues: a permanent 100 kJ/day change yields about 1 kg at steady state, with half the change reached in about 1 year [@HALL2011]. For trial-like T2D populations with baseline HbA1c of about 8%, in which the drug lowers HbA1c by about 1.5 percentage points more than placebo [@SURMOUNT2], the retained energy could account for roughly 1 kg (low scenario) to 6–7 kg (high scenario) by 68–72 weeks. The observed placebo-adjusted gap between STEP 1 and STEP 2 is about 6 percentage points, or roughly 6 kg.

These calculations show that the energetics of glycaemic correction are *quantitatively capable* of explaining a meaningful share of the gap. They do not show that they do. Four caveats apply. Baseline glycosuria in trial populations was not measured and varies widely between individuals [@RAVE2006]. Behavioural compensation could be blunted by the drug's own anorectic effect, or it could add to the offset. The anchoring studies of metabolic rate involved poorer control than in modern trials [@BOGARDUS1986]. And the gradient seen in prediabetes, where glycosuria is negligible (Section 2.4), shows that glycosuria cannot be the whole explanation.

Our scenarios and the formal model agree on the central point and differ usefully in method. Both conclude that the energetics of glycaemic correction can account for a substantial but partial share of the gap. The model adds physiological structure our scenarios lack — a renal-threshold-based UGE calculation, an explicit expenditure coefficient, and dynamic rather than steady-state weight prediction — and it generates a testable prediction about background SGLT2 inhibition that scenario arithmetic could not reach. Neither rests on a single measurement of urinary glucose or energy expenditure made during incretin treatment, because none exists.

### 9.5 What the mechanism explains well, and what it does not

The mechanism fits three features of the clinical phenotype. It operates only in the arm whose glycaemia improves, so it predicts a deficit in drug-attributable rather than placebo-arm weight change, as observed — most cleanly in STEP UP and STEP UP T2D, where placebo-arm change was −3.9% in both [@STEPUP; @STEPUP_T2D]. Because people without diabetes have no glycosuria to lose, it predicts no offset in non-diabetes trials. And because the offset scales with the magnitude of glycaemic correction, it predicts a gradient with baseline HbA1c, which is what the within-T2D analyses show [@SATTAR2025; @ARODA2020].

It is also consistent with the gap appearing outside incretin pharmacology altogether (Section 2.5): any intervention that lowers weight and corrects glycaemia in T2D incurs the same energetic offset, whether it acts on the GLP-1 receptor, the 5-HT2C receptor, or the stomach [@HOLLANDER2013; @ONEIL2012; @COURCOULAS2015; @HENRY1986].

Two things it does not explain. The prediabetes step, where glycosuria is negligible yet roughly 2 percentage points of deficit have already appeared (Section 2.4). And the residual that the model itself leaves unexplained, which the author describes as partial explanation rather than full [@HALL2026]. Something further is operating, and Sections 5 to 8 and 10 set out the candidates.

**Table 2. Energy offsets from glycaemic correction: measured anchors and assumption-driven scenarios.**

| Source / scenario | Input | Energy (kcal/day) | Weight equivalent |
|---|---|---|---|
| Bogardus 1986, T2D, sulfonylurea [@BOGARDUS1986] | Urinary glucose 128 → 11 g/day (measured) | ~439 | — |
| Carlson & Campbell 1993, type 1 diabetes, intensive insulin [@CARLSON1993] | Glycosuria 428 → 39 mmol/day; 24-h EE −118 kcal/day (measured) | ~263 (glycosuria) + 118 (EE) | +2.6 kg in 2 months at constant intake |
| Ferrannini 2015, empagliflozin [@FERRANNINI_G2015] | Glycosuric loss (estimated from measurements) | ~206 | Predicted −11.3 kg; observed −3.2 kg (compensation) |
| Rave 2006 clamp [@RAVE2006] | UGE 0.06 → 0.77 mmol/min at 7.8 → 13.3 mmol/L | 58–749 if sustained for 24 h | — |
| Gougeon 2002, obese T2D (n=65) [@GOUGEON2002] | REE elevation with poor glycaemic control (measured, cross-sectional) | up to +8% of REE; modelled as 3.5 kcal/day per mg/dL fasting glucose [@HALL2026] | — |
| Hall 2026 model, T2D without background SGLT2i [@HALL2026] | UGE from eGFR, renal threshold 180 mg/dL and HbA1c-derived glucose, plus expenditure term | not stated as a single value | Partially explains the STEP UP T2D gap |
| Hall 2026 model, T2D on stable background SGLT2i [@HALL2026] | Renal threshold lowered to 110 mg/dL; baseline UGE ~100 g/day higher | ~375 (at 3.75 kcal/g) | Greatest predicted attenuation of all groups modelled |
| Scenario: low | 10 g/day differential glycosuria; no REE change | 38 | ~1.0 kg by 68–72 weeks |
| Scenario: central | 25 g/day; REE −40 kcal/day | 134 | ~3.3 kg by 68–72 weeks |
| Scenario: high | 45 g/day; REE −90 kcal/day | 259 | ~6.4–6.7 kg by 68–72 weeks |

Scenarios are illustrative assumptions, not measurements. Conversion: 23.9 kcal/day per kg at steady state; exponential approach with a 1-year half-time [@HALL2011].
