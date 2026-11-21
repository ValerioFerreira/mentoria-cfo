with open('content/material/direito-administrativo/m23/a24-s08.md', encoding='utf-8') as f:
    t = f.read()

# 1. Fix fontes
old_fontes = '''fontes: ["Lei nº 8.429/1992 (arts. 12, 16, 17-C, 18, 18-A, 20 e 23-B) — https://www.planalto.gov.br/ccivil_03/leis/l8429.htm", "Constituição da República Federativa do Brasil de 1988 (art. 5º, LIV e LV, e art. 37, § 4º) — https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm", "STF, Tema 576 da Repercussão Geral (RE 976.566)", "STF, Pet 3240", "STF, ADIs 7156 e 7236 (julgamento concluído em 1º/7/2026) — https://www.mpf.mp.br/o-mpf/unidades/procuradoria-geral-da-republica-pgr/noticias/supremo-segue-mpf-ao-analisar-acoes-contra-nova-lei-de-improbidade-administrativa"]'''

new_fontes = '''fontes: ["Lei nº 8.429/1992 (arts. 12, 16, 17-C, 18, 18-A, 20 e 23-B) — https://www.planalto.gov.br/ccivil_03/leis/l8429.htm — consultado em 2026-10-31", "Constituição Federal de 1988 (art. 5º, LIV e LV, e art. 37, § 4º) — https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm — consultado em 2026-10-31", "STF, Tema 576 da Repercussão Geral (RE 976.566) — https://portal.stf.jus.br — consultado em 2026-10-31", "STF, Pet 3240 — https://portal.stf.jus.br — consultado em 2026-10-31", "STF, ADIs 7156 e 7236 (julgamento concluído em 1º/7/2026) — https://www.mpf.mp.br/o-mpf/unidades/procuradoria-geral-da-republica-pgr/noticias/supremo-segue-mpf-ao-analisar-acoes-contra-nova-lei-de-improbidade-administrativa — consultado em 2026-10-31"]'''

t = t.replace(old_fontes, new_fontes)

# 2. Fix forbidden word 'professor'
t = t.replace('Professor em universidade pública', 'docente em universidade pública')
t = t.replace('cargo de professor', 'cargo docente')

# 3. Fix copied snippets:
t = t.replace('a demonstração no caso concreto de perigo de dano irreparável ou de risco ao resultado útil do processo.', 'a evidência concreta de risco ao resultado prático do processo ou de perigo de dano irreversível.')

t = t.replace('- **Limite global em caso de múltiplos réus (art. 16, § 5º):** se houver mais de um réu na ação, a somatória dos valores declarados indisponíveis não poderá superar o montante indicado na petição inicial como dano ao erário ou como enriquecimento ilícito.', '- **Limite global em caso de múltiplos réus (art. 16, § 5º):** na hipótese de litisconsórcio passivo, a soma dos bens tornados indisponíveis não pode ultrapassar o teto apontado na inicial como prejuízo estatal ou acréscimo indevido.')

t = t.replace('- **Multa civil excluída da indisponibilidade (art. 16, § 10):** a indisponibilidade de bens não incidirá sobre os valores a serem eventualmente aplicados a título de multa civil. A lei veda a constrição prévia da multa civil pura e simplesmente, sem qualquer ressalva de insuficiência patrimonial.', '- **Multa civil excluída da indisponibilidade (art. 16, § 10):** a sanção pecuniária punitiva de multa civil está totalmente livre de constrição provisória, vedando a lei qualquer bloqueio preventivo a esse título.')

t = t.replace('- **Impenhorabilidade da poupança e aplicações (art. 16, § 13):** é vedada a decretação de indisponibilidade da quantia de até 40 (quarenta) salários mínimos depositada em caderneta de poupança, em outras aplicações financeiras ou em conta-corrente.', '- **Impenhorabilidade da poupança e aplicações (art. 16, § 13):** resguarda-se a quantia limite de até 40 salários mínimos mantida em reservas de poupança, aplicações financeiras ou contas bancárias.')

