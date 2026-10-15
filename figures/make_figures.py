"""Generates manuscript figures (PNG + SVG). Run: python3 figures/make_figures.py
Figure 1: matched-pair placebo-adjusted weight change (reads evidence/matched_pairs.csv) + glycaemic gradient.
Figure 2: integrative conceptual model with evidence-strength line styles.
Palette: reference categorical slots 1-2 (validated adjacent pair), text in neutral inks."""
import csv, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
BLUE, ORANGE = '#2a78d6', '#eb6834'
INK, INK2, MUTED, GRID, SURF = '#0b0b0b', '#52514e', '#8a8984', '#e4e3df', '#fcfcfb'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9, 'axes.edgecolor': MUTED,
                     'axes.labelcolor': INK2, 'xtick.color': INK2, 'ytick.color': INK2,
                     'figure.facecolor': SURF, 'axes.facecolor': SURF, 'savefig.facecolor': SURF})

# ---------------- Figure 1 ----------------
rows = list(csv.DictReader(open(os.path.join(ROOT, 'evidence', 'matched_pairs.csv'))))
fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 5.8), gridspec_kw={'width_ratios': [2.1, 1]})
labels = [f"{r['agent']}\n{r['dose']} ({r['weeks'].split('/')[0]} wk)" for r in rows]
y = list(range(len(rows)))[::-1]
for yi, r in zip(y, rows):
    a, b = float(r['etd_noT2D']), float(r['etd_T2D'])
    ax.plot([a, b], [yi, yi], color=GRID, lw=2, zorder=1, solid_capstyle='round')
    ax.scatter(a, yi, s=64, color=BLUE, edgecolor=SURF, linewidth=2, zorder=3)
    ax.scatter(b, yi, s=64, color=ORANGE, edgecolor=SURF, linewidth=2, zorder=3, marker='D')
    ax.text(0.4, yi, f"ratio {float(r['ratio_T2D_to_noT2D']):.2f}", va='center', ha='left', color=INK2, fontsize=8)
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=7.6, color=INK)
ax.set_xlim(-19.5, 3.2); ax.axvline(0, color=MUTED, lw=0.8)
ax.set_xlabel('Placebo-adjusted change in body weight (percentage points)')
ax.grid(axis='x', color=GRID, lw=0.6); ax.set_axisbelow(True)
for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
ax.legend(handles=[Line2D([], [], marker='o', ls='', color=BLUE, ms=7, label='Population without diabetes'),
                   Line2D([], [], marker='D', ls='', color=ORANGE, ms=6, label='Population with type 2 diabetes')],
          loc='upper center', bbox_to_anchor=(0.45, -0.12), ncol=2, frameon=False, fontsize=8)
ax.set_title('A  Same molecule, dose and duration; separate populations', loc='left', fontsize=10, color=INK, pad=12)

cats = ['Normo-\nglycaemia\n(STEP 1,\nimplied)', 'Pre-\ndiabetes\n(STEP 1)', 'Type 2\ndiabetes\n(STEP 2)']
vals = [-15.9, -13.7, -9.6]
cols = [BLUE, BLUE, ORANGE]
bx.bar(range(3), vals, color=cols, width=0.6, edgecolor=SURF, linewidth=2)
for i, v in enumerate(vals):
    bx.text(i, v - 0.6, f'{v:.1f}%', ha='center', va='top', color=INK, fontsize=9)
bx.set_xticks(range(3)); bx.set_xticklabels(cats, fontsize=8, color=INK)
bx.set_ylim(-19, 0); bx.axhline(0, color=MUTED, lw=0.8)
bx.set_ylabel('Mean change in body weight at week 68 (%)')
bx.grid(axis='y', color=GRID, lw=0.6); bx.set_axisbelow(True)
for s in ('top', 'right', 'bottom'): bx.spines[s].set_visible(False)
bx.set_title('B  Graded with dysglycaemia\n    (semaglutide 2.4 mg, unadjusted)', loc='left', fontsize=10, color=INK, pad=12)
fig.text(0.01, 0.01, 'Cross-trial comparisons, not randomised by diabetes status. Normoglycaemic value derived (analysis/derived.py).',
         fontsize=7.5, color=MUTED)
fig.tight_layout(rect=(0, 0.05, 1, 1))
for ext in ('png', 'svg'):
    fig.savefig(os.path.join(HERE, f'figure1_clinical_phenotype.{ext}'), dpi=220)
plt.close(fig)

# ---------------- Figure 2 ----------------
fig, ax = plt.subplots(figsize=(12, 7.6)); ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

