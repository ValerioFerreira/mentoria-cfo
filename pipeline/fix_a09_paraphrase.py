import json
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
p = ROOT / "content" / "items" / "direito-constitucional" / "a09.json"
doc = json.loads(p.read_text(encoding="utf-8"))

# Mapeamento de reparafraseamento exato por questão
# segmentId, qIndex, field, new_text
REPLACEMENTS = {
    # s01 q1 opt_E
    ("direito-constitucional/a09/s01", 0, "options", 4): (
        "Submetem-se ao regime jurídico-administrativo não apenas as estruturas estatais típicas, mas também os agentes delegados no desempenho de atividades públicas."
    ),
    # s01 q3 explanation
    ("direito-constitucional/a09/s01", 2, "explanation"): (
        "Autarquias demandam lei específica para sua direta criação (art. 37, XIX). Já as empresas estatais, sociedades de economia mista e fundações públicas dependem de autorização legislativa para serem instituídas, cabendo à lei complementar fixar as áreas de atuação fundacional."
    ),
    # s01 q5 explanation
    ("direito-constitucional/a09/s01", 4, "explanation"): (
        "Empresas públicas admitem qualquer formatação societária sob capital exclusivamente público. Já as sociedades de economia mista estruturam-se obrigatoriamente como sociedade anônima, com maioria das ações votantes sob controle estatal."
    ),
    # s01 q6 opt_E
    ("direito-constitucional/a09/s01", 5, "options", 4): (
        "Entidades privadas da administração descentralizada voltadas a atividades de interesse coletivo."
    ),
    # s01 q6 explanation
    ("direito-constitucional/a09/s01", 5, "explanation"): (
        "Conforme o STF (ADI 2.310), o poder de polícia estatal é indelegável a pessoas jurídicas de direito privado da estrutura indireta, ressalvada a hipótese de estatais não concorrenciais prestadoras de serviço público exclusivo."
    ),
    # s01 q9 explanation
    ("direito-constitucional/a09/s01", 8, "explanation"): (
        "A publicidade governamental deve ter caráter estritamente educativo, informativo ou de orientação social (art. 37, § 1º), sendo inconstitucional a veiculação de marcas, fotografias ou termos que identifiquem agentes políticos ou impliquem enaltecimento individual."
    ),
    # s02 q3
    ("direito-constitucional/a09/s02", 2, "explanation"): (
        "A exigência de teste psicológico para admissão no serviço público é nula se não constar expressamente em lei em sentido estrito, conforme jurisprudência pacífica e Súmula Vinculante 44. A mera menção no edital não supre a reserva legal."
    ),
    # s04 q2 opt_A
    ("direito-constitucional/a09/s04", 1, "options", 0): (
        "Dois cargos ou empregos exercidos na área de saúde, desde que as profissões sejam devidamente regulamentadas e haja compatibilidade de horários."
    ),
    # s03 q1 opt_A
    ("direito-constitucional/a09/s03", 0, "options", 0): (
        "O vínculo por concurso destina-se aos cargos de carreira efetivos, ao passo que funções comissionadas destinam-se a chefia, direção e assessoramento."
    ),
    # s03 q2 opt_E
    ("direito-constitucional/a09/s03", 1, "options", 4): (
        "Destinam-se exclusivamente a atribuições diretivas, de assessoramento e chefia, nas quais se exige confiança e livre nomeação."
    ),
    # s03 q3 explanation
    ("direito-constitucional/a09/s03", 2, "explanation"): (
        "A Súmula Vinculante 13 veda o nepotismo na Administração direta e indireta de qualquer dos Poderes, impedindo a escolha de cônjuge, companheiro ou parentes consanguíneos/afins até o 3º grau da autoridade nomeante ou de ocupante de cargo diretivo na mesma esfera jurídica."
    ),
    # s03 q8 explanation
    ("direito-constitucional/a09/s03", 7, "explanation"): (
        "A Súmula Vinculante 55 estabelece que o benefício de auxílio-alimentação não contempla os servidores inativos, possuindo natureza indenizatória vinculada ao exercício funcional presencial."
    ),
    # s03 q10 explanation
    ("direito-constitucional/a09/s03", 9, "explanation"): (
        "A revisão remuneratória anual (art. 37, X) requer lei específica com iniciativa privativa do chefe do respectivo Poder, em idêntica data e sem diferenciação de índices. O Judiciário não pode conceder reajuste indenizatório pela omissão legislativa (Súmula Vinculante 37)."
    ),
    # s03 q11 opt_D
    ("direito-constitucional/a09/s03", 10, "options", 3): (
        "Parcelas remuneratórias de natureza indenizatória ou decorrentes de encargo de chefia, direção e confiança."
    ),
    # s03 q13 explanation
    ("direito-constitucional/a09/s03", 12, "explanation"): (
        "A Súmula Vinculante 42 proíbe atrelar remuneração de servidores estaduais/municipais a índices ou parâmetros federais de correção monetária. O teto geral do funcionalismo é o subsídio dos Ministros do STF (art. 37, XI)."
    ),
    # s03 q14 statement
    ("direito-constitucional/a09/s03", 13, "statement"): (
        "Em relação ao regime remuneratório dos servidores públicos previsto no art. 37, XIV, da CF/88, as vantagens e acréscimos pecuniários concedidos"
    ),
    # s03 q14 opt_E
    ("direito-constitucional/a09/s03", 13, "options", 4): (
        "Não incidem sobre parcelas adicionais anteriores, vedando-se a superposição de gratificações (efeito repique)."
    ),
    # s04 q1 statement
    ("direito-constitucional/a09/s04", 0, "statement"): (
        "A proibição constitucional de cumulação remunerada de cargos, funções e empregos públicos (art. 37, XVI e XVII)"
    ),
    # s04 q1 opt_C
    ("direito-constitucional/a09/s04", 0, "options", 2): (
        "Abrange autarquias, fundações estatais, empresas públicas, sociedades de economia mista, empresas controladas e subsidiárias."
    ),
    # s04 q2 opt_A
    ("direito-constitucional/a04/s04", 1, "options", 0): (
        "Dois vínculos privativos de profissionais da área da saúde, desde que haja regulamentação da profissão e compatibilidade de horários."
    ),
    # s04 q2 explanation
    ("direito-constitucional/a09/s04", 1, "explanation"): (
        "O art. 37, XVI, 'c', autoriza cumular dois cargos ou empregos na área de saúde, exigindo profissão regulamentada e horários compatíveis. O STF não impõe teto fixo de 60 horas semanais se comprovada a compatibilidade."
    ),
    # s04 q3 opt_C
    ("direito-constitucional/a09/s04", 2, "options", 2): (
        "Apenas dois vínculos de médico, não cabendo extensão a outros especialistas da área de perícia."
    ),
    # s04 q3 explanation
    ("direito-constitucional/a09/s04", 2, "explanation"): (
        "Conforme jurisprudência do STJ, o cargo de perito criminal de polícia não configura cargo privativo de profissional de saúde para efeito de cumulação, ainda que a formação exigida seja medicina veterinária."
    ),
    # s04 q6 opt_C
    ("direito-constitucional/a09/s04", 5, "options", 2): (
        "Função de livre provimento e demissão declarada em diploma legal ordinário."
    ),
    # s04 q9 statement
    ("direito-constitucional/a09/s04", 8, "statement"): (
        "O art. 39 da CF/88, com as alterações da Reforma Administrativa, disciplina a política remuneratória do funcionalismo estabelecendo que"
    ),
    # s04 q10 statement
    ("direito-constitucional/a09/s04", 9, "statement"): (
        "Na estruturação remuneratória e fixação de vencimentos para as carreiras públicas (art. 39, § 1º, da CF/88), deve-se levar em conta"
    ),
    # s04 q10 opt_D
    ("direito-constitucional/a09/s04", 9, "options", 3): (
        "A natureza, o nível de complexidade e as responsabilidades inerentes a cada cargo público."
    ),
    # s04 q10 explanation
    ("direito-constitucional/a09/s04", 9, "explanation"): (
        "O art. 39, § 1º, impõe que a fixação de vencimentos considere a natureza, complexidade e responsabilidade dos cargos, bem como os requisitos de escolaridade e peculiaridades das carreiras."
    ),
    # s04 q11 opt_B
    ("direito-constitucional/a09/s04", 10, "options", 1): (
        "Exame especial de desempenho conduzido por colegiado constituído especificamente para tal encargo."
    ),
    # s04 q11 explanation
    ("direito-constitucional/a09/s04", 10, "explanation"): (
        "A estabilidade exige aprovação prévia em concurso, três anos de efetivo exercício no cargo de provimento efetivo e parecer favorável em avaliação especial de desempenho realizada por comissão instituída para esse fim (art. 41, § 4º)."
    ),
    # s04 q13 opt_A
    ("direito-constitucional/a09/s04", 12, "options", 0): (
        "Mário retorna por reintegração; Pedro, sendo estável, retorna ao cargo anterior sem indenização, ou será aproveitado em outra vaga ou colocado em disponibilidade proporcional."
    ),
    # s04 q13 explanation
    ("direito-constitucional/a09/s04", 12, "explanation"): (
        "Invalidada a demissão do servidor estável por decisão judicial, dá-se a reintegração. O ocupante anterior (se estável) é reconduzido ao posto de origem sem direito a indenização, aproveitado em outra função ou posto em disponibilidade proporcional ao tempo de contribuição (art. 41, § 2º)."
    ),
    # s04 q14 opt_E
    ("direito-constitucional/a09/s04", 13, "options", 4): (
        "Permanece em disponibilidade, com estipêndio proporcional ao tempo contributivo, até futuro aproveitamento."
    ),
    # s04 q14 explanation
    ("direito-constitucional/a09/s04", 13, "explanation"): (
        "Extinto o cargo público ou declarada a sua desnecessidade, o servidor já detentor de estabilidade fica em disponibilidade remunerada proporcionalmente ao tempo de serviço/contribuição, até ser adequadamente aproveitado (art. 41, § 3º)."
    ),
    # s05 q4 explanation
    ("direito-constitucional/a09/s05", 3, "explanation"): (
        "A EC 103/2019 vedou a criação de novos regimes próprios de previdência e proibiu a coexistência de mais de um RPPS e de mais de uma unidade gestora por ente estatal, englobando os Poderes Executivo, Legislativo e Judiciário (art. 40, § 20)."
    ),
    # s05 q6 opt_A
    ("direito-constitucional/a09/s05", 5, "options", 0): (
        "Requer grau de instrução e qualificação técnica compatíveis com a nova função, preservando-se o padrão remuneratório originário."
    ),
    # s05 q11 opt_B
    ("direito-constitucional/a09/s05", 10, "options", 1): (
        "Fará jus a abono de permanência facultado ao ente, limitado ao equivalente de sua contribuição, até atingir a idade limite de desligamento compulsório."
    ),
    # s05 q13 explanation
    ("direito-constitucional/a09/s05", 12, "explanation"): (
        "A passagem para a inatividade com aproveitamento de tempo de serviço público ou privado encerra o liame funcional com o cargo respectivo. A Carta Magna veda contagem de tempo fictício para aposentadoria (art. 40, § 10 e § 14)."
    ),
    # s06 q1 opt_A
    ("direito-constitucional/a09/s06", 0, "options", 0): (
        "Aplica-se objetivamente a entes públicos e a pessoas jurídicas privadas prestadoras de serviços de utilidade pública."
    ),
    # s06 q1 opt_E
    ("direito-constitucional/a09/s06", 0, "options", 4): (
        "Incide sobre corporações estatais atuantes na exploração de atividade econômica em regime puramente mercantil."
    ),
    # s06 q1 explanation
    ("direito-constitucional/a09/s06", 0, "explanation"): (
        "O art. 37, § 6º, consagra a responsabilidade civil objetiva para pessoas de direito público e concessionárias/permissionárias delegatárias de serviços públicos. Empresas públicas e sociedades de economia mista que exerçam atividade econômica submetem-se ao regime de direito privado (art. 173)."
    ),
    # s06 q4 explanation
    ("direito-constitucional/a09/s06", 3, "explanation"): (
        "A concessionária responde perante terceiros na modalidade objetiva, ressalvada a ação regressiva contra o agente público causador direto do dano nos casos em que comprovado dolo ou culpa (art. 37, § 6º)."
    ),
    # s06 q6 explanation
    ("direito-constitucional/a09/s06", 5, "explanation"): (
        "O instrumento de contrato de gestão/desempenho expande a flexibilidade administrativa e orçamentária dos órgãos e entidades, subordinando-os a metas institucionais e critérios formais de avaliação (art. 37, § 8º)."
    ),
    # s06 q11 statement
    ("direito-constitucional/a09/s06", 10, "statement"): (
        "Dois militares estaduais da ativa foram investidos: um em cargo público civil de provimento efetivo, e o outro em encargo civil temporário não eletivo. Segundo as normas constitucionais aplicáveis às corporações militares (art. 42 c/c art. 142, § 3º):"
    ),
    # s06 q14 opt_C
    ("direito-constitucional/a09/s06", 13, "options", 2): (
        "As diretrizes pensionais submetem-se a lei própria do Estado, sendo a disciplina militar regida por estatuto legal específico."
    ),
    # s06 q14 explanation
    ("direito-constitucional/a09/s06", 13, "explanation"): (
        "As normas atinentes à pensão militar estadual e ao código de ética e disciplina das corporações devem constar em lei estadual específica (art. 42, § 1º e § 2º), definindo sanções, procedimentos e garantias recursais."
    ),
}

# Aplica modificações
for seg in doc.get("segments", []):
    sid = seg["id"]
    for qidx, q in enumerate(seg.get("questions", [])):
        # Statement
        key_stmt = (sid, qidx, "statement")
        if key_stmt in REPLACEMENTS:
            q["statement"] = REPLACEMENTS[key_stmt]
            
        # Explanation
        key_exp = (sid, qidx, "explanation")
        if key_exp in REPLACEMENTS:
            q["explanation"] = REPLACEMENTS[key_exp]
            
        # Options
        for oidx in range(5):
            key_opt = (sid, qidx, "options", oidx)
            if key_opt in REPLACEMENTS:
                q["options"][oidx] = REPLACEMENTS[key_opt]

p.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print("Substituições aplicadas em direito-constitucional/a09.json com sucesso!")
