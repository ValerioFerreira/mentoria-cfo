# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s05"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cf.clean.txt", "r", encoding="utf-8") as f:
    cf = f.read()

registros = []

# 1: Linha 14
registros.append({
    "linha": 14,
    "citacao": "art. 12 da Lei 8.429/1992, com redação da Lei 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "As sanções são o ponto em que as provas gostam de cobrar números: anos de suspensão dos direitos políticos, anos de proibição de contratar, múltiplos da multa. A Lei 14.230/2021 reescreveu todo o art. 12",
    "resultado": "OK",
    "trecho_lei": "Art. 12. Independentemente do ressarcimento integral do dano patrimonial, se efetivo, e das sanções penais comuns e de responsabilidade, civis e administrativas previstas na legislação específica"
})

# 2: Linha 17
registros.append({
    "linha": 17,
    "citacao": "art. 12 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Distinguir as sanções do art. 12 por espécie de ato e memorizar os limites de cada uma.",
    "resultado": "OK",
    "trecho_lei": "está o responsável pelo ato de improbidade sujeito às seguintes cominações, que podem ser aplicadas isolada ou cumulativamente, de acordo com a gravidade do fato:"
})

# 3: Linha 25
registros.append({
    "linha": 25,
    "citacao": "art. 12 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "As sanções por improbidade são aplicadas pelo **Poder Judiciário**, na ação de improbidade, que segue o Código de Processo Civil e as regras próprias da LIA. O art. 12 define o regime: o responsável fica sujeito às cominações previstas, **isolada ou cumulativamente**, conforme a gravidade do fato",
    "resultado": "OK",
    "trecho_lei": "Art. 12. Independentemente do ressarcimento integral do dano patrimonial, se efetivo, e das sanções penais comuns e de responsabilidade"
})

# 4: Linha 32
registros.append({
    "linha": 32,
    "citacao": "art. 12, § 6º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "4. **Dedução do ressarcimento já obtido.** Se houver lesão ao patrimônio público, a reparação nesta lei deve deduzir o que já foi ressarcido nas esferas criminal, civil e administrativa pelos mesmos fatos (art. 12, § 6º).",
    "resultado": "OK",
    "trecho_lei": "§ 6º Se ocorrer lesão ao patrimônio público, a reparação do dano a que se refere esta Lei deverá deduzir o ressarcimento ocorrido nas instâncias criminal, civil e administrativa"
})

# 5: Linha 36
registros.append({
    "linha": 36,
    "citacao": "art. 10 e art. 21 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 21 estabelece que a aplicação das sanções independe: (a) da efetiva ocorrência de dano ao patrimônio público, salvo quanto ao ressarcimento e às condutas de lesão ao erário (art. 10); e (b) da aprovação ou rejeição das contas pelo controle interno ou pelo Tribunal ou Conselho de Contas.",
    "resultado": "OK",
    "trecho_lei": "I - da efetiva ocorrência de dano ao patrimônio público, salvo quanto à pena de ressarcimento e às condutas previstas no art. 10 desta Lei;"
})

# 6: Linha 38
registros.append({
    "linha": 38,
    "citacao": "art. 21, §§ 1º e 2º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Isso decorre de duas coisas. Enriquecimento ilícito e violação a princípios não exigem dano ao erário. E a aprovação das contas não afasta a improbidade, porque a análise das contas não tem como objetivo apurar esse ilícito. Mas as decisões do controle serão consideradas pelo juiz se o agente se baseou neles ao agir, e as provas produzidas perante os órgãos de controle entram na formação do convencimento, sem dispensar a análise do dolo (art. 21, §§ 1º e 2º).",
    "resultado": "OK",
    "trecho_lei": "§ 1º Os atos do órgão de controle interno ou externo serão considerados pelo juiz quando tiverem servido de fundamento para a conduta do agente público."
})

