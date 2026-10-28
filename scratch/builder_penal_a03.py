# -*- coding: utf-8 -*-
"""Builder for direito-penal a03 (items and summaries)."""
import json
import os

ITEMS_FILE = "content/items/direito-penal/a03.json"
SUMMARIES_FILE = "content/summaries/direito-penal/a03.json"

os.makedirs(os.path.dirname(ITEMS_FILE), exist_ok=True)
os.makedirs(os.path.dirname(SUMMARIES_FILE), exist_ok=True)

with open("content/segments/direito-penal.json", "r", encoding="utf-8") as f:
    all_segs = {s["id"]: s for s in json.load(f)["segments"]}

def get_fp(sid):
    s = all_segs[sid]
    return {"startPage": s["startPage"], "endPage": s["endPage"], "startTopic": s["startTopic"]}

# ---------------------------------------------------------
# BIZU ITEMS (a03)
# ---------------------------------------------------------
items_data = {
    "aula": "direito-penal/a03",
    "batch": "pcpe-bizu-direito-penal",
    "status": "DRAFT",
    "stage": "bizu",
    "segments": [
        {
            "id": "direito-penal/a03/s01",
            "bizu": {
                "summary": [
                    "**Conceito de Culpabilidade**: juízo normativo de censura e reprovação pessoal que recai sobre o autor de um fato típico e antijurídico.",
                    "**Teoria Normativa Pura**: capitaneada por Welzel, estruturou a culpabilidade exclusivamente com elementos normativos: imputabilidade, potencial consciência da ilicitude e exigibilidade de conduta diversa.",
                    "**Imputabilidade Penal**: aptidão biopsicológica do indivíduo para discernir a antijuridicidade material da ação e conduzir sua volição segundo tal valoração ao tempo da conduta.",
                    "**Inimputabilidade por Anomalia Psíquica (art. 26)**: isenta de sanção criminal quem, por enfermidade mental ou desenvolvimento mental incompleto ou retardado, era inteiramente incapaz de compreender a ilicitude do ato.",
                    "**Semi-Imputabilidade (art. 26, parágrafo único)**: o indivíduo que não possuía a plena capacidade de autodeterminação responde pelo crime, com direito à redução compulsória de pena de um a dois terços ou substituição por tratamento curativo.",
                    "**Inimputabilidade Etária (art. 27)**: menores de dezoito anos são penalmente inimputáveis, submetendo-se exclusivamente às normas do Estatuto da Criança e do Adolescente.",
                    "**Teoria da Actio Libera In Causa**: o consumo deliberado ou desatento de álcool e narcóticos não elide a responsabilidade penal, retroagindo a verificação da voluntariedade ao momento do gole originário.",
                    "**Embriaguez Fortuita Completa (art. 28, § 1º)**: decorrente de caso fortuito ou força maior que retire completamente a capacidade de discernimento isenta o agente de pena.",
                    "**Emoção e Paixão (art. 28, I)**: estados emocionais agudos ou paixões sentimentais intensas não excluem a imputabilidade penal do autor.",
                    "**Potencial Consciência da Ilicitude**: possibilidade de o cidadão comum alcançar a compreensão da antijuridicidade de seu comportamento na vida comunitária.",
                    "**Exigibilidade de Conduta Diversa**: expectativa social de que o indivíduo atue segundo os mandamentos do direito quando colocado perante alternativas de conduta.",
                    "**Causas Legais de Inexigibilidade (art. 22)**: coação moral irresistível (responde pelo crime o coator originário) e submissão estrita a comando não abertamente ilegítimo de autoridade hierárquica superior."
                ],
                "teoria": [
                    {
                        "statement": "A constatação de semi-imputabilidade do agente autoriza o magistrado a extinguir a punibilidade da conduta praticada por ausência de dolo.",
                        "isTrue": False,
                        "explanation": "A semi-imputabilidade conserva o crime e a responsabilidade penal, autorizando a redução obrigatória de um a dois terços da reprimenda ou medida curativa."
                    },
                    {
                        "statement": "Pela teoria da actio libera in causa, o agente que se embriaga culposamente para festejar responde normalmente pelos crimes que vier a cometer.",
                        "isTrue": True,
                        "explanation": "O art. 28, II, do CP consagra que a embriaguez não acidental não exclui a imputabilidade, transferindo a análise da voluntariedade ao momento do consumo."
                    },
                    {
                        "statement": "A coação moral irresistível exclui a tipicidade formal do delito praticado pelo indivíduo ameaçado fisicamente.",
                        "isTrue": False,
                        "explanation": "A coação moral irresistível afasta a culpabilidade por inexigibilidade de conduta diversa, preservando o fato típico e ilícito."
                    },
                    {
                        "statement": "Na hipótese de cumprimento de ordem não manifestamente ilegal de superior hierárquico, a sanção penal recai sobre o superior que emitiu o mandamento.",
                        "isTrue": True,
                        "explanation": "O art. 22 do Código Penal comina responsabilidade criminal ao superior hierárquico prolator da ordem não manifestamente ilegal."
                    }
                ],
                "revisao": [
                    {
                        "statement": "A perturbação emocional intensa decorrente de término de relacionamento afetivo exclui a imputabilidade penal do agressor.",
                        "isTrue": False,
                        "explanation": "O art. 28, inciso I, do Código Penal estatui que a emoção ou a paixão não excluem a imputabilidade penal."
                    },
                    {
                        "statement": "O sistema biopsicológico adotado pelo Código Penal exige a conjugação de causa mental patológica com a incapacidade concreta de entendimento na data do fato.",
                        "isTrue": True,
                        "explanation": "O art. 26 acolheu o critério biopsicológico, exigindo transtorno mental associado à perda efetiva da capacidade de compreensão no momento delitivo."
                    },
                    {
                        "statement": "A teoria psicológica da culpabilidade situava o dolo e a culpa como elementos normativos desprovidos de liame subjetivo com a conduta.",
                        "isTrue": False,
                        "explanation": "Na teoria psicológica de Liszt e Beling, o dolo e a culpa constituíam as espécies puramente psicológicas que integravam a culpabilidade."
                    },
                    {
                        "statement": "A embriaguez involuntária incompleta proveniente de caso fortuito opera no direito penal como causa obrigatória de diminuição da reprimenda.",
                        "isTrue": True,
                        "explanation": "Conforme o art. 28, § 2º, a embriaguez incompleta decorrente de força maior ou caso fortuito autoriza redução de um a dois terços da pena."
                    }
                ],
                "pointers": [
                    {"topic": "Evolução dogmática da culpabilidade e teoria normativa pura", "pageRef": 3},
                    {"topic": "Imputabilidade penal e critério biopsicológico no artigo 26", "pageRef": 6},
                    {"topic": "Embriaguez involuntária e teoria da actio libera in causa", "pageRef": 9},
                    {"topic": "Exigibilidade de conduta diversa e excludentes do artigo 22", "pageRef": 13}
                ]
            }
        },
        {
            "id": "direito-penal/a03/s02",
            "bizu": {
                "summary": [
                    "**Erro de Tipo Essencial (art. 20, caput)**: recai sobre dados elementares constitutivos da figura típica; quando invencível extirpa dolo e culpa; quando vencível afasta o dolo e autoriza a punição culposa se prevista.",
                    "**Descriminantes Putativas por Erro de Fato (art. 20, § 1º)**: o agente imagina situação fática que justificaria a ação; se escusável isenta de pena; se inescusável pune por culpa imprópria.",
                    "**Erro Provocado por Terceiro (art. 20, § 2º)**: responde pela infração o terceiro causador intencional ou culposo da ilusão, respondendo o executor nos limites de seu próprio elemento anímico.",
                    "**Erro sobre o Objeto (*Error in Objecto*)**: erro meramente acidental que não exclui o dolo nem afasta a punição do delito contra a coisa efetivamente lesada.",
                    "**Erro sobre a Pessoa (*Error in Persona* - art. 20, § 3º)**: confunde a identidade da vítima; responde penalmente considerando as qualidades pessoais da vítima virtual visada e não as da pessoa real atingida.",
                    "**Erro na Execução (*Aberratio Ictus* - art. 73)**: desvio na execução mecânica por acidente atinge pessoa diversa; resultado único aplica as qualidades da pretendida; resultado duplo gera concurso formal.",
                    "**Resultado Diverso do Pretendido (*Aberratio Delicti* - art. 74)**: por erro na execução atinge bem jurídico de espécie diferente do pretendido; responde pelo resultado produzido a título de culpa se tipificado.",
                    "**Aberratio Causae e Dolo Geral**: desvio no curso causal do resultado; no dolo geral (*dolus generalis*) o autor supõe consumado o delito e pratica novo ato que causa a morte, respondendo por homicídio doloso consumado.",
                    "**Erro de Proibição Direto (art. 21)**: recai sobre a ilicitude do comportamento; quando inevitável isenta de pena; quando evitável atenua a sanção de um sexto a um terço.",
                    "**Erro de Proibição Indireto ou de Permissão**: o autor sabe que a conduta é abstratamente proibida, mas crê equivocadamente existir norma permissiva que justifique seu ato no ordenamento.",
                    "**Distinção entre Erro de Tipo e de Proibição**: no erro de tipo o indivíduo não sabe o que faz faticamente; no erro de proibição o indivíduo sabe o que faz mas desconhece a proibição normativa.",
                    "**Delito Putativo por Erro de Proibição**: o agente supõe erroneamente estar praticando um crime quando a conduta é juridicamente indiferente para o direito penal, configurando fato atípico."
                ],
                "teoria": [
                    {
                        "statement": "No erro sobre a pessoa, o Código Penal determina que a culpabilidade seja valorada segundo as condições particulares da vítima real concretamente alvejada.",
                        "isTrue": False,
                        "explanation": "O art. 20, § 3º, estipula expressamente que não se consideram as condições da vítima atingida, mas sim as da pessoa contra quem o autor pretendia praticar o crime."
                    },
                    {
                        "statement": "O erro de tipo essencial evitável mantém a punição dolosa do agente caso a modalidade culposa não esteja positivada no ordenamento.",
                        "isTrue": False,
                        "explanation": "O erro de tipo sempre exclui o dolo; a evitabilidade apenas autoriza punir por culpa se houver tipificação culposa na legislação."
                    },
                    {
                        "statement": "Na hipótese de aberratio ictus de resultado duplo, o agente responderá pelos delitos concorrentes sob as regras do concurso formal de crimes.",
                        "isTrue": True,
                        "explanation": "Conforme o art. 73, na ocorrência de duplo resultado lesivo, aplicam-se as balizas do concurso formal de infrações."
                    },
                    {
                        "statement": "O erro de proibição inescusável extingue a ilicitude da conduta praticada diante da ausência de má-fé do agente infrator.",
                        "isTrue": False,
                        "explanation": "O erro de proibição inescusável (evitável) conserva a reprovabilidade do fato, operando unicamente como causa de diminuição da pena de um sexto a um terço."
                    }
                ],
                "revisao": [
                    {
                        "statement": "A ocorrência de erro provocado dolosamente por terceiro transfere a autoria penal do delito ao sujeito causador da falsa representação da realidade.",
                        "isTrue": True,
                        "explanation": "O art. 20, § 2º, comina ao terceiro que determinou o engano a responsabilidade pelo crime praticado em autoria mediata."
                    },
                    {
                        "statement": "No erro sobre o nexo causal caracterizado por dolo geral, o agente responde por tentativa de homicídio em concurso material com homicídio culposo.",
                        "isTrue": False,
                        "explanation": "No dolus generalis considera-se a conduta como um contexto fático unitário, respondendo o infrator por crime doloso único consumado."
                    },
                    {
                        "statement": "O erro de tipo permissivo que recai sobre pressuposto fático de uma excludente de ilicitude configura modalidade de descriminante putativa.",
                        "isTrue": True,
                        "explanation": "A suposição fática equivocada que ampararia causa justificante enquadra-se nas descriminantes putativas do art. 20, § 1º."
                    },
                    {
                        "statement": "O erro de proibição inevitável atua no direito penal excluindo a tipicidade formal do comportamento humano investigado.",
                        "isTrue": False,
                        "explanation": "O erro de proibição inevitável afasta a potencial consciência da ilicitude, operando como causa exculpante de isenção de pena na culpabilidade."
                    }
                ],
                "pointers": [
                    {"topic": "Erro de tipo essencial evitável e inevitável no artigo 20", "pageRef": 18},
                    {"topic": "Descriminantes putativas e culpa imprópria", "pageRef": 21},
                    {"topic": "Erros acidentais: error in persona, aberratio ictus e aberratio delicti", "pageRef": 25},
                    {"topic": "Erro de proibição direto e indireto no artigo 21", "pageRef": 29}
                ]
            }
        }
    ]
}

