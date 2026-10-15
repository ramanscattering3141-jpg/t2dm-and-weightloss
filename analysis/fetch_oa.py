"""Try every Unpaywall OA location for each DOI; save first genuine PDF.
Usage: UNPAYWALL_EMAIL=you@domain python3 -I fetch_oa.py OUTDIR"""
import json, subprocess, sys, os, urllib.parse
out = sys.argv[1]
dois = {'STEP1':'10.1056/NEJMoa2032183','STEP2':'10.1016/S0140-6736(21)00213-0','SURMOUNT1':'10.1056/NEJMoa2206038',
 'SURMOUNT2':'10.1016/S0140-6736(23)01200-X','SCALE_OB':'10.1056/NEJMoa1411892','SCALE_DM':'10.1001/jama.2015.9676',
 'STRATHE2023':'10.1111/dom.15211','STEPHFpEF':'10.1056/NEJMoa2306963','STEPHFpEF_DM':'10.1056/NEJMoa2313917',
 'OASIS1':'10.1016/S0140-6736(23)01185-6','RETA_OB':'10.1056/NEJMoa2301972','RETA_DM':'10.1016/S0140-6736(23)01053-X',
 'SURPASS2':'10.1056/NEJMoa2107519','PIONEERPLUS':'10.1016/S0140-6736(23)01127-3','WING1987':'10.2337/diacare.10.5.563',
 'BOGARDUS1986':'10.2337/diab.35.1.1','MAKIMATTILA1999':'10.1007/s001250051172','RAVE2006':'10.1093/ndt/gfl175',
 'HEISE2022':'10.1016/S2213-8587(22)00085-7','RAVUSSIN2025':'10.1016/j.cmet.2025.03.011'}
def curl(url, dest=None):
    args = ['curl','-sS','-L','-m','60','-A','Mozilla/5.0','-o',dest or '/dev/null','-w','%{http_code}',url]
    r = subprocess.run(args, capture_output=True, text=True); return r.stdout.strip()
for key, doi in dois.items():
    j = json.loads(subprocess.run(['curl','-sS','-m','20',f'https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={os.environ.get("UNPAYWALL_EMAIL", "you@example.com")}'],capture_output=True,text=True).stdout or '{}')
    locs = j.get('oa_locations') or []
    got = None
    for L in locs:
        for url in [L.get('url_for_pdf'), L.get('url')]:
            if not url: continue
            dest = os.path.join(out, f'{key}.pdf')
            code = curl(url, dest)
            if code == '200' and os.path.exists(dest) and open(dest,'rb').read(5) == b'%PDF-':
                got = url; break
            if os.path.exists(dest): os.remove(dest)
        if got: break
    print(f"{key:16} OA={j.get('is_oa')} locations={len(locs)} -> {'SAVED from '+got if got else 'no downloadable PDF'}")