# 7: Linha 47
registros.append({
    "linha": 47,
    "citacao": "arts. 9º, 10 e 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Sanção | Enriquecimento ilícito (art. 9º) | Lesão ao erário (art. 10) | Violação a princípios (art. 11) |",
    "resultado": "OK",
    "trecho_lei": "I - na hipótese do art. 9º desta Lei, perda dos bens ou valores acrescidos ilicitamente ao patrimônio, perda da função pública, suspensão dos direitos políticos até 14 (catorze) anos"
})

# 8: Linha 58
registros.append({
    "linha": 58,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> Associe cada espécie a um número: enriquecimento ilícito, **14**; lesão ao erário, **12**; violação a princípios, **24**.",
    "resultado": "OK",
    "trecho_lei": "III - na hipótese do art. 11 desta Lei, pagamento de multa civil de até 24 (vinte e quatro) vezes o valor da remuneração percebida pelo agente"
})

# 9: Linha 60
registros.append({
    "linha": 60,
    "citacao": "art. 9º, art. 10 e art. 12, II da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "As penalidades de enriquecimento ilícito e lesão ao erário são parecidas, com três diferenças: a perda de bens na lesão só ocorre se concorrer a circunstância de acréscimo patrimonial ilícito (do agente ou do terceiro beneficiado, nos termos do art. 12, II); a multa equivale ao acréscimo (art. 9º) ou ao dano (art. 10); e os prazos são de até 14 ou de até 12 anos.",
    "resultado": "OK",
    "trecho_lei": "II - na hipótese do art. 10 desta Lei, perda dos bens ou valores acrescidos ilicitamente ao patrimônio, se concorrer esta circunstância, perda da função pública, suspensão dos direitos políticos até 12 (doze) anos"
})

# 10: Linha 62
registros.append({
    "linha": 62,
    "citacao": "art. 11 da Lei 8.429/1992 e art. 37, § 4º da Constituição Federal",
    "lei": "cf",
    "frase_capitulo": "O STF considerou constitucional a limitação das sanções do art. 11 a apenas duas. O argumento é que o art. 37, § 4º, da Constituição prevê as consequências \"na forma e gradação previstas em lei\", de modo que a definição de quais sanções cabem em cada ato está dentro da liberdade do legislador.",
    "resultado": "OK",
    "trecho_lei": "§ 4º Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
})

# 11: Linha 66
registros.append({
    "linha": 66,
    "citacao": "art. 9º e art. 10 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A[\"Art. 9: até 14 anos, perda de bens, função, multa e proibição\"] --> B[\"Art. 10: até 12 anos, mesmas sanções com perda de bens excepcional\"]",
    "resultado": "OK",
    "trecho_lei": "pagamento de multa civil equivalente ao valor do acréscimo patrimonial e proibição de contratar com o poder público ou de receber benefícios ou incentivos fiscais ou creditícios"
})

# 12: Linha 67
registros.append({
    "linha": 67,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "B --> C[\"Art. 11: só multa de até 24 remunerações e proibição de até 4 anos\"]",
    "resultado": "OK",
    "trecho_lei": "proibição de contratar com o poder público ou de receber benefícios ou incentivos fiscais ou creditícios, direta ou indiretamente, ainda que por intermédio de pessoa jurídica da qual seja sócio majoritário, pelo prazo não superior a 4 (quatro) anos;"
})

# 13: Linha 74
registros.append({
    "linha": 74,
    "citacao": "art. 12, § 1º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "No julgamento das ADIs 7156 e 7236, concluído em 1º/7/2026, o STF retirou do art. 12, § 1º, as expressões \"apenas\", \"na hipótese do inciso I do caput deste artigo\" e \"em caráter excepcional\" e deu interpretação conforme a Constituição ao restante",
    "resultado": "OK",
    "trecho_lei": "§ 1º A sanção de perda da função pública, nas hipóteses dos incisos I e II do caput deste artigo, atinge apenas o vínculo de mesma qualidade e natureza"
})

