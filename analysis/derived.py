"""Derived quantities for the review. Pure standard library; run: python3 analysis/derived.py
Every input number is copied from a verified source (see references/verified_log.md, keyed by source ID).
Outputs: analysis/derived_outputs.md and evidence/matched_pairs.csv
"""
import csv, math, os, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ---------------------------------------------------------------------------
# 1. Matched molecule pairs: placebo-adjusted % weight change (ETD), no-T2D vs T2D
#    (drug %, placebo %) taken from primary abstracts; ETD = drug - placebo unless the
#    paper reports its own ETD (then the reported ETD is used and noted).
# ---------------------------------------------------------------------------
pairs = [
    # agent, dose, weeks_noT2D, weeks_T2D, noT2D source, (drug, pbo, reported ETD), T2D source, (drug, pbo, reported ETD), design note
    ("Semaglutide s.c.", "2.4 mg weekly", 68, 68, "STEP1", (-14.9, -2.4, -12.4), "STEP2", (-9.6, -3.4, -6.2),
     "Separate trials, same programme, same estimand (treatment policy)"),
    ("Semaglutide s.c. (HFpEF)", "2.4 mg weekly", 52, 52, "STEPHFpEF", (-13.3, -2.6, -10.7), "STEPHFpEF_DM", (-9.8, -3.4, -6.4),
     "Harmonised protocols; prespecified IPD pool; heterogeneity p<0.0001 (I2 95.8%)"),
    ("Tirzepatide", "10 mg weekly", 72, 72, "SURMOUNT1", (-19.5, -3.1, None), "SURMOUNT2", (-12.8, -3.2, -9.6),
     "Separate trials, same programme, treatment-regimen estimand"),
    ("Tirzepatide", "15 mg weekly", 72, 72, "SURMOUNT1", (-20.9, -3.1, None), "SURMOUNT2", (-14.7, -3.2, -11.6),
     "Separate trials, same programme, treatment-regimen estimand"),
    ("Orforglipron (oral)", "36 mg daily", 72, 72, "ATTAIN1", (-11.2, -2.1, None), "ATTAIN2", (-9.6, -2.5, -7.1),
     "Separate trials, same programme, treatment-regimen estimand"),
    ("Orforglipron (oral)", "12 mg daily", 72, 72, "ATTAIN1", (-8.4, -2.1, None), "ATTAIN2", (-7.0, -2.5, -4.5),
     "Separate trials, same programme, treatment-regimen estimand"),
    ("Cagrilintide + semaglutide", "2.4/2.4 mg weekly", 68, 68, "REDEFINE1", (-20.4, -3.0, -17.3), "REDEFINE2", (-13.7, -3.4, -10.4),
     "Separate trials, same programme, treatment-policy estimand"),
    ("Liraglutide", "3.0 mg daily", 56, 56, "SCALE_OB", None, "SCALE_DM", (-6.0, -2.0, -4.0),
     "SCALE Obesity abstract reports kg only (-8.4 vs -2.8 kg; baseline 106.2 kg); see kg comparison below"),
    ("Maridebart cafraglutide", "highest-response arm in each cohort", 52, 52, "MARITIDE2025", (-16.2, -2.5, None), "MARITIDE2025", (-12.3, -1.7, None),
     "Single protocol, two cohorts; dose/escalation arms differ between cohorts; GIPR antagonist"),
    ("Semaglutide s.c.", "7.2 mg weekly", 72, 72, "STEPUP", (-18.7, -3.9, -14.8), "STEPUP_T2D", (-13.2, -3.9, -9.3),
     "Separate trials, same programme, treatment-policy estimand; identical placebo-arm change (-3.9%) in both"),
]

