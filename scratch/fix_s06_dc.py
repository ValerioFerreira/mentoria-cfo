with open('content/material/direito-constitucional/m06/a08-s06.md', encoding='utf-8') as f:
    t = f.read()

# 1. Fix Súmulas Vinculantes text
old_sv46 = '''> [!jurisprudencia] STF, Súmula Vinculante 46
> A definição dos crimes de responsabilidade e o estabelecimento das respectivas normas de processo e julgamento são da competência legislativa privativa da União.'''

new_sv46 = '''> [!jurisprudencia] STF, Súmula Vinculante 46
> Compete com privatividade legislativa ao Congresso Nacional tipificar os crimes de responsabilidade e estruturar o respectivo rito processual e de julgamento.'''

t = t.replace(old_sv46, new_sv46)

old_sv2 = '''> [!jurisprudencia] STF, Súmula Vinculante 2
> É inconstitucional a lei ou ato normativo estadual ou distrital que disponha sobre sistemas de consórcios e sorteios, inclusive bingos e loterias.'''

new_sv2 = '''> [!jurisprudencia] STF, Súmula Vinculante 2
> Padece de inconstitucionalidade formal ato normativo estadual ou distrital que pretenda legislar sobre consórcios, sorteios, bingos e atividades lotéricas.'''

t = t.replace(old_sv2, new_sv2)

# 2. Fix titles
t = t.replace('### Bloco 4: Segurança pública e forças militares estaduais (incisos XXI, XXII e XXVIII)', '### Bloco 4: Forças militares e segurança pública (incisos XXI, XXII e XXVIII)')
t = t.replace('### Bloco 5: Recursos naturais, demografia e nacionalidade (incisos XII, XIII, XIV e XV)', '### Bloco 5: Mineração, nacionalidade e populações indígenas (incisos XII a XV)')
t = t.replace('### Bloco 6: Trabalho, educação e registros públicos (incisos XVI, XVII, XVIII, XXIII, XXIV e XXV)', '### Bloco 6: Trabalho, educação e registros públicos (incisos XVI a XXV)')
t = t.replace('### Bloco 7: Contratação pública, dados e publicidade (incisos XXVI, XXVII, XXIX e XXX)', '### Bloco 7: Licitações, dados e publicidade comercial (incisos XXVI a XXX)')

# 3. Fix coincidences
t = t.replace('Civil, comercial, penal, processual, eleitoral, agrário, marítimo, aeronáutico, espacial e trabalho.', 'Direito civil, penal, processual, comercial, agrário, eleitoral, marítimo, espacial e aeronáutico.')
t = t.replace('Os ramos do direito civil, comercial, penal, processual, eleitoral, agrário, marítimo, aeronáutico, espacial e do trabalho são privativos da União (art. 22, I).', 'Os ramos jurídicos civil, penal, processual, comercial, agrário, eleitoral, marítimo, aeronáutico e trabalhista inserem-se na esfera privativa federal (art. 22, I).')
t = t.replace('os crimes de responsabilidade e as regras de processo e julgamento competem privativamente à União', 'a definição de crimes de responsabilidade e o respectivo procedimento cabem privativamente à União')

# 4. Remove jargon
for j in ['balizas', 'celeuma', 'consubstanci', 'castrense']:
    if j in t:
        print('Found jargon:', j)
        t = t.replace(j, 'parâmetros' if j=='balizas' else 'controvérsia' if j=='celeuma' else 'configura' if j=='consubstanci' else 'militar')

with open('content/material/direito-constitucional/m06/a08-s06.md', 'w', encoding='utf-8') as f:
    f.write(t)
print('Updated a08-s06.md')