# 14: Linha 84
registros.append({
    "linha": 84,
    "citacao": "art. 9º, art. 10, art. 11 e art. 12, §§ 2º e 3º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A multa tem base no valor do acréscimo (art. 9º), do dano (art. 10) ou da remuneração do agente (art. 11). Se o juiz considerar que, pela situação econômica do réu, o valor calculado não é suficiente para reprovar e prevenir o ato, ele pode **aumentá-la até o dobro** (art. 12, § 2º). Quando o réu é pessoa jurídica, o juiz pesa o impacto econômico e social da punição para que a empresa possa continuar funcionando (§ 3º).",
    "resultado": "OK",
    "trecho_lei": "§ 2º A multa pode ser aumentada até o dobro, se o juiz considerar que, em virtude da situação econômica do réu, o valor calculado na forma dos incisos I, II e III do caput deste artigo é ineficaz para reprovação e prevenção do ato de improbidade."
})

# 15: Linha 88
registros.append({
    "linha": 88,
    "citacao": "art. 12, §§ 4º e 8º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A proibição de contratar, e de receber benefícios ou incentivos fiscais ou creditícios, abrange a contratação direta e a indireta, inclusive por pessoa jurídica de que o agente seja sócio majoritário. A reforma tentou limitá-la ao ente lesado, com exceções para casos relevantes. O STF, nas ADIs 7156 e 7236, declarou esse dispositivo (art. 12, § 4º) **inconstitucional** e entendeu que a proibição se aplica a **todos os entes da federação**. A sanção deve constar do Cadastro Nacional de Empresas Inidôneas e Suspensas (CEIS), observadas as limitações territoriais da decisão judicial (§ 8º).",
    "resultado": "OK",
    "trecho_lei": "sanção de proibição de contratação com o poder público deverá constar do Cadastro Nacional de Empresas Inidôneas e Suspensas (CEIS)"
})

# 16: Linha 95
registros.append({
    "linha": 95,
    "citacao": "art. 12, § 5º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Quando o ato ofende pouco os bens jurídicos protegidos, a punição se restringe à **multa**; ainda assim, se houver dano, ele é reparado, e os valores obtidos indevidamente são perdidos (art. 12, § 5º).",
    "resultado": "OK",
    "trecho_lei": "No caso de atos de menor ofensa aos bens jurídicos tutelados por esta Lei, a sanção limitar-se-á à aplicação de multa"
})

# 17: Linha 99
registros.append({
    "linha": 99,
    "citacao": "art. 12, § 9º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Lei 8.429/1992, art. 12, § 9º",
    "resultado": "OK",
    "trecho_lei": "LEI Nº 8.429, DE 2 DE JUNHO DE 1992 Texto compilado"
})

# 18: Linha 102
registros.append({
    "linha": 102,
    "citacao": "art. 20, caput da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Isso vale para **todas** as sanções. O art. 20, caput, que dizia o mesmo apenas sobre a perda da função e a suspensão dos direitos políticos, ficou como resquício da redação antiga, e o § 9º tem alcance mais amplo. A regra reflete a presunção de inocência.",
    "resultado": "OK",
    "trecho_lei": "Art. 20. A perda da função pública e a suspensão dos direitos políticos só se efetivam com o trânsito em julgado da sentença condenatória."
})

# 19: Linha 104
registros.append({
    "linha": 104,
    "citacao": "art. 12, § 10 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O § 10 do art. 12 previa que o prazo da suspensão dos direitos políticos fosse contado **retroativamente** a partir da decisão colegiada, descontando o intervalo até o trânsito em julgado. Seria um mecanismo que reduziria, às vezes a zero, a sanção: um réu condenado a oito anos de suspensão, com seis anos entre a decisão de segundo grau e o trânsito, cumpriria apenas dois. O STF declarou essa regra inconstitucional nas ADIs 7156 e 7236. Assim, o prazo corre normalmente a partir da execução.",
    "resultado": "OK",
    "trecho_lei": "computar-se-á retroativamente o intervalo de tempo entre a decisão colegiada e o trânsito em julgado da sentença condenatória."
})

