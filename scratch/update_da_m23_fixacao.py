import json

path = 'content/material/direito-administrativo/m23/fixacao.json'
with open(path, encoding='utf-8') as f:
    d = json.load(f)

d['status'] = 'PRONTO_PARA_REVISAO'

# 1. Update _316 (Q1)
for q in d['questoes']:
    if q['id'] == 'mentoria_mcn_direito-administrativo_316_f470ca':
        q['comentario'] = (
            "O princípio da independência das instâncias consagra que as esferas civil, penal e administrativa operam "
            "de modo autônomo. Todavia, esse postulado sofre mitigação expressa no art. 21, § 3º, da Lei nº 8.429/1992, "
            "o qual preceitua que as sentenças penais produzirão efeitos na ação de improbidade quando concluírem pela "
            "inexistência da conduta ou pela negativa da autoria. Nessas hipóteses taxativas, a decisão penal absolutória "
            "vincula a esfera cível, obstando a responsabilização por ato de improbidade com base no mesmo contexto histórico. "
            "Por outro lado, o STF declarou inconstitucional o art. 21, § 4º, nas ADIs 7156 e 7236, afastando a vinculação "
            "por absolvição fundada em falta de provas."
        )

    # 2. Update _320 (Q3)
    if q['id'] == 'mentoria_mcn_direito-administrativo_320_dcd469':
        q['comentario'] = (
            "O microssistema de tutela da probidade administrativa estabeleceu regras expressas de compensação e dedução "
            "no art. 12, § 6º, e no art. 21, § 5º, da Lei nº 8.429/1992 para coibir o bis in idem e o enriquecimento injustificado "
            "do erário. Nos termos do art. 12, § 6º, se ocorrer lesão ao patrimônio público, a reparação do dano a que se refere a LIA "
            "deverá deduzir o ressarcimento ocorrido nas instâncias criminal, civil e administrativa que tiver por objeto os mesmos fatos. "
            "Ademais, conforme o art. 21, § 5º, as sanções eventualmente aplicadas em outras esferas deverão ser compensadas com as sanções da LIA."
        )

    # 3. Update _326 (Q9)
    if q['id'] == 'mentoria_mcn_direito-administrativo_326_41c540':
        q['comentario'] = (
            "O regramento da tutela de indisponibilidade de bens na ação de improbidade foi disciplinado pelo art. 16 da Lei nº 8.429/1992. "
            "O art. 16, § 3º, previu a demonstração no caso concreto de perigo de dano ou risco ao resultado útil do processo. "
            "Ao apreciar as ADIs 7156 e 7236, o Supremo Tribunal Federal conferiu interpretação conforme à Constituição ao dispositivo, "
            "admitindo a concessão de tutela de evidência e a presunção do perigo da demora em situações excepcionais de comprovada gravidade, "
            "além de assentar que a constrição pode alcançar tanto o ressarcimento do dano quanto o enriquecimento ilícito."
        )

# 4. Replace _332 with _333
new_q14 = {
    "id": "mentoria_mcn_direito-administrativo_333_97c3dc",
    "capitulo": "direito-administrativo/a24/s09",
    "gabarito": "A",
    "comentario": (
        "O art. 23, § 4º, da Lei nº 8.429/1992 positivou um rol taxativo de cinco marcos interruptivos da prescrição da pretensão sancionatória: "
        "(I) ajuizamento da ação de improbidade; (II) publicação da sentença condenatória; (III) publicação de decisão ou acórdão de Tribunal de Justiça "
        "ou Tribunal Regional Federal que confirma sentença condenatória ou reforma sentença de improcedência; (IV) publicação de decisão ou acórdão "
        "do Superior Tribunal de Justiça que confirma acórdão condenatório ou reforma acórdão de improcedência; e (V) publicação de decisão ou acórdão "
        "do Supremo Tribunal Federal que confirma acórdão condenatório ou reforma acórdão de improcedência. Pronunciamentos de improcedência não interrompem "
        "a prescrição. Além disso, no julgamento das ADIs 7156 e 7236, o STF declarou inconstitucional a expressão 'pela metade' do § 5º, de modo que "
        "o prazo recomeça por 8 anos após a interrupção, observado o teto total de 20 anos."
    ),
    "alternativas": {
        "A": "Correta, pois reproduz hipóteses taxativas de marcos interruptivos positivados no art. 23, § 4º, incisos I, II e III, da Lei nº 8.429/1992.",
        "B": "Incorreta, pois meros requerimentos administrativos ou certidões não constituem marco interruptivo legal.",
        "C": "Incorreta, pois despachos ordinatórios e designação de audiência não interrompem a prescrição da LIA.",
        "D": "Incorreta, pois os marcos interruptivos são estritamente taxativos na lei, não se admitindo interrupção por juntada de petições.",
        "E": "Incorreta, pois remessas ao arquivo provisório não constam do rol de marcos interruptivos do art. 23, § 4º."
    }
}

for i, q in enumerate(d['questoes']):
    if q['id'] == 'mentoria_mcn_direito-administrativo_332_aa71ce':
        d['questoes'][i] = new_q14
        break

with open(path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=1)
print('fixacao.json updated successfully!')
