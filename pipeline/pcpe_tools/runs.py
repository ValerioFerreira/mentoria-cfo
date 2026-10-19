import sys, json
sys.path.insert(0, 'pipeline')
import validate_summaries as v
f = sys.argv[1]
doc = json.load(open(f, encoding='utf-8'))
aula = doc['aula']
src = v.load_source_shingles(aula)
for s in doc['segments']:
    blob = s['analytic'] + '\n' + '\n'.join(s.get('synthetic', []))
    runs = [r for r in v.copied_runs(blob, src) if not v.is_trivial_run(r)]
    tot = sum(len(r) for r in runs)
    if runs and (tot >= 30 or any(len(r) >= 16 for r in runs)):
        print(s['id'], 'total', tot)
        for r in runs:
            print('   ', len(r), ' '.join(r))