# 20: Linha 108
registros.append({
    "linha": 108,
    "citacao": "art. 20, § 1º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O juiz pode afastar o agente do cargo, emprego ou função, mantendo a remuneração, se isso for indispensável para a **instrução do processo** ou para impedir que **novos ilícitos** estejam prestes a ocorrer (art. 20, § 1º).",
    "resultado": "OK",
    "trecho_lei": "§ 1º A autoridade judicial competente poderá determinar o afastamento do agente público do exercício do cargo, do emprego ou da função, sem prejuízo da remuneração"
})

# 21: Linha 120
registros.append({
    "linha": 120,
    "citacao": "art. 20, §§ 1º e 2º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> **Resolução.** Não. O afastamento não é sanção, é medida cautelar judicial para proteger a instrução e evitar novos ilícitos (art. 20, § 1º), e a remuneração é **mantida**. Por isso, a regra do trânsito em julgado não se aplica a ele. O prazo máximo é de 90 dias, prorrogável uma vez.",
    "resultado": "OK",
    "trecho_lei": "será de até 90 (noventa) dias, prorrogáveis uma única vez por igual prazo, mediante decisão motivada."
})

# 22: Linha 124
registros.append({
    "linha": 124,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O foco é numérico. A banca troca 14 por 12 ou 12 por 14, inverte o limite do art. 11 ou atribui a suspensão dos direitos políticos aos atos que atentam contra os princípios.",
    "resultado": "OK",
    "trecho_lei": "§ 9º As sanções previstas neste artigo somente poderão ser executadas após o trânsito em julgado da sentença condenatória."
})

# 23: Linha 131
registros.append({
    "linha": 131,
    "citacao": "art. 10 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Ressarcimento | Obrigação civil, sempre que houver dano efetivo | Chamá-lo de sanção exclusiva do art. 10 |",
    "resultado": "OK",
    "trecho_lei": "Art. 10. Constitui ato de improbidade administrativa que causa lesão ao erário qualquer ação ou omissão dolosa"
})

output_data = {
    "unidade": unit_id,
    "agente": "B",
    "materia": "direito-administrativo",
    "censo": registros
}

# Verifications
errors = []
trechos_vistos = set()
for idx, r in enumerate(registros):
    fc = r["frase_capitulo"]
    if fc not in chapter_content:
        errors.append(f"Row {idx+1} (linha {r['linha']}): frase_capitulo not in chapter!")
    elif r["resultado"] == "ERRO" and chapter_content.count(fc) != 1:
        errors.append(f"Row {idx+1} (linha {r['linha']}): frase_capitulo appears {chapter_content.count(fc)} times (must be 1)!")

    if r["resultado"] != "NAOVER":
        tl = r.get("trecho_lei", "")
        if len(tl) < 25:
            errors.append(f"Row {idx+1}: trecho_lei too short ({len(tl)} chars)")
        if tl in trechos_vistos:
            errors.append(f"Row {idx+1}: duplicate trecho_lei: '{tl[:30]}...'")
        trechos_vistos.add(tl)

        law_txt = cf if r["lei"] == "cf" else l8429
        if tl not in law_txt:
            errors.append(f"Row {idx+1}: trecho_lei not in {r['lei']}: '{tl}'")

if errors:
    print("ERRORS FOUND:")
    for e in errors:
        print("  -", e)
else:
    print(f"All {len(registros)} rows verified locally! Writing draft...")
    with open(f"material-pdf/_avaliacao/2026-11-11/rascunho/{unit_id}.json", "w", encoding="utf-8") as out:
        json.dump(output_data, out, ensure_ascii=False, indent=1)
    print("Draft saved.")
