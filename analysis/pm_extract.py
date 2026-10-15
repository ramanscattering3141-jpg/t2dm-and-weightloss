"""Compact view of PubMed MCP get_article_metadata JSON dumps.
Usage: python3 -I pm_extract.py FILE [--full]   (prints pmid, doi, citation, title, abstract)
Also merges records into references/pubmed_records.json (keyed by PMID)."""
import json, sys, os
path = sys.argv[1]; full = '--full' in sys.argv
data = json.load(open(path))
if isinstance(data, list):  # some dumps wrap content blocks
    data = json.loads(data[0]['text'])
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references', 'pubmed_records.json')
db = json.load(open(db_path)) if os.path.exists(db_path) else {}
for a in data['articles']:
    pmid = a['identifiers']['pmid']
    au = [x for x in a.get('authors', []) if x.get('last_name')]
    cit = a.get('citation', {})
    rec = {'pmid': pmid, 'doi': a['identifiers'].get('doi', ''), 'title': a['title'],
           'journal': a['journal'].get('iso_abbreviation', ''), 'year': a['publication_date'].get('year', ''),
           'volume': cit.get('volume', ''), 'issue': cit.get('issue', ''), 'pages': cit.get('pages', ''),
           'authors': [f"{x['last_name']} {x.get('initials','')}".strip() for x in au],
           'types': a.get('article_types', []), 'abstract': a.get('abstract', '')}
    db[pmid] = rec
    print(f"=== {pmid} | {rec['doi']} | {', '.join(rec['authors'][:1])} {rec['year']} {rec['journal']} {rec['volume']}:{rec['pages']}")
    print(rec['title'])
    ab = rec['abstract']
    print(ab if full else ab[:2600])
    print()
json.dump(db, open(db_path, 'w'), indent=1, ensure_ascii=False)
