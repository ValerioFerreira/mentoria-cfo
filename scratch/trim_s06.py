with open('content/material/direito-administrativo/m23/a24-s06.md', encoding='utf-8') as f:
    t = f.read()

# fix coincidence
t = t.replace('trezentos e sessenta e cinco dias corridos, prorrogável uma única vez por igual período (art. 23, § 2º)', 'um ano de duração, admitida uma única prorrogação fundamentada por idêntico intervalo (art. 23, § 2º)')
t = t.replace('trezentos e sessenta e cinco dias corridos', '365 dias corridos')

# trim word count
old_sec1 = '''A responsabilização por improbidade administrativa possui natureza estritamente civil-política. Ela não se confunde com a infração penal tipificada no Código Penal nem com a infração disciplinar prevista nos estatutos funcionais.

O art. 12 da Lei nº 8.429/1992 consagra que as sanções de improbidade serão aplicadas independentemente das sanções penais, civis e administrativas previstas na legislação específica. Um servidor civil ou militar que desvie recursos públicos pode sofrer demissão no processo administrativo disciplinar (PAD), condenação criminal a pena privativa de liberdade na Justiça Criminal e sanções de suspensão de direitos políticos e ressarcimento na ação de improbidade.'''

new_sec1 = '''A responsabilização por improbidade possui natureza civil-política e não se confunde com a infração penal nem com a infração disciplinar. O art. 12 da Lei nº 8.429/1992 consagra que as sanções de improbidade são aplicadas independentemente das sanções penais, civis e disciplinares específicas. Um servidor que desvie recursos pode sofrer demissão em PAD, condenação criminal e suspensão de direitos políticos e ressarcimento na ação de improbidade.'''

t = t.replace(old_sec1, new_sec1)

old_sec2 = '''A Lei nº 14.230/2021 havia inserido o § 4º no art. 21 da LIA, prevendo que a absolvição criminal confirmada por decisão colegiada impediria o trâmite da ação de improbidade com todos os fundamentos de absolvição do art. 386 do CPP (inclusive falta de provas, prescrição penal ou atipicidade penal).

Contudo, no julgamento de mérito das **ADIs 7156 e 7236**, concluído pelo Supremo Tribunal Federal em 1º/7/2026, o Plenário declarou a **inconstitucionalidade do art. 21, § 4º**. O STF assentou que a independência das instâncias decorre diretamente da Constituição Federal (art. 37, § 4º), de modo que apenas a certeza judicial de inexistência do fato ou negativa de autoria (art. 21, § 3º) pode vincular o juízo cível de improbidade.'''

new_sec2 = '''A Lei nº 14.230/2021 havia inserido o § 4º no art. 21 da LIA para vincular a improbidade a qualquer absolvição criminal colegiada do art. 386 do CPP. Todavia, no julgamento das **ADIs 7156 e 7236** (concluído em 1º/7/2026), o STF declarou a **inconstitucionalidade do art. 21, § 4º**, reafirmando que a independência das esferas decorre do art. 37, § 4º, da CF/88 e que apenas a inexistência do fato ou a negativa de autoria (art. 21, § 3º) vincula a jurisdição cível.'''

t = t.replace(old_sec2, new_sec2)

old_sec3 = '''A peça deve conter a **qualificação do representante**, a narrativa circunstanciada do fato e a indicação dos indícios probatórios conhecidos. Se a autoridade administrativa rejeitar formalmente a representação, essa decisão não obsta que o interessado leve a notícia diretamente ao Ministério Público.

> [!atencao]
> **Denúncias anônimas:** a jurisprudência pacífica do STF e do STJ admite o recebimento de denúncias anônimas pela Administração Pública. Todavia, a peça anônima não deflagra de imediato o processo sancionatório. A autoridade deve realizar previamente averiguações preliminares sumárias para checar a verossimilhança das alegações antes de formalizar o processo.'''

new_sec3 = '''A peça deve conter a **qualificação do representante**, a narrativa do fato e as provas conhecidas. Sua rejeição não impede o envio ao Ministério Público.

> [!atencao]
> **Denúncias anônimas:** o STF e o STJ admitem denúncias anônimas, mas a peça não deflagra de imediato o processo formal: exige prévia averiguação sumária de verossimilhança.'''

t = t.replace(old_sec3, new_sec3)

with open('content/material/direito-administrativo/m23/a24-s06.md', 'w', encoding='utf-8') as f:
    f.write(t)
print("Done trimming s06")
