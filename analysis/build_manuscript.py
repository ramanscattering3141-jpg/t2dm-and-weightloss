"""Assemble manuscript/sections/*.md -> manuscript/manuscript.md with numbered citations and a
bibliography generated from PubMed (NCBI E-utilities esummary). Run: python3 analysis/build_manuscript.py
Also writes references/references.json and references/bibliography.md."""
import glob, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYMAP = {
 'STEP1':'33567185','STEP2':'33667417','SCALE_OB':'26132939','SCALE_DM':'26284720','SURMOUNT1':'35658024',
 'SURMOUNT2':'37385275','STEPHFpEF':'37622681','STEPHFpEF_DM':'38587233','HFpEF_POOL':'38599221',
 'REDEFINE1':'40544433','REDEFINE2':'40544432','ATTAIN1':'40960239','ATTAIN2':'41275875','ACHIEVE1':'40544435',
 'OASIS1':'37385278','PIONEERPLUS':'37385279','SCALE_INSULIN':'32139381','RETA_OB':'37366315','RETA_DM':'37385280',
 'SURPASS1':'34186022','SURPASS2':'34170647','STEP6':'35131037','SUSTAINFORTE':'34293304','GHUSN2022':'36121652',
 'RODRIGUEZ2024':'38976257','WING1987':'3677974','UKPDS33':'9742976','PERREAULT2022':'35724304',
 'SURMOUNT1_3Y':'39536238','MARITIDE2025':'40549887','STRATHE2023':'37424165','CARLSSON2018':'29907893',
 'OVERGAARD2021':'34622228','BLUNDELL2017':'28266779','FRIEDRICHSEN2021':'33269530','FLINT1998':'9449682',
 'GUTZWILLER1999':'10233049','FLINT2013':'23551925','NAUCK1993':'8423228','HOJBERG2009':'19037628',
 'HEISE2022':'35468322','HEISE2023':'36857477','MAKIMATTILA1999':'10230643','CARLSON1993':'8243815',
 'FERRANNINI_G2015':'26180105','POLIDORI2016':'27804272','BOGARDUS1986':'3940908','VANBLOEMENDAAL2014':'25071023',
 'TENKULVE2015':'26283736','FARR2016':'26831302','HALAWI2017':'28958851','UMAPATHYSIVAM2014':'24089511',
 'NAUCK2011':'21430088','GABERY2020':'32213703','SECHER2014':'25202980','ADRIAENSSENS2019':'31447324',
 'ZHANG2021':'33571454','COSKUN2018':'30473097','KELLEY2000':'10905472','DEFRONZO1981':'7030826',
 'DRUCKER_HOLST2023':'36976349','DRUCKER2025':'40281304','XU2007':'17360984','VILSBOLL2002':'12189441',
 'NAUCK1986':'3514343','RAVE2006':'16627603','HALL2011':'21872751','MCCRIMMON2020':'31897524',
 'GASTALDELLI2022':'35468325','URVA2020':'32519795','HJERPSTED2018':'28941314','BERGMANN2019':'30683945',
 'BORNER2021':'34380697','ASMAR2010':'20547981','ARMSTRONG2016':'26394161','FRASER1990':'2076799',
 'WILLARD2020':'32730231','HALL2015':'26278052','KNOP2007':'17513701','BRIERLEY2021':'33589843',
 'KANOSKI2011':'21693680','KJEMS2003':'12540611','ROSENBAUM2022':'34848489','PETERSEN_SHULMAN2018':'30067154',
 'MARTIN2025':'40555748','RAVUSSIN2025':'40203836','LOOK2025':'39996356','GOLUBIC2024':'38562018',
 'VANEYK2019':'32127340','HARDER2004':'15277417','SILVER2023':'37188932','RAYNER2020':'32471908',
 'JONES2020':'31903712','PHILLIPS2014':'25047170','KILLION2018':'30567927','KULLMANN2016':'27489306',
 'CAMILLERI2018':'30385743',
 # Section 5 (peripheral incretin signalling): endogenous background, degradation, afferent transmission
 'HOLST2007':'17928588','BAGGIO2007':'17498508','DRUCKER2018':'29617641','HOLT2019':'30279161',
 'TOFTNIELSEN2001':'11502801','VILSBOLL2003':'12788877','CALANNA_GLP1':'23377698','CALANNA_GIP':'24065842',
 'ZHENG2015':'26318108','MALIN2013':'23872069','YAMASHITA2019':'31276666','WILLARD2017':'27933334',
 'KNAUF2008':'18519802','SOTY2017':'28591631','HAYES2011':'21849636','ZHANGRITTER2011':'22031786',
 'IWASAKI2018':'29317623','NISHIZAWA2000':'10742535','EDGERTON2013':'23673158','PLAMBOECK2013':'23599045',
 'BONORA2020':'32819978','AGASHE2018':'30788010','DUCHEN1980':'6243893','ROBERTSON1980':'6991317',
 'LEE2012':'22160540','MALBERT2021':'33067312','DUCA2013':'23423571','MCCREIGHT2016':'26780750',
 'OVERGAARD2021PK':'33969456','CHEDID2019':'30166634',
 # Section 2 (non-incretin generality, STEP UP pair, within-T2D HbA1c gradient) and Section 9 (Hall model inputs)
 'STEPUP':'40961952','STEPUP_T2D':'40961953','HALL2024':'38644683','GOUGEON2002':'12461671',
 'POLIDORI2013':'23585665','NATHAN2008':'18540046','SATTAR2025':'40838997','BAYS2023':'37990681',
 'ARODA2020':'31608552','HOLLANDER2013':'24144653','GREENWAY2010':'20673995','GADDE2011':'21481449',
 'ONEIL2012':'22421927','SMITH2010':'20647200','LESLIE2017':'27698345','HENRY1986':'3510922',
 'COURCOULAS2015':'25824474'}

