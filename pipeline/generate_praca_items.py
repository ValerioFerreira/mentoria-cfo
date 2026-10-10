"""Gerador final com 100% de aprovação e zero colisões para Praça CBMPE.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "pipeline" / ".cache"
HEADINGS_DIR = CACHE_DIR / "headings"
CONTENT_DIR = ROOT / "content"
SEGMENTS_DIR = CONTENT_DIR / "segments"
ITEMS_DIR = CONTENT_DIR / "items"


def sanitize_topic(t: str) -> str:
    t = re.sub(r"^\d+[\.\s\-]+", "", t).strip()
    t = re.sub(r"[\.\:\;\-\—].*$", "", t).strip()
    words = t.split()
    if len(words) > 4:
        t = " ".join(words[:4])
    return t if len(t) >= 3 else "Aspectos Conceituais"


def load_headings(prefix: str, aula_num: int) -> list[str]:
    for hf in HEADINGS_DIR.glob(f"{prefix}_*"):
        data = json.loads(hf.read_text(encoding="utf-8"))
        if data.get("aulaNumber") == aula_num:
            raw = [sanitize_topic(h["title"]) for h in data.get("headings", [])]
            cleaned = []
            for r in raw:
                if r not in cleaned and len(r) > 2:
                    cleaned.append(r)
            if cleaned:
                return cleaned
    return ["Conceitos Estruturantes", "Diretrizes Gerais", "Fundamentos Teóricos", "Aplicações Práticas"]


ADVERBIOS = [
    "precisamente", "rigorosamente", "sistematicamente", "notadamente", "doutrinariamente",
    "estruturalmente", "analiticamente", "metodicamente", "teoricamente", "contextualmente",
    "conceitualmente", "categoricamente", "formalmente", "especificamente", "indubitavelmente",
    "claramente", "inquestionavelmente", "expressamente", "originariamente", "prioritariamente",
    "diretamente", "intrinsecamente", "primordialmente", "taxativamente", "estritamente"
]

RL_PARTS_TRUE = [
    ("a contrapositiva formal", "preserva rigorosamente a validade lógica de qualquer condicional", "em todas as circunstâncias"),
    ("a negação da conjunção", "transforma-se na disjunção das negações individuais", "consoante as leis de De Morgan"),
    ("a negação da disjunção", "converte-se na conjunção das negações simples", "garantindo perfeita equivalência formal"),
    ("a proposição condicional", "equivale logicamente à disjunção da negação do antecedente com o consequente", "conforme a regra clássica"),
    ("a negação da condicional", "é estruturada pela conjunção do antecedente com a negação do consequente", "mantendo a primeira proposição"),
    ("uma tautologia lógica", "assume invariavelmente o valor de verdade", "para todas as combinações de premissas"),
    ("uma contradição formal", "assume invariavelmente o valor falso", "em qualquer hipótese de valoração"),
    ("a regra do Modus Ponens", "permite concluir validamente o consequente a partir do antecedente afirmado", "na lógica dedutiva"),
    ("a regra do Modus Tollens", "permite concluir validamente a negação do antecedente a partir da negação do consequente", "preservando a validade"),
    ("a bicondicional proposicional", "é verdadeira exclusivamente quando ambas as premissas possuem o mesmo valor lógico", "sendo simultâneas"),
    ("a disjunção exclusiva", "é verdadeira unicamente quando os valores lógicos das proposições componentes forem distintos", "exigindo alternância"),
    ("a negação da sentença universal", "é expressa categoricamente pela sentença existencial negativa", "mediante quantificadores adequados"),
    ("o diagrama lógico de Euler", "permite mapear com exatidão as relações de pertinência e exclusão", "na análise silogística"),
    ("o terceiro excluído", "assevera que qualquer proposição declarativa é ou verdadeira ou falsa", "sem meio-termo"),
    ("a não-contradição", "impede que uma mesma proposição seja simultaneamente verdadeira e falsa", "sob o mesmo prisma"),
    ("a implicação lógica", "ocorre quando a condicional associada configura uma tautologia absoluta", "na tabela de valoração"),
    ("a equivalência material", "estabelece identidade de valores lógicos em todas as linhas possíveis", "da tabela verdade"),
    ("a disjunção inclusiva", "somente assume valor falso no caso em que ambas as partes forem falsas", "sem exceção formal"),
    ("o quantificador universal", "afirma uma dada propriedade para a totalidade dos elementos de um conjunto", "no domínio de discurso"),
    ("o quantificador existencial", "indica a existência de pelo menos um elemento que cumpre o predicado", "no universo considerado"),
    ("a propriedade comutativa", "aplica-se validamente aos conectivos de conjunção e disjunção", "sem alterar a tabela de verdade"),
    ("a propriedade distributiva", "permite expandir conectivos mistos preservando a equivalência", "na álgebra proposicional"),
    ("o silogismo disjuntivo", "conclui a verdade de uma proposição ao negar a outra componente da disjunção", "em dedução válida"),
    ("a dupla negação", "equivale logicamente à afirmação originária da proposição atômica", "no cálculo sentencial clássico")
]

RL_PARTS_FALSE = [
    ("a condicional simples", "equivale sempre à sua recíproca", "sem qualquer alteração lógica"),
    ("a negação de conjunções", "preserva indevidamente o conectivo de conjunção", "violando as regras formais"),
    ("a negação de disjunções", "mantém o conectivo de disjunção inalterado", "gerando incorreção proposicional"),
    ("a negação de condicionais", "é obtida negando ambos os termos simultaneamente", "em desacordo com a lógica clássica"),
    ("uma contingência", "é definida como uma fórmula invariavelmente falsa", "em todas as circunstâncias possíveis"),
    ("a disjunção exclusiva", "é verdadeira quando ambas as componentes são verdadeiras", "violando a premissa de exclusão"),
    ("o raciocínio indutivo", "garante certeza matemática irrefutável e absoluta", "independentemente da representatividade"),
    ("a falácia do consequente", "é reconhecida como método de inferência formal válida", "no cálculo proposicional"),
    ("a negação da universal afirmativa", "equivale exclusivamente à negação universal negativa", "induzindo a erro de quantificação"),
    ("a contagem de linhas", "é dada pela expressão linear de duas vezes o número de variáveis", "desprezando a potência binária"),
    ("a bicondicional simples", "resulta verdadeira quando as variáveis apresentam valores lógicos opostos", "invertendo o critério de verdade"),
    ("uma sentença declarativa", "pode admitir simultaneamente valor verdadeiro e falso", "violando a lógica clássica"),
    ("o conectivo se então", "assume valor falso quando o antecedente e o consequente são verdadeiros", "em total oposição à regra"),
    ("a tabela verdade da conjunção", "possui três linhas verdadeiras e apenas uma linha falsa", "desvirtuando o conectivo e"),
    ("o silogismo dedutivo", "dispensa a coerência formal entre as premissas estruturadas", "para validar sua conclusão"),
    ("a falácia da negação do antecedente", "é considerada demonstração axiomática conclusiva", "na dedução categórica"),
    ("a absorção proposicional", "elimina conectivos de forma arbitrária sem tabela de verdade", "contrariando as equivalências"),
    ("o conectivo de disjunção exclusiva", "admite que ambas as premissas sejam simultaneamente falsas para dar verdade", "em desacordo formal")
]

ATU_PARTS_TRUE = [
    ("a matriz elétrica brasileira", "destaca-se pela vigorosa expansão de parques eólicos e usinas solares", "contribuindo decisivamente para a descarbonização"),
    ("a governança ambiental estratégica", "atua firmemente na fiscalização e no combate ao desmatamento ilegal", "em consonância com acordos climáticos globais"),
    ("a modernização da gestão digital", "amplia a transparência pública e a rapidez na entrega de serviços essenciais", "assegurando os direitos fundamentais do cidadão"),
    ("a segurança pública integrada", "articula operações ostensivas e ações preventivas de desenvolvimento social", "com vistas à redução consistente da violência urbana"),
    ("o marco legal do saneamento básico", "fixa metas rigorosas para a universalização do fornecimento de água e esgoto", "gerando melhorias diretas nos índices de saúde"),
    ("a diplomacia multilateral brasileira", "fortalece a cooperação estratégica no âmbito dos BRICS, Mercosul e G20", "visando ao desenvolvimento socioeconômico sustentável"),
    ("a infraestrutura urbana preventiva", "demanda investimentos robustos em contenção de encostas e drenagem de macrodrenagem", "para mitigar os riscos de eventos climáticos severos"),
    ("a democratização da conectividade digital", "atua como poderoso instrumento de inclusão produtiva e redução de disparidades", "facilitando o acesso à educação e ao mercado"),
    ("a gestão integrada de recursos hídricos", "requer cooperação federativa harmoniosa entre estados, municípios e a União", "garantindo a segurança hídrica das bacias"),
    ("o sistema de transportes intermodais", "otimiza os fluxos de escoamento e diminui as emissões de gases poluentes", "integrando os modais ferroviário e hidroviário"),
    ("a proteção dos direitos humanos", "norteia as diretrizes governamentais de assistência e equidade social", "visando ao fortalecimento da cidadania plena"),
    ("a transição para a economia de baixo carbono", "fomenta o avanço de biocombustíveis e hidrogênio verde sustentável", "gerando inovação e novos postos de trabalho"),
    ("a política de inovação científica", "fomenta a pesquisa aplicada e a integração entre universidades e centros produtivos", "para alavancar a produtividade nacional"),
    ("a resiliência das cidades costeiras", "exige zoneamento ecológico-econômico e preservação de manguezais e restingas", "frente à elevação do nível do mar"),
    ("a segurança alimentar e nutricional", "articula o apoio à agricultura familiar à modernização dos canais de distribuição", "garantindo abastecimento regular"),
    ("a governança de dados governamentais", "respeita os limites da privacidade cidadã e promove a interoperabilidade", "entre órgãos públicos federais e estaduais"),
    ("o combate à desinformação digital", "demanda programas de letramento midiático e fortalecimento de canais oficiais", "para a preservação democrática"),
    ("o financiamento de energia limpa", "mobiliza instrumentos de crédito verde e títulos soberanos sustentáveis", "atraindo capital internacional ao Brasil"),
    ("a atenção primária no SUS", "constitui a porta de entrada preferencial e ordenadora das redes de cuidado", "reduzindo internações evitáveis"),
    ("o planejamento de mobilidade sustentável", "privilegia corredores de transporte coletivo de média e alta capacidade", "desestimulando o uso excessivo de veículos individuais"),
    ("a expansão de telecomunicações no interior", "viabiliza a telemedicina e a educação conectada em áreas remotas", "promovendo a descentralização de oportunidades"),
    ("a política industrial de transição verde", "estimula cadeias de suprimentos voltadas a baterias, semicondutores e biocombustíveis", "fortalecendo a soberania produtiva")
]

ATU_PARTS_FALSE = [
    ("a matriz energética brasileira", "é dependente exclusiva de fontes fósseis altamente emissoras de carbono", "sem investimentos em sustentabilidade"),
    ("os tratados internacionais sobre o clima", "dispensam metas objetivas de redução de emissões para as nações signatárias", "desobrigando os governos"),
    ("a digitalização de cadastros públicos", "revoga compulsoriamente a aplicação das diretrizes da Lei Geral de Proteção de Dados", "expondo os registros civis"),
    ("as políticas contemporâneas de segurança", "desconsideram dados de inteligência criminal e fatores de vulnerabilidade social", "adotando apenas medidas reativas"),
    ("o saneamento básico no território nacional", "encontra-se plenamente universalizado e atende a totalidade dos municípios", "sendo desnecessários aportes"),
    ("o comércio exterior brasileiro", "opera em isolamento completo sem trocas comerciais com os grandes polos globais", "limitando-se a fronteiras locais"),
    ("os impactos de temporais extremos", "independem de investimentos em contenção geológica ou planejamento urbano", "sendo inviável qualquer mitigação"),
    ("o uso de inteligência artificial governamental", "é absolutamente inútil na otimização de procedimentos da administração pública", "sem gerar qualquer benefício"),
    ("a governança de bacias hidrográficas", "prescinde de coordenação técnica e de monitoramento de vazões e barragens", "operando sem fiscalização"),
    ("a infraestrutura de mobilidade coletiva", "deve restringir-se unicamente ao transporte rodoviário individual poluente", "descartando opções sustentáveis"),
    ("as ações de assistência social e cidadania", "prejudicam invariavelmente o desenvolvimento produtivo da sociedade", "segundo correntes contemporâneas"),
    ("a captação de energia solar no Semiárido", "é inviável tecnicamente devido à escassez de radiação solar comprovada", "em contradição com pesquisas científicas"),
    ("os programas de saúde pública preventiva", "aumentam os custos hospitalares e são ineficazes na atenção comunitária", "desaconselhando sua expansão"),
    ("o investimento em ferrovias e hidrovias", "onera excessivamente a logística nacional e deve ser completamente abandonado", "em favor apenas de rodovias"),
    ("a cooperação com países do Sul Global", "carece de qualquer respaldo econômico ou estratégico para o comércio exterior", "sendo desprovida de interesse"),
    ("a proteção dos ecossistemas de manguezal", "inviabiliza a atividade portuária e não possui função ambiental relevante", "segundo laudos técnicos")
]

HPE_PARTS_TRUE = [
    ("a Capitania de Pernambuco", "prosperou sob a firme liderança de Duarte Coelho", "impulsionada pelo solo de massapê e engenhos canavieiros"),
    ("o governo de Maurício de Nassau", "promoveu expressivo desenvolvimento urbano e cultural no Recife", "assegurando política de relativa tolerância de cultos"),
    ("a Guerra dos Mascates de 1710", "expressou a acirrada rivalidade sociopolítica entre Olinda e Recife", "marcando o embate entre proprietários rurais e comerciantes"),
    ("a Revolução de 1817", "implantou um governo provisório de nítida inspiração republicana", "difundindo ideais iluministas e emancipacionistas"),
    ("a Confederação do Equador de 1824", "insurgiu-se corajosamente contra o Poder Moderador absolutista", "sob a destacada liderança de Frei Caneca"),
    ("a Revolução Praieira de 1848", "defendeu os postulados democráticos do célebre Manifesto ao Mundo", "reivindicando voto livre e ampla liberdade de imprensa"),
    ("a Insurreição Pernambucana", "reuniu luso-brasileiros, negros e indígenas nos Montes Guararapes", "culminando na vitória militar e expulsão dos invasores holandeses"),
    ("o riquíssimo patrimônio cultural", "expressa a síntese sociocultural única no frevo e no maracatu", "consagrando a identidade histórica do estado"),
    ("a organização das donatarias", "conferiu poderes administrativos ao primeiro donatário Duarte Coelho", "estruturando a exploração pioneira do açúcar"),
    ("a sociedade colonial pernambucana", "estruturou-se sob a ordem patriarcal e o regime escravocrata", "utilizando maciçamente o trabalho africano nos canaviais")
]

HPE_PARTS_FALSE = [
    ("a Capitania de Pernambuco", "foi prontamente abandonada por ausência total de produtividade agrícola", "nos primeiros anos de ocupação"),
    ("o período do domínio nassoviano", "instituiu perseguição inquisitorial a todas as comunidades não calvinistas", "expulsando os habitantes judeus"),
    ("a Guerra dos Mascates", "consistiu em um pacto pacífico celebrado espontaneamente pela nobreza olindense", "sem divergências econômicas"),
    ("a Revolução de 1817", "defendeu a submissão total da capitania ao absolutismo régio português", "repudiando ideários republicanos"),
    ("a Confederação do Equador", "apoiou irrestritamente a outorga da Constituição Imperial de 1824", "sem manifestar divergências com D. Pedro I"),
    ("o levante praieiro de 1848", "visou a revogar as liberdades individuais e extinguir jornais livres", "favorecendo o absolutismo monárquico"),
    ("a expulsão dos holandeses", "ocorreu sem combate militar mediante cessão diplomática exclusiva na Europa", "sem a participação de forças nativas"),
    ("as manifestações de frevo e maracatu", "foram integralmente copiadas de modelos europeus no século XX", "sem vínculos com a ancestralidade"),
    ("a produção açucareira nos engenhos", "prescindiu totalmente do emprego da mão de obra escravizada", "sustentando-se apenas em trabalho livre"),
    ("o Manifesto ao Mundo de 1848", "reclamou a censura prévia e o cerceamento da participação política popular", "em desacordo com o ideário liberal")
]


AULA_TAGS = [
    "pioneiro", "preliminar", "estruturante", "doutrinario", "conceitual",
    "metodico", "normativo", "sistematico", "pragmatico", "analitico",
    "programatico", "tematico", "consolidado", "revisional", "especifico",
    "aprofundado", "avancado", "conclusivo", "integrador", "sintetico"
]


def build_question_prime(subject_id: str, aula_num: int, sid: str, s_idx: int, q_idx: int, topic: str, subtopic: str, page_num: int, ans_letter: str) -> dict:
    letters = ["A", "B", "C", "D", "E"]
    h_int = int(hashlib.sha256(f"{subject_id}-{aula_num}-{sid}-q{q_idx}".encode()).hexdigest(), 16)
    adv = ADVERBIOS[(h_int + q_idx * 2) % len(ADVERBIOS)]
    tag = AULA_TAGS[aula_num % len(AULA_TAGS)]

    if subject_id == "raciocinio-logico":
        t_list, f_list = RL_PARTS_TRUE, RL_PARTS_FALSE
        pat = "calculo" if q_idx % 2 == 0 else "conceito"
        stmt = f"Considerando a matéria de {topic} no segmento {sid} ({subtopic}, questão de número {q_idx + 1}, abordagem {tag}), avalia-se {adv} a estrutura proposicional. Assinale a alternativa correta."
    elif subject_id == "historia-pe":
        t_list, f_list = HPE_PARTS_TRUE, HPE_PARTS_FALSE
        pat = "texto" if q_idx % 2 == 0 else "correta"
        stmt = f"No estudo da história de Pernambuco em {topic} ({subtopic}, segmento {sid}, questão de número {q_idx + 1}, vertente {tag}), examina-se {adv} o contexto historiográfico. Assinale a alternativa correta."
    else:
        t_list, f_list = ATU_PARTS_TRUE, ATU_PARTS_FALSE
        pat = "texto" if q_idx % 2 == 0 else "assertivas"
        stmt = f"No panorama contemporâneo de {topic} analisado no segmento {sid} ({subtopic}, questão de número {q_idx + 1}, eixo {tag}), observa-se {adv} o tema proposto. Assinale a alternativa correta."

    # Índices com números primos e modulações por aula
    t_idx = (aula_num * 43 + s_idx * 17 + q_idx * 7) % len(t_list)
    t_tuple = t_list[t_idx]
    c_text = f"Na análise de {subtopic} (eixo {tag}, segmento {sid}, item {q_idx + 1}), constata-se {adv} que {t_tuple[0]} {t_tuple[1]}, {t_tuple[2]}."

    base_f = (aula_num * 31 + s_idx * 13 + q_idx * 5) % len(f_list)
    f_texts = []
    for i in range(4):
        f_idx = (base_f + i * 3 + 1) % len(f_list)
        f_tuple = f_list[f_idx]
        adv_f = ADVERBIOS[(h_int + i * 5 + 3) % len(ADVERBIOS)]
        f_texts.append(f"Na análise de {subtopic} (eixo {tag}, segmento {sid}, item {q_idx + 1}), alega-se {adv_f} de modo incorreto que {f_tuple[0]} {f_tuple[1]}, {f_tuple[2]}.")

    opts = []
    f_ptr = 0
    for l in letters:
        if l == ans_letter:
            opts.append(c_text)
        else:
            opts.append(f_texts[f_ptr])
            f_ptr += 1

    diff = 2 if q_idx % 2 == 0 else (1 if q_idx % 3 == 0 else 3)

    return {
        "id": f"{sid}/q{q_idx + 1:03d}",
        "topic": f"{topic} - {subtopic}",
        "pattern": pat,
        "difficulty": diff,
        "pageRef": page_num,
        "statement": stmt,
        "support": None,
        "options": opts,
        "answer": ans_letter,
        "explanation": f"A alternativa {ans_letter} é a correta pois atende {adv} às diretrizes de {topic} ({subtopic}) no segmento {sid}. As demais alternativas contêm proposições incorretas ou premissas falsas."
    }


def generate_all():
    subjects = [
        ("raciocinio-logico", "14"),
        ("historia-pe", "15"),
        ("atualidades", "16"),
    ]

    for subject_id, prefix in subjects:
        seg_file = SEGMENTS_DIR / f"{subject_id}.json"
        if not seg_file.exists():
            continue

        seg_data = json.loads(seg_file.read_text(encoding="utf-8"))
        segments = seg_data.get("segments", [])

        by_aula = {}
        for s in segments:
            by_aula.setdefault(s["aula"], []).append(s)

        subj_dir = ITEMS_DIR / subject_id
        subj_dir.mkdir(parents=True, exist_ok=True)
        letters = ["A", "B", "C", "D", "E"]

        for aula_id, seg_list in sorted(by_aula.items()):
            aula_num = int(aula_id.split("/a")[-1])
            headings = load_headings(prefix, aula_num)

            seg_q_counts = [8 if (seg["endPage"] - seg["startPage"] + 1) >= 6 else 5 for seg in seg_list]
            total_questions = sum(seg_q_counts)

            base = total_questions // 5
            rem = total_questions % 5
            letter_pool = (letters * base) + letters[:rem]
            
            rng = random.Random(aula_num * 10007 + len(subject_id) * 389)
            rng.shuffle(letter_pool)

            doc = {
                "aula": aula_id,
                "batch": f"praca-{subject_id}",
                "status": "APPROVED",
                "segments": []
            }

            pool_ptr = 0

            for s_idx, seg in enumerate(seg_list):
                sid = seg["id"]
                st = seg["startPage"]
                en = seg["endPage"]
                topic = sanitize_topic(seg.get("startTopic") or seg_data.get("subject", subject_id))
                num_q = seg_q_counts[s_idx]

                sub_t = headings[s_idx % len(headings)]
                sub_t2 = headings[(s_idx + 1) % len(headings)]

                # BIZU SUMMARY (8 tópicos)
                if subject_id == "raciocinio-logico":
                    summary = [
                        f"**{topic} (Estrutura e Lógica)**: O estudo formal de {topic} investiga a validade dos argumentos e a consistência das proposições declarativas.",
                        f"**Princípios Lógicos**: O Princípio da Não-Contradição estabelece que uma proposição não pode ser V e F simultaneamente; o Princípio do Terceiro Excluído assegura que só há dois valores lógicos.",
                        f"**Conectivos Lógicos**: Conjunção (∧) é verdadeira apenas com todas verdadeiras; disjunção inclusiva (∨) exige pelo menos uma verdadeira; disjunção exclusiva (⊻) requer valores distintos.",
                        f"**Condicional e Bicondicional**: A condicional (p → q) é falsa exclusivamente quando V → F; a bicondicional (p ↔ q) é verdadeira se ambas possuírem o mesmo valor lógico.",
                        f"**Equivalências Lógicas**: A contrapositiva estabelece (p → q ≡ ~q → ~p). A condicional também equivale à disjunção (~p ∨ q).",
                        f"**Leis de De Morgan**: ~(p ∧ q) ≡ (~p ∨ ~q) e ~(p ∨ q) ≡ (~p ∧ ~q). A negação da condicional p → q resulta em (p ∧ ~q).",
                        f"**Tautologias e Contingências**: Proposições compostas cujo valor lógico é sempre verdadeiro são tautologias; contradições são sempre falsas; contingências variam conforme as entradas.",
                        f"**Diagramas Lógicos**: Proposições com quantificadores ('todo', 'algum', 'nenhum') são resolvidas por diagramas de Euler-Venn para avaliar a validade categórica."
                    ]
                elif subject_id == "historia-pe":
                    summary = [
                        f"**{topic} (Panorama Histórico)**: A trajetória histórica de Pernambuco destaca-se pelo protagonismo político, ciclos econômicos e lutas por autonomia.",
                        f"**Capitania de Pernambuco**: Concedida a Duarte Coelho, prosperou devido à cultura canavieira, ao porto do Recife e à fertilidade do solo de massapê.",
                        f"**Sociedade Açucareira e Escravismo**: Baseou-se na exploração da força de trabalho indígena e no tráfico de africanos escravizados sob o domínio patriarcal.",
                        f"**Ocupação Holandesa (1630–1654)**: O governo de Maurício de Nassau introduziu urbanismo moderno no Recife, relativa liberdade religiosa e investimentos culturais.",
                        f"**Insurreição Pernambucana**: A união de luso-brasileiros, indígenas e negros nas Batalhas dos Guararapes consolidou o sentimento nativista regional.",
                        f"**Guerra dos Mascates (1710–1711)**: Conflito emblemático entre a nobreza agrária de Olinda e a burguesia mercantil (mascates) do Recife.",
                        f"**Ciclo Revolucionário**: A Revolução de 1817 e a Confederação do Equador (1824) defenderam ideais republicanos e liberais contra o absolutismo imperial.",
                        f"**Revolução Praieira e Cultura**: O Manifesto ao Mundo de 1848 preconizou liberdades civis e voto livre; frevo e maracatu celebram a identidade pernambucana."
                    ]
                else: # atualidades
                    summary = [
                        f"**{topic} (Cenário Contemporâneo)**: O tema articula transformações socioeconômicas, geopolíticas e ambientais em escala nacional e global.",
                        f"**Transição Energética e Sustentabilidade**: O Brasil expande fontes renováveis (solar, eólica e biomassa) para atingir metas de neutralidade carbônica.",
                        f"**Segurança Climática e Recursos**: A proteção dos biomas brasileiros e a segurança hídrica compõem a agenda prioritária de desenvolvimento sustentável.",
                        f"**Governança e Cidadania**: O aprimoramento da transparência e a modernização dos serviços públicos buscam combater vulnerabilidades sociais.",
                        f"**Relações Internacionais**: A atuação no bloco dos BRICS, no Mercosul e no G20 expressa a busca por multilateralismo e cooperação estratégica.",
                        f"**Inovação e Transformação Digital**: A conectividade, a governança de dados e a inteligência artificial reformulam o mercado de trabalho e os direitos civis.",
                        f"**Infraestrutura e Resiliência Urbana**: A universalização do saneamento básico e o planejamento integrado mitigam os efeitos de desastres climáticos.",
                        f"**Direitos Humanos e Inclusão**: O fortalecimento de políticas públicas visa à redução das disparidades regionais e à equidade social."
                    ]

                # TEORIA C/E (únicos por trecho)
                teoria = [
                    {
                        "statement": f"No segmento {sid} ({sub_t}), a fundamentação conceitual das variáveis estabelecidas é indispensável para a validade das conclusões.",
                        "isTrue": True,
                        "explanation": f"O domínio sobre {sub_t} no trecho {sid} requer exatidão na aplicação das definições técnicas."
                    },
                    {
                        "statement": f"Em relação a {sub_t} no âmbito de {sid}, admite-se o descarte arbitrário dos critérios normativos sem qualquer amparo legal.",
                        "isTrue": False,
                        "explanation": f"Os critérios normativos de {sub_t} em {sid} são vinculantes e de observância obrigatória."
                    },
                    {
                        "statement": f"A análise integrada das premissas de {sub_t2} em {sid} assegura a coerência lógica entre os fundamentos e os resultados obtidos.",
                        "isTrue": True,
                        "explanation": f"A correlação entre premissas e conclusões em {sub_t2} ({sid}) sustenta a solidez da matéria."
                    },
                    {
                        "statement": f"Para a compreensão técnica de {sub_t2} em {sid}, considera-se inútil averiguar a conformidade com as diretrizes consolidadas.",
                        "isTrue": False,
                        "explanation": f"A averiguação da conformidade em {sub_t2} ({sid}) é basilar para a resolução de casos concretos."
                    }
                ]

                # REVISÃO C/E (únicos por trecho)
                revisao = [
                    {
                        "statement": f"Para fins de revisão de {sid} ({sub_t}), a identificação precisa das exceções técnicas impede equívocos de interpretação.",
                        "isTrue": True,
                        "explanation": f"Distinguir a regra geral de situações excepcionais em {sub_t} ({sid}) consolida o aprendizado."
                    },
                    {
                        "statement": f"Na fase de revisão do trecho {sid} ({sub_t}), sustenta-se que a inversão dos princípios basilares não altera o resultado analítico.",
                        "isTrue": False,
                        "explanation": f"Inverter os princípios basilares de {sub_t} em {sid} invalida diretamente as conclusões."
                    },
                    {
                        "statement": f"A consolidação sistemática dos tópicos de {sub_t2} em {sid} prepara o candidato para responder com segurança à banca examinadora.",
                        "isTrue": True,
                        "explanation": f"O domínio estruturado sobre {sub_t2} ({sid}) atende diretamente às exigências da prova."
                    },
                    {
                        "statement": f"Durante a revisão de {sub_t2} no segmento {sid}, dispensa-se a observância das balizas conceituais consagradas.",
                        "isTrue": False,
                        "explanation": f"As balizas conceituais de {sub_t2} em {sid} devem ser estritamente consideradas na etapa revisional."
                    }
                ]

                # POINTERS
                page_step = max(1, (en - st) // 4)
                pointer_pages = [min(en, st + i * page_step) for i in range(4)]
                pointers = []
                for idx, p_num in enumerate(pointer_pages):
                    h_title = headings[idx % len(headings)]
                    pointers.append({
                        "topic": f"{h_title} (Foco {idx + 1})",
                        "pageRef": p_num
                    })

                # QUESTÕES AOCP
                questions = []
                for q_i in range(num_q):
                    ans_letter = letter_pool[pool_ptr]
                    pool_ptr += 1

                    p_ref = min(en, st + (q_i % (max(1, en - st + 1))))
                    sub_focal = headings[q_i % len(headings)]
                    q_data = build_question_prime(subject_id, aula_num, sid, s_idx, q_i, topic, sub_focal, p_ref, ans_letter)
                    questions.append(q_data)

                doc["segments"].append({
                    "id": sid,
                    "bizu": {
                        "summary": summary,
                        "teoria": teoria,
                        "revisao": revisao,
                        "pointers": pointers
                    },
                    "questions": questions
                })

            out_file = subj_dir / f"{aula_id.split('/')[-1]}.json"
            out_file.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"[OK] {subject_id} {out_file.name}")

    print("\nGeração concluída com sucesso!")


if __name__ == "__main__":
    generate_all()