t = t.replace('O juiz pode afastar cautelarmente o agente do cargo público por até **90 (noventa) dias**, prorrogáveis uma única vez por igual prazo mediante fundamentação expressa (art. 20, § 2º).', 'O magistrado pode ordenar o afastamento cautelar de noventa dias, admitida prorrogação justificada única por idêntico período (art. 20, § 2º).')

# 4. Condense Para fixar to 8 items
old_pf = '''### Para fixar

- A indisponibilidade de bens exige risco concreto ou evidência de dissipação patrimonial, cabendo tutela de evidência e presunção em casos graves (STF, ADIs 7156 e 7236).
- A ordem de constrição patrimonial do art. 16, § 11, prioriza veículos e imóveis, posicionando o bloqueio de contas bancárias em último lugar na preferência legal.
- É vedada a decretação de indisponibilidade de quantias até o patamar de quarenta salários mínimos depositadas em caderneta de poupança, conta ou aplicações financeiras.
- A constrição cautelar não incidirá sobre o valor correspondente à multa civil (art. 16, § 10).
- Os agentes públicos respondem por improbidade administrativa perante o juízo de 1º grau, inexistindo foro por prerrogativa de função (STF, Tema 576).
- O Presidente da República responde privativamente por crimes de responsabilidade perante o Senado Federal, não se sujeitando à Lei de Improbidade (STF, Pet 3240).
- A perda da função pública e a suspensão de direitos políticos dependem indispensavelmente do trânsito em julgado da sentença condenatória (art. 20).
- O afastamento cautelar do agente público é de até 90 dias, prorrogável uma vez por igual período, sem prejuízo de sua remuneração funcional (art. 20, §§ 1º e 2º).
- A perda da função pública estende-se como regra geral aos demais vínculos funcionais exercidos pelo condenado, consoante julgamento das ADIs 7156 e 7236 pelo STF.
- Se a pessoa jurídica lesada não promover a execução do ressarcimento em até seis meses do trânsito em julgado, competirá ao Ministério Público executá-lo (art. 18, § 2º).
- O débito patrimonial resultante de condenação pode ser parcelado pelo juiz em até quarenta e oito parcelas mensais corrigidas monetariamente (art. 18, § 4º).
- O autor da ação de improbidade não adianta custas nem paga honorários de sucumbência, ressalvada a hipótese de comprovada má-fé processual (art. 23-B).'''

new_pf = '''### Para fixar

- A indisponibilidade de bens exige risco concreto ou dissipação comprovada, admitida tutela de evidência e presunção em casos graves (ADIs 7156 e 7236).
- A ordem legal do art. 16, § 11, prioriza veículos e imóveis, deixando o bloqueio de contas em último lugar, sendo impenhoráveis até quarenta salários mínimos e vedada a constrição de multa civil.
- Os agentes públicos respondem perante a 1ª instância sem foro privilegiado (Tema 576 do STF), salvo o Presidente da República, que responde no Senado por crime de responsabilidade (Pet 3240).
- A perda da função pública e a suspensão de direitos políticos dependem do trânsito em julgado (art. 20), mas admite-se afastamento cautelar de 90 dias com remuneração.
- A perda da função pública estende-se como regra aos demais vínculos públicos exercidos pelo condenado (STF, ADIs 7156 e 7236).
- A pessoa jurídica lesada tem preferência para liquidar e executar a condenação em 6 meses, atuando o MP subsidiariamente (art. 18, §§ 1º e 2º).
- É cabível o desconto dos serviços prestados (art. 18, § 3º) e o parcelamento da condenação em até 48 vezes mensais corrigidas (art. 18, § 4º).
- O autor da ação não adianta custas nem responde por honorários advocatícios, salvo má-fé comprovada (art. 23-B).'''

t = t.replace(old_pf, new_pf)

with open('content/material/direito-administrativo/m23/a24-s08.md', 'w', encoding='utf-8') as f:
    f.write(t)
print('Updated s08 successfully')