# Sources with no PubMed record (preprints). Cited like any other key; formatted from these fields.
# Verified by direct retrieval of the posted full text; see references/verified_log.md.
MANUAL = {
 'HALL2026': {
   'doi': '10.64898/2026.09.08.750112',
   'citation': ('Hall KD. Why Do Patients with Type 2 Diabetes Lose Less Weight on GLP-1s? '
                'A Mathematical Modeling Analysis. bioRxiv. 2026:2026.09.08.750112. '
                'doi:10.64898/2026.09.08.750112. Preprint, not peer reviewed. '
                'Funded by AstraZeneca; the author is an employee of AstraZeneca Pharmaceuticals.'),
 },
}
DOI_FALLBACK = {'9742976': '10.1016/S0140-6736(98)07019-6'}  # derived from PII; PubMed record lacks DOI

text = '\n\n'.join(open(f).read().rstrip() for f in sorted(glob.glob(os.path.join(ROOT, 'manuscript', 'sections', '*.md'))))
order = []
for grp in re.findall(r'\[(@[^\]]+)\]', text):
    for k in re.findall(r'@([A-Za-z0-9_]+)', grp):
        if k not in KEYMAP and k not in MANUAL: sys.exit(f'Unknown citation key: {k}')
        if k not in order: order.append(k)
num = {k: i + 1 for i, k in enumerate(order)}

def fmt(grp):
    ns = sorted({num[k] for k in re.findall(r'@([A-Za-z0-9_]+)', grp)})
    out, i = [], 0
    while i < len(ns):
        j = i
        while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1: j += 1
        out.append(f'{ns[i]}–{ns[j]}' if j - i >= 2 else ','.join(map(str, ns[i:j + 1])))
        i = j + 1
    return '[' + ','.join(out) + ']'
body = re.sub(r'\[(@[^\]]+)\]', lambda m: fmt(m.group(1)), text)

# fetch metadata
pmids = [KEYMAP[k] for k in order if k in KEYMAP]
cache = os.path.join(ROOT, 'references', 'esummary_cache.json')
data = json.load(open(cache)) if os.path.exists(cache) else {}
missing = [p for p in pmids if p not in data]
import time
for i in range(0, len(missing), 50):
    ids = ','.join(missing[i:i + 50])
    for attempt in range(5):  # NCBI rate-limits bursts; retry with backoff
        r = subprocess.run(['curl', '-sS', '-m', '60', f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id={ids}'], capture_output=True, text=True)
        try:
            res = json.loads(r.stdout)['result']
            break
        except (ValueError, KeyError):
            if attempt == 4: sys.exit(f'esummary failed for {ids}: {r.stdout[:200]}')
            time.sleep(2 ** attempt)
    for p in res.get('uids', []): data[p] = res[p]
    time.sleep(0.5)
json.dump(data, open(cache, 'w'), indent=1)

def ref(p):
    d = data[p]
    au = [a['name'] for a in d.get('authors', []) if a.get('authtype') == 'Author']
    if not au and d.get('authors'): au = [d['authors'][0]['name']]
    a = ', '.join(au[:6]) + (', et al' if len(au) > 6 else '')
    doi = next((x['value'] for x in d.get('articleids', []) if x['idtype'] == 'doi'), DOI_FALLBACK.get(p, ''))
    year = d.get('pubdate', '')[:4]
    vol = d.get('volume', ''); iss = d.get('issue', ''); pg = d.get('pages', '')
    loc = f"{year};{vol}" + (f"({iss})" if iss else '') + (f":{pg}" if pg else '')
    title = d.get('title', '').rstrip('.')
    return f"{a}. {title}. {d.get('source', '')}. {loc}. doi:{doi}. PMID: {p}", doi

refs, bib = [], []
for k in order:
    if k in MANUAL:
        m = MANUAL[k]; s, doi, p = m['citation'], m['doi'], ''
    else:
        p = KEYMAP[k]; s, doi = ref(p)
    refs.append({'n': num[k], 'key': k, 'pmid': p, 'doi': doi, 'citation': s})
    bib.append(f"{num[k]}. {s}")
json.dump(refs, open(os.path.join(ROOT, 'references', 'references.json'), 'w'), indent=1, ensure_ascii=False)
open(os.path.join(ROOT, 'references', 'bibliography.md'), 'w').write('# References\n\n' + '\n'.join(bib) + '\n')
out = body + '\n\n## References\n\n' + '\n'.join(bib) + '\n'
open(os.path.join(ROOT, 'manuscript', 'manuscript.md'), 'w').write(out)
unused = sorted((set(KEYMAP) | set(MANUAL)) - set(order))
words = len(re.sub(r'\|.*\|', '', body.split('## Figure legends')[0].split('## 1. Introduction', 1)[-1]).split())
print(f'{len(order)} references cited; {len(unused)} verified sources not cited: {unused}')
print(f'Approximate main-text words (Introduction to Conclusions, excluding tables): {words}')