rows = []
for agent, dose, wk1, wk2, s1, a, s2, b, note in pairs:
    if a is None:
        continue
    etd_a = a[2] if a[2] is not None else round(a[0] - a[1], 1)
    etd_b = b[2] if b[2] is not None else round(b[0] - b[1], 1)
    rows.append(dict(agent=agent, dose=dose, weeks=f"{wk1}/{wk2}", source_noT2D=s1, drug_noT2D=a[0], pbo_noT2D=a[1],
                     etd_noT2D=etd_a, source_T2D=s2, drug_T2D=b[0], pbo_T2D=b[1], etd_T2D=etd_b,
                     abs_gap_pp=round(etd_b - etd_a, 1), ratio_T2D_to_noT2D=round(etd_b / etd_a, 2), note=note))

# liraglutide kg comparison (SCALE Obesity reports kg; SCALE Diabetes reports both)
lira_noT2D_kg = -8.4 - (-2.8)          # SCALE_OB abstract
lira_T2D_kg = -6.4 - (-2.2)            # SCALE_DM abstract
lira_ratio_kg = lira_T2D_kg / lira_noT2D_kg

os.makedirs(os.path.join(ROOT, 'evidence'), exist_ok=True)
with open(os.path.join(ROOT, 'evidence', 'matched_pairs.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

ratios = [r['ratio_T2D_to_noT2D'] for r in rows]
gaps = [r['abs_gap_pp'] for r in rows]

# ---------------------------------------------------------------------------
# 2. STEP 1: implied weight change in normoglycaemic semaglutide-treated participants
#    Overall sema arm -14.9% (n=1306); prediabetes subgroup -13.7% (n=593)  [STEP1; PERREAULT2022]
#    Approximation: overall mean = weighted mean of subgroup means (ignores imputation differences).
# ---------------------------------------------------------------------------
n_all, n_pre = 1306, 593
m_all, m_pre = -14.9, -13.7
m_normo = (m_all * n_all - m_pre * n_pre) / (n_all - n_pre)

# ---------------------------------------------------------------------------
# 3. Energy-balance scenarios: glycosuria reduction and REE fall with glycaemic correction
#    Energy content of glucose: 3.75 kcal/g (anhydrous glucose ~15.6 kJ/g)
#    Hall 2011 (verified full text): permanent 100 kJ/day change -> ~1 kg steady-state change;
#    ~half reached at 1 year. 100 kJ = 23.9 kcal.
# ---------------------------------------------------------------------------
KCAL_PER_G = 3.75
KCAL_PER_KG_STEADY = 100 / 4.184   # 23.9 kcal/day per kg at steady state
TAU_YR = 1 / math.log(2)           # exponential approximation matching half-time of 1 year

def steady_kg(kcal_day):
    return kcal_day / KCAL_PER_KG_STEADY

def kg_at(weeks, kcal_day):
    return steady_kg(kcal_day) * (1 - math.exp(-(weeks / 52.18) / TAU_YR))

anchors = {
    'Bogardus 1986 (obese T2D, FPG 253->144 mg/dL; urine glucose 128->11 g/d)': (128 - 11) * KCAL_PER_G,
    'Carlson & Campbell 1993 (T1D; glycosuria 428->39 mmol/d)': (428 - 39) * 0.18016 * KCAL_PER_G,
    'Ferrannini G 2015 (empagliflozin-induced glycosuria, T2D)': 206.0,
    'Rave 2006 clamp: UGE if sustained 24 h at 7.8 mmol/L (0.06 mmol/min)': 0.06 * 1440 * 0.18016 * KCAL_PER_G,
    'Rave 2006 clamp: UGE if sustained 24 h at 13.3 mmol/L (0.77 mmol/min)': 0.77 * 1440 * 0.18016 * KCAL_PER_G,
}
# Bogardus REE fall: 31.9 -> 30.2 kcal/kg FFM/day; assume FFM 55-60 kg
ree_bogardus = [(31.9 - 30.2) * ffm for ffm in (55, 60)]

# Trial-like scenarios (assumptions, NOT measurements): differential (drug minus placebo) reduction
scen = [
    ('Low',     10, 0),
    ('Central', 25, 40),
    ('High',    45, 90),
]
scen_rows = []
for name, g, ree in scen:
    kcal = g * KCAL_PER_G + ree
    scen_rows.append((name, g, g * KCAL_PER_G, ree, kcal, steady_kg(kcal), kg_at(68, kcal), kg_at(72, kcal)))

# ---------------------------------------------------------------------------
out = []
out.append('# Derived outputs (generated by analysis/derived.py)\n')
out.append('## 1. Placebo-adjusted weight change in matched molecule pairs\n')
out.append('| Agent | Dose | Weeks | ETD no T2D (pp) | ETD T2D (pp) | Gap (pp) | Ratio T2D/no-T2D | Design |')
out.append('|---|---|---|---|---|---|---|---|')
for r in rows:
    out.append(f"| {r['agent']} | {r['dose']} | {r['weeks']} | {r['etd_noT2D']} | {r['etd_T2D']} | {r['abs_gap_pp']:+} | {r['ratio_T2D_to_noT2D']} | {r['note']} |")
out.append(f"\nLiraglutide 3.0 mg (kg, abstract data): placebo-adjusted -{abs(lira_noT2D_kg):.1f} kg (no T2D) vs -{abs(lira_T2D_kg):.1f} kg (T2D); ratio {lira_ratio_kg:.2f}.")
out.append(f"\nAcross the {len(rows)} %-based comparisons: ratio median {statistics.median(ratios):.2f} (range {min(ratios):.2f}-{max(ratios):.2f}); "
           f"absolute gap median {statistics.median(gaps):+.1f} pp (range {max(gaps):+.1f} to {min(gaps):+.1f}).")
out.append('Caveat: comparisons are between populations, not randomised by diabetes status; pairs are not independent (two doses from the same trials).\n')
out.append('## 2. STEP 1 implied normoglycaemic subgroup\n')
out.append(f'Overall semaglutide arm {m_all}% (n={n_all}); prediabetes {m_pre}% (n={n_pre}) -> implied normoglycaemia ~{m_normo:.1f}% (n={n_all-n_pre}).')
out.append('Graded pattern (cross-trial, unadjusted): normoglycaemia ~-15.9% > prediabetes -13.7% > T2D (STEP 2) -9.6% on the same dose and duration.\n')
out.append('## 3. Energy-balance anchors (measured inputs; kcal/day)\n')
for k, v in anchors.items():
    out.append(f'- {k}: {v:.0f} kcal/day')
out.append(f'- Bogardus 1986 RMR fall with sulfonylurea (1.7 kcal/kg FFM/day x FFM 55-60 kg): {ree_bogardus[0]:.0f}-{ree_bogardus[1]:.0f} kcal/day')
out.append(f'\nConversion: {KCAL_PER_G} kcal/g glucose; {KCAL_PER_KG_STEADY:.1f} kcal/day per kg steady-state (Hall 2011); exponential approach with half-time 1 year.\n')
out.append('## 4. Scenario estimates for a trial-like T2D population (assumption-driven)\n')
out.append('| Scenario | Differential glycosuria reduction (g/d) | kcal/d retained | Differential REE fall (kcal/d) | Total (kcal/d) | Steady-state kg | kg by wk 68 | kg by wk 72 |')
out.append('|---|---|---|---|---|---|---|---|')
for s in scen_rows:
    out.append(f'| {s[0]} | {s[1]} | {s[2]:.0f} | {s[3]} | {s[4]:.0f} | {s[5]:.1f} | {s[6]:.1f} | {s[7]:.1f} |')
out.append('\nInterpretation: these are upper-bound-style what-if calculations; they assume no behavioural compensation and that the ')
out.append('differential (drug minus placebo) change in glycosuria/REE persists. Observed placebo-adjusted gap STEP1 vs STEP2 ~6 pp (~6 kg at ~100 kg).')

open(os.path.join(HERE, 'derived_outputs.md'), 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