# ---------------------------------------------------------
# SUMMARIES (a03)
# ---------------------------------------------------------
summaries_data = {
    "aula": "direito-penal/a03",
    "batch": "pcpe-summary-direito-penal",
    "status": "DRAFT",
    "segments": [
        {
            "id": "direito-penal/a03/s01",
            "fingerprint": get_fp("direito-penal/a03/s01"),
            "analytic": """Este segmento aborda a culpabilidade como terceiro substrato analítico do crime, analisando sua evolução teórica até a consolidação da Teoria Normativa Pura, seus três elementos estruturantes (imputabilidade, potencial consciência da ilicitude e exigibilidade de conduta diversa) e as causas exculpantes legalmente reconhecidas.

### Evolução dogmática da culpabilidade e Teoria Normativa Pura
A concepção da culpabilidade experimentou transformações teóricas determinantes na dogmática criminal:
- **Teoria Psicológica da Culpabilidade (von Liszt e Beling)**: alocava na culpabilidade o vínculo puramente psicológico entre o autor e o evento danoso. O dolo e a culpa eram tratados como as duas espécies psicológicas da culpabilidade, ao lado da imputabilidade como pressuposto biológico.
- **Teoria Psicológico-Normativa (Reinhard Frank)**: agregou o elemento normativo da *exigibilidade de conduta diversa*, concebendo a culpabilidade como um juízo de censura axiológica e não mero nexo psíquico.
- **Teoria Normativa Pura (Hans Welzel)**: com a criação do finalismo, o dolo e a culpa foram deslocados para o fato típico (integrando a conduta volitiva). A culpabilidade despojou-se de dados psicológicos, passando a constituir juízo estritamente normativo de reprovabilidade composto por três elementos: **imputabilidade penal, potencial consciência da ilicitude e exigibilidade de conduta diversa**.

### Imputabilidade penal e suas causas de exclusão
A imputabilidade consubstancia a maturidade e higidez psíquica que conferem ao sujeito capacidade de entender o caráter antijurídico de suas ações e governar seus atos segundo esse entendimento. O Código Penal adotou primordialmente o **critério biopsicológico** (salvo para a menoridade, que adota critério puramente biológico):

| Causa de Inimputabilidade | Critério Adotado | Consequência Jurídica no Processo |
| --- | --- | --- |
| **Menoridade Penal (art. 27)** | Critério Biológico puro | Inimputabilidade absoluta; aplicação do Estatuto da Criança e Adolescente |
| **Anomalia Mental Completa (art. 26)** | Critério Biopsicológico | Isenção de pena com imposição de medida de segurança (*absolvição imprópria*) |
| **Semi-Imputabilidade (art. 26, parágrafo único)** | Critério Biopsicológico | Diminuição obrigatória de 1 a 2 terços da pena ou substituição por tratamento |
| **Embriaguez Fortuita Completa (art. 28, § 1º)** | Força maior ou caso fortuito | Isenção integral de pena privativa de liberdade |

A semi-imputabilidade caracteriza-se quando o agente não era inteiramente incapaz de compreender o caráter ilícito do fato em virtude de perturbação de saúde mental ou desenvolvimento incompleto, cabendo ao magistrado aplicar a causa de diminuição na terceira fase da dosimetria ou converter a reprimenda em medida de segurança curativa se demonstrada periculosidade real.

Quanto à ingestão alcoólica ou substâncias de efeitos análogos, vigora no direito brasileiro a **Teoria da Actio Libera In Causa**: a embriaguez voluntária (desejada) ou culposa (imprudente) não afasta a imputabilidade penal, transferindo-se a análise da voluntariedade para o instante precedente do consumo. Somente a embriaguez acidental completa (proveniente de caso fortuito ou força maior) isenta o autor de pena. Ademais, o artigo 28, inciso I, estipula que a emoção ou a paixão não excluem a imputabilidade.

### Potencial consciência da ilicitude e exigibilidade de conduta diversa
- **Potencial Consciência da Ilicitude**: diz respeito à aptidão de o indivíduo comum vislumbrar a ilicitude material do comportamento adotado na vida comunitária. Não se exige conhecimento técnico-jurídico de leis, bastando o senso ético comum. A sua ausência invencível configura o **erro de proibição inevitável** (artigo 21 do CP), que opera a isenção de pena.
- **Exigibilidade de Conduta Diversa**: consiste na possibilidade real e fática de exigir que o indivíduo aja em conformidade com o mandamento do direito no momento crítico do acontecimento. A sua inexistência afasta a reprovação social.

O Código Penal positivou no artigo 22 duas hipóteses legais expressas de inexigibilidade de conduta diversa:
1. **Coação Moral Irresistível (*Vis Compulsiva*)**: o agente comete o fato sob grave ameaça física ou psicológica insuperável perpetrada por terceiro contra si ou pessoa próxima. O coagido é isento de sanção por inexigibilidade de conduta, respondendo pelo ilícito o autor originário da coação (*autor mediato*);
2. **Estrita Obediência a Ordem Não Manifestamente Ilegal**: aplica-se estritamente às relações hierárquicas de direito público administrativo. O subordinado que cumpre comando de superior aparentemente legítimo é isento de pena, respondendo pelo crime unicamente o superior que emitiu o mandamento viciado. Se a ilegalidade for manifesta e evidente (como torturar um preso), ambos respondem em concurso de pessoas.

### Para fixar
- A culpabilidade estrutura-se no trinômio imputabilidade, consciência da ilicitude e exigibilidade de conduta.
- O Código Penal acolheu a Teoria Normativa Pura da culpabilidade no bojo da reforma penal de 1984.
- A imputabilidade adota o critério biopsicológico para saúde mental e biológico para a menoridade.
- A semi-imputabilidade impõe redução de um a dois terços ou substituição por medida de segurança.
- A teoria da actio libera in causa impede a exculpação pela embriaguez voluntária ou culposa ordinária.
- A embriaguez involuntária e completa por caso fortuito gera isenção absoluta de reprimenda corporal.
- O erro de proibição inevitável exclui a potencial consciência da ilicitude e isenta o indivíduo de sanção.
- A coação moral irresistível e a ordem hierárquica não manifestamente ilegal afastam a exigibilidade de conduta.""",
            "synthetic": [
                "**Teoria Normativa Pura**: consolida a culpabilidade como juízo estrito de reprovação composto por imputabilidade, potencial consciência e exigibilidade de conduta.",
                "**Critério Biopsicológico**: exige diagnóstico de perturbação mental aliado à privação concreta da aptidão de compreensão ou autodeterminação na conduta.",
                "**Semi-Imputabilidade (art. 26, p. único)**: reduz compulsoriamente a pena de um a dois terços ou autoriza medida de segurança conforme a periculosidade.",
                "**Actio Libera In Causa**: a ingestão culposa ou intencional de álcool não afasta a imputabilidade, aferindo-se a vontade no instante da ingestão.",
                "**Embriaguez Fortuita**: isenta de reprimenda corporal apenas quando for completa e derivada impreterivelmente de caso fortuito ou coação física.",
                "**Potencial Consciência da Ilicitude**: conhecimento ético leigo ao alcance do cidadão, cuja ausência insuperável caracteriza erro de proibição dirimente.",
                "**Coação Moral Irresistível**: preserva o fato típico e ilícito, isentando o coagido por inexigibilidade de conduta e cominando a pena ao coator.",
                "**Obediência Hierárquica**: isenta o funcionário que executa ordem funcional de superior desprovida de ilegalidade manifesta aos olhos comuns."
            ]
        },
        {
            "id": "direito-penal/a03/s02",
            "fingerprint": get_fp("direito-penal/a03/s02"),
            "analytic": """Este segmento aprofunda a Teoria Geral do Erro no Direito Penal, examinando a dicotomia entre erro de tipo e erro de proibição, as descriminantes putativas, o erro provocado por terceiro, os erros acidentais na execução e as espécies de aberrações delitivas.

### Erro de tipo essencial e descriminantes putativas
O erro de tipo essencial recai sobre os dados fáticos constitutivos da figura delitiva (*o caçador dispara contra vulto na mata supondo tratar-se de animal selvagem, alvejando outro homem*). Conforme o artigo 20, caput, do Código Penal:
- **Erro Inevitável (Escusável ou Invencível)**: o agente emprega todas as cautelas exigíveis do homem médio, mas incide no equívoco fático. **Exclui o dolo e a culpa**, operando a atipicidade penal absoluta do comportamento;
- **Erro Evitável (Inescusável ou Vencível)**: o agente peca por desatenção ou imprudência que qualquer pessoa prudente evitaria. **Exclui o dolo, mas permite a punição por culpa**, desde que a modalidade culposa esteja expressamente tipificada no diploma legal.

O artigo 20, § 1º, cuida das **Descriminantes Putativas por Erro de Tipo Permissivo**: situações em que o agente atua imaginando um contexto empírico de perigo que, caso existisse no plano real, autorizaria legítima defesa ou estado de necessidade (*o sujeito supõe falsamente que o desafeto puxa uma arma ao enfiar a mão no bolso para pegar a carteira*).

O Código Penal adotou a **Teoria Limitada da Culpabilidade**: o erro sobre a situação fática de uma causa de justificação recebe o mesmo tratamento do erro de tipo. Se o erro for inevitável, isenta de pena; se for evitável, o sujeito responde pela infração a título de **culpa imprópria** (conduta voluntariamente dolosa punida como culposa por política penal).

O artigo 20, § 2º, disciplina o erro provocado por terceiro: se um terceiro induz deliberadamente o executor a cometer o engano fático, aquele responde pelo crime doloso na condição de autor mediato.

### Erros acidentais: objeto, pessoa e causalidade
Os erros acidentais recaem sobre aspectos secundários do iter criminis sem macular a representação típica do delito, não afastando o dolo nem isentando de pena:
- **Erro sobre o Objeto (*Error in Objecto*)**: o indivíduo atinge materialmente uma coisa imaginando tratar-se de outra (*subtrai anel de bijuteria supondo ser joia de brilhantes*). Responde pelo furto considerando os dados reais do objeto efetivamente subtraído;
- **Erro sobre a Pessoa (*Error in Persona* - art. 20, § 3º)**: o infrator confunde a identidade visual do alvo e executa conduta contra outrem (*atira em estranho achando que é seu desafeto*). Por expressa ficção legal, **não se consideram as condições da vítima real, mas sim as da vítima virtual visada** (se o alvo visado era o genitor do autor, incide a agravante de crime contra ascendente, mesmo que a vítima real seja pessoa estranha);
- **Erro sobre o Nexo Causal (*Aberratio Causae*)**: o resultado pretendido efetiva-se através de trajetória causal diversa da inicialmente imaginada. No chamado **Dolo Geral (*Dolus Generalis*)**, o autor asfixia a vítima e, supondo que ela já está morta, atira seu corpo no mar para ocultar o cadáver, vindo ela a falecer por afogamento. A jurisprudência reconhece a unicidade do contexto causal fático, condenando o autor por crime único de homicídio doloso consumado.

### Desvios na execução: Aberratio Ictus e Aberratio Delicti
- **Erro na Execução (*Aberratio Ictus* - art. 73 do CP)**: o autor seleciona corretamente o alvo pretendido, porém, por inabilidade mecânica, ricochete ou desvio do projétil, atinge pessoa diversa:
  - *Resultado Único*: a punição é modulada com esteio nas condições particulares da vítima pretendida originalmente pelo atirador (aplicam-se as regras do *error in persona*);
  - *Resultado Duplo*: atinge a pessoa visada e terceira pessoa involuntária; responde pelas duas infrações em **concurso formal de crimes** (artigo 70 do CP).
- **Resultado Diverso do Pretendido (*Aberratio Delicti* - art. 74 do CP)**: o desvio executivo atinge bem jurídico de espécie distinta daquela almejada (*arremessa pedra para quebrar vitrine e fere o comerciante atrás do balcão*). Responde pelo resultado lesivo produzido a título culposo se previsto na norma; se sobrevém duplo resultado, incidem as balizas do concurso formal.

### Erro de proibição (art. 21 do CP)
O erro de proibição incide sobre a consciência da antijuridicidade da conduta. O indivíduo sabe exatamente o que faz no plano físico, mas acredita falsamente que seu comportamento é plenamente lícito perante a ordem jurídica:
- **Erro de Proibição Inevitável (Invencível)**: o agente não tinha como alcançar a compreensão da ilicitude material do ato em virtude de suas condições socioculturais. **Isenta o agente de pena**, afastando a potencial consciência da ilicitude;
- **Erro de Proibição Evitável (Vencível)**: o sujeito poderia atingir o discernimento com esforço normal de reflexão. O fato permanece reprovável, atuando o erro como **causa de diminuição da pena de um sexto a um terço**.

Distingue-se o erro de proibição direto (desconhecimento da norma proibitiva) do erro de proibição indireto (o sujeito conhece a proibição, mas crê equivocadamente existir causa excludente de ilicitude autorizadora no direito).

### Para fixar
- O erro de tipo essencial inevitável exclui o dolo e a culpa, afastando a tipicidade.
- O erro de tipo evitável afasta o dolo mas permite responsabilização a título culposo.
- O Código Penal adotou a Teoria Limitada da Culpabilidade nas descriminantes putativas.
- No erro sobre a pessoa, aplicam-se as qualidades pessoais da vítima virtual pretendida (art. 20, § 3º).
- A *aberratio ictus* decorre de desvio no uso dos meios de execução em direção a pessoa diversa.
- No duplo resultado na *aberratio ictus*, o autor responde em concurso formal de crimes.
- A *aberratio delicti* atinge bem jurídico de espécie distinta daquela que o autor planejava lesar.
- O erro de proibição recai sobre a ilicitude do fato, isentando de pena se inevitável (art. 21).""",
            "synthetic": [
                "**Erro de Tipo Essencial**: recai sobre elementares fáticas do tipo penal, eliminando o dolo sempre e afastando a culpa quando se mostrar invencível.",
                "**Teoria Limitada da Culpabilidade**: equipara o erro sobre circunstância fática de justificação ao erro de tipo, punindo a modalidade inescusável como culpa imprópria.",
                "**Error in Persona (art. 20, § 3º)**: confunde a identidade do alvo alvejado, computando-se as agravantes e condições pessoais da vítima visada pretendida.",
                "**Aberratio Ictus (art. 73)**: desvio mecânico de pontaria que atinge terceira pessoa acidental, considerando as qualidades da pretendida em resultado único.",
                "**Duplo Resultado**: na aberratio ictus com dois ofendidos lesionados, o agente responde pelas infrações mediante regras do concurso formal de delitos.",
                "**Aberratio Delicti (art. 74)**: atinge objeto jurídico de espécie diversa do planejado, imputando-se o evento produzido a título culposo se previsto.",
                "**Dolo Geral (Dolus Generalis)**: desvio na causalidade em que a vítima morre em ato posterior de desova, sancionando o agente por homicídio doloso consumado.",
                "**Erro de Proibição (art. 21)**: falsa percepção sobre a ilicitude jurídica do ato, gerando isenção de pena se invencível ou minoração fracionária se evitável."
            ]
        }
    ]
}

# Write files
with open(ITEMS_FILE, "w", encoding="utf-8") as f:
    json.dump(items_data, f, ensure_ascii=False, indent=2)
print(f"Wrote {ITEMS_FILE}")

with open(SUMMARIES_FILE, "w", encoding="utf-8") as f:
    json.dump(summaries_data, f, ensure_ascii=False, indent=2)
print(f"Wrote {SUMMARIES_FILE}")
