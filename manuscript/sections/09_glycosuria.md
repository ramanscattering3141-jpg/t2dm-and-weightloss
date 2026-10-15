## 9. Glycosuria, glycaemic correction and net energy balance

### 9.1 The premise

When plasma glucose exceeds the renal reabsorptive capacity, glucose is lost in urine and its energy leaves the body. In people with T2D under stepped hyperglycaemic clamps, urinary glucose excretion rose from 0.06 mmol/min at 7.8 mmol/L to 0.77 mmol/min at 13.3 mmol/L. Glycosuria persisted down to 7.8 mmol/L, and the threshold varied between people from 7.7 to 12.2 mmol/L [@RAVE2006]. Restoring glycaemia closes this energy leak. The energy is then retained, acting like an increase in intake, but only in people who were glycosuric, and only in the arm whose glycaemia improves.

### 9.2 Measured magnitudes

Three human studies measured the energy involved directly.

* In obese Pima Indians with T2D, 6 weeks of sulfonylurea lowered fasting glucose from 253 to 144 mg/dL and urinary glucose from 128 to 11 g/day. Resting metabolic rate per kilogram of fat-free mass also fell. To keep weight constant, daily intake had to be cut from 3070 to 2784 kcal [@BOGARDUS1986].
* In type 1 diabetes, intensive insulin therapy under constant intake reduced glycosuria from 428 to 39 mmol/day. Whole-room calorimetry showed a 5% (118 kcal/day) fall in 24-hour energy expenditure, and weight increased by 2.6 kg, almost all of it fat [@CARLSON1993].
* In insulin-treated T2D, improved glycaemia was an independent determinant of lower basal metabolic rate. The authors concluded that better glycaemic control promotes weight gain by reducing both metabolic rate and glucosuria [@MAKIMATTILA1999].

The reverse experiment confirms that urinary glucose energy matters to weight. SGLT2 inhibition with empagliflozin caused about 206 kcal/day of glycosuric loss, which predicted an 11.3 kg weight loss. Observed loss was 3.2 kg because calculated intake rose by about 13% [@FERRANNINI_G2015]. With canagliflozin, intake rose by about 100 kcal/day for each kilogram lost [@POLIDORI2016].

### 9.3 Could this offset be large enough?

None of the incretin trials measured urinary glucose or energy expenditure. We therefore built transparent scenario estimates (Table 2; analysis/derived.py). Each assumes a *differential* reduction in glycosuria between drug and placebo arms, plus a differential fall in resting energy expenditure, persisting over the trial. We used 3.75 kcal per gram of glucose and the energy–weight relationship of Hall and colleagues: a permanent 100 kJ/day change yields about 1 kg at steady state, with half the change reached in about 1 year [@HALL2011]. For trial-like T2D populations with baseline HbA1c of about 8%, in which the drug lowers HbA1c by about 1.5 percentage points more than placebo [@SURMOUNT2], the retained energy could account for roughly 1 kg (low scenario) to 6–7 kg (high scenario) by 68–72 weeks. The observed placebo-adjusted gap between STEP 1 and STEP 2 is about 6 percentage points, or roughly 6 kg.

These calculations show that the energetics of glycaemic correction are *quantitatively capable* of explaining a meaningful share of the gap. They do not show that they do. Four caveats apply. Baseline glycosuria in trial populations was not measured and varies widely between individuals [@RAVE2006]. Behavioural compensation could be blunted by the drug's own anorectic effect, or it could add to the offset. The anchoring studies of metabolic rate involved poorer control than in modern trials [@BOGARDUS1986]. And the gradient seen in prediabetes, where glycosuria is negligible (Section 2.4), shows that glycosuria cannot be the whole explanation.

The mechanism does fit two features of the clinical phenotype. It operates only in the arm whose glycaemia improves, so it predicts a deficit in drug-attributable rather than placebo-arm weight change, as observed. And because people without diabetes have no glycosuria to lose, it predicts no offset in non-diabetes trials.

**Table 2. Energy offsets from glycaemic correction: measured anchors and assumption-driven scenarios.**

| Source / scenario | Input | Energy (kcal/day) | Weight equivalent |
|---|---|---|---|
| Bogardus 1986, T2D, sulfonylurea [@BOGARDUS1986] | Urinary glucose 128 → 11 g/day (measured) | ~439 | — |
| Carlson & Campbell 1993, type 1 diabetes, intensive insulin [@CARLSON1993] | Glycosuria 428 → 39 mmol/day; 24-h EE −118 kcal/day (measured) | ~263 (glycosuria) + 118 (EE) | +2.6 kg in 2 months at constant intake |
| Ferrannini 2015, empagliflozin [@FERRANNINI_G2015] | Glycosuric loss (estimated from measurements) | ~206 | Predicted −11.3 kg; observed −3.2 kg (compensation) |
| Rave 2006 clamp [@RAVE2006] | UGE 0.06 → 0.77 mmol/min at 7.8 → 13.3 mmol/L | 58–749 if sustained for 24 h | — |
| Scenario: low | 10 g/day differential glycosuria; no REE change | 38 | ~1.0 kg by 68–72 weeks |
| Scenario: central | 25 g/day; REE −40 kcal/day | 134 | ~3.3 kg by 68–72 weeks |
| Scenario: high | 45 g/day; REE −90 kcal/day | 259 | ~6.4–6.7 kg by 68–72 weeks |

Scenarios are illustrative assumptions, not measurements. Conversion: 23.9 kcal/day per kg at steady state; exponential approach with a 1-year half-time [@HALL2011].