def box(x, y, w, h, title, body, edge=INK2, fill='#ffffff'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.4,rounding_size=1.2', fc=fill, ec=edge, lw=1.2))
    ax.text(x + w / 2, y + h - 1.6, title, ha='center', va='top', fontsize=9, fontweight='bold', color=INK)
    ax.text(x + w / 2, y + h - 5.4, body, ha='center', va='top', fontsize=7.4, color=INK2, linespacing=1.35)
    return (x, y, w, h)

STY = {'established': dict(ls='-', lw=1.8), 'human': dict(ls=(0, (6, 3)), lw=1.6), 'hypothesis': dict(ls=(0, (1.5, 2.5)), lw=1.6)}
def arrow(p, q, kind, color=INK2, rad=0.0):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=12, color=color, connectionstyle=f'arc3,rad={rad}', **STY[kind]))

box(1, 74, 22, 22, 'T2D state', 'Hyperglycaemia; glycosuria\nInsulin resistance (muscle,\nliver, adipose)\nReduced incretin effect\nAutonomic/GI change\nOlder, more male cohorts\nSU / insulin co-therapy')
box(30, 74, 40, 22, 'Incretin-based drug: exposure & receptor engagement',
    'Same dose & duration in matched programmes\nExposure determined chiefly by body weight\n(popPK; T2D data)  ·  GI tolerability and\ndiscontinuation similar or lower in T2D trials\n-> drug exposure unlikely to explain the gap')
box(76, 74, 23, 22, 'Observed phenotype', 'Placebo-adjusted weight loss\n~0.5-0.8 x that in\npopulations without diabetes\n(median ~0.6; 2-7 pp)\nPlacebo-arm loss NOT lower')

box(1, 38, 30, 28, '1  Energy intake', 'Appetite, satiation, food reward\n(hypothalamus, hindbrain, CVOs,\nmesolimbic; vagal afferents)\nSuppression shown in T2D (human)\nMagnitude vs non-T2D: untested\nGastric emptying: tachyphylaxis;\nbaseline-dependent (diabetes)')
box(35, 38, 30, 28, '2  Energy expenditure & storage', 'REE falls as glycaemia corrects\n(T2D RMR elevated; sulfonylurea,\ninsulin studies)  ·  substrate\npartitioning / fat oxidation\n(tirzepatide: more fat oxidation,\nno change in adaptation; non-T2D)\nGlycogen-water shifts (inference)')
box(69, 38, 30, 28, '3  Energy losses', 'Glycosuria eliminated as glucose\nfalls below the renal threshold\n(measured: 100+ g/d in poor control;\nSGLT2i: ~200 kcal/d drives\ncompensatory intake)\nIn incretin trials: NOT measured')

box(1, 4, 30, 24, '4  Clinical/behavioural', 'Weight-promoting background drugs\n(UKPDS: insulin +4.0 kg, SU +1.7-2.6)\nHypoglycaemia-related eating (hyp.)\nAdherence/motivation (lifestyle:\nT2D lost less than spouses)\nAge, sex composition')
box(35, 4, 30, 24, 'Net energy balance', 'Drug-arm-specific offsets:\nretained glucose energy + lower REE\nScenario estimate: ~1-6 kg by\nweek 68-72 (assumption-driven)\nvs observed gap ~6 kg (STEP 1 vs 2)')
box(69, 4, 30, 24, '5  Methodological', 'Separate trials, populations\nnot randomised by T2D status\nNo cross-programme IPD with\nadjustment for age, sex, BMI,\nbackground therapy')

arrow((23, 85), (29.4, 85), 'established')
arrow((70.6, 85), (75.4, 85), 'established')
arrow((12, 73.4), (12, 66.6), 'human')
arrow((18, 73.4), (44, 67.2), 'human')
arrow((21, 73.4), (78, 67.2), 'established')
arrow((40, 73.4), (20, 67.2), 'established')
arrow((16, 37.4), (40, 28.6), 'established', rad=0.1)
arrow((50, 37.4), (50, 28.6), 'hypothesis')
arrow((84, 37.4), (60, 28.6), 'hypothesis', rad=-0.1)
arrow((31.6, 16), (34.4, 16), 'human')
arrow((68.4, 16), (65.6, 16), 'hypothesis')

ax.legend(handles=[Line2D([], [], color=INK2, label='Established causal link (human)', **STY['established']),
                   Line2D([], [], color=INK2, label='Supported by human data; diabetes-specific role unproven', **STY['human']),
                   Line2D([], [], color=INK2, label='Inference / hypothesis (not measured in incretin trials)', **STY['hypothesis'])],
          loc='upper center', bbox_to_anchor=(0.5, 0.005), ncol=3, frameon=False, fontsize=8)
ax.set_title('From type 2 diabetes pathophysiology to attenuated weight loss: an evidence-graded model', fontsize=11, color=INK, loc='left')
fig.tight_layout()
for ext in ('png', 'svg'):
    fig.savefig(os.path.join(HERE, f'figure2_integrative_model.{ext}'), dpi=220)
print('figures written')
