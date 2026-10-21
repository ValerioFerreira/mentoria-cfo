import sys,subprocess,re
sys.stdout.reconfigure(encoding='utf-8')
for tid in sys.argv[1:]:
    out=subprocess.run([sys.executable,'-I','pipeline/summary_source.py',tid],capture_output=True,env={'PYTHONIOENCODING':'utf-8','PATH':__import__('os').environ['PATH'],'SYSTEMROOT':__import__('os').environ.get('SYSTEMROOT','')},cwd='.').stdout.decode('utf-8','replace')
    head=out.split('\n')[0]
    print('#####',head)
    txt=re.sub(r'\n(?=[a-e]\) )',' ¶ ',out)
    items=re.split(r'\n(?=\([A-Za-zÀ-ú ]+/)',out)
    for it in items[1:]:
        it=re.sub(r'\s+',' ',it)
        it=re.sub(r'Equipe Exatas.*?Raciocínio Lógico','',it)
        print('-',it[:230])
