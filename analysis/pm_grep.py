"""Print sentences from abstracts in a PubMed JSON dump that match keywords.
Usage: python3 -I pm_grep.py FILE kw1,kw2,...  (case-insensitive)"""
import json, sys, re
data = json.load(open(sys.argv[1])); kws = [k.lower() for k in sys.argv[2].split(',')]
for a in data['articles']:
    pm = a['identifiers']['pmid']; ab = a.get('abstract', '')
    au = [x for x in a.get('authors', []) if x.get('last_name')]
    print(f"=== {pm} | {a['identifiers'].get('doi','')} | {au[0]['last_name'] if au else ''} {a['publication_date'].get('year','')} | {a['title'][:150]}")
    for s in re.split(r'(?<=[.;])\s+(?=[A-Z(])', ab):
        if any(k in s.lower() for k in kws):
            print('  -', s.strip()[:700])
