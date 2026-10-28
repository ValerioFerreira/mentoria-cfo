import sys
p='scratch/draft_lpe.txt'
s=open(p,encoding='utf-8').read()
R=[
("A) equiparados a hediondos, pois a Constituição lhes dá o mesmo tratamento, embora não integrem o rol do art. 1º da Lei nº 8.072/1990.","A) equiparados a hediondos, embora não integrem o rol do art. 1º da Lei nº 8.072/1990."),
("A) É admissível, pois a vedação original afrontava a Constituição; a restrição da liberdade depende de decisão judicial fundamentada nos casos legais.","A) É admissível, e a prisão depende de decisão judicial fundamentada."),
("A) com restrição de liberdade da vítima, com arma de fogo e o qualificado pelo resultado lesão grave ou morte.","A) com restrição de liberdade, com arma de fogo e o qualificado pelo resultado."),
("A) trinta dias, prorrogáveis por igual período em caso de extrema e comprovada necessidade.","A) trinta dias, prorrogáveis por igual período."),
("A) A pena é cumprida inicialmente em regime fechado, mas o juiz deve fundamentar o regime, pois a obrigatoriedade absoluta foi declarada inconstitucional.","A) A pena é cumprida inicialmente em regime fechado, mas o juiz deve fundamentar o regime."),
("A) observar a inconstitucionalidade do art. 2º da Lei nº 8.072/1990, sem prejuízo de avaliar os requisitos objetivos e subjetivos, inclusive por exame criminológico fundamentado.","A) observar a inconstitucionalidade do art. 2º, sem prejuízo de avaliar requisitos objetivos e subjetivos."),
("A) de fazê-la sofrer, puni-la ou controlá-la, em contexto de violência doméstica e familiar.","A) de fazê-la sofrer, puni-la ou controlá-la."),
("A) retenção, subtração ou destruição de objetos, documentos, bens, valores e direitos ou recursos econômicos da mulher.","A) retenção, subtração ou destruição de bens, documentos e recursos econômicos da mulher."),
("A) preservar sua integridade física, psíquica e emocional, evitar contato direto com o investigado e não revitimizá-la com inquirições sucessivas sobre o mesmo fato.","A) preservar sua integridade, evitar contato com o investigado e não revitimizá-la."),
("A) perante o juiz, em audiência designada para essa finalidade, antes do recebimento da denúncia e ouvido o Ministério Público.","A) perante o juiz, em audiência especial, antes do recebimento da denúncia."),
("A) vedada a aplicação de pena de cesta básica ou outra de prestação pecuniária, bem como a substituição que resulte no pagamento isolado de multa.","A) vedada a pena de cesta básica ou outra prestação pecuniária e a substituição por multa isolada."),
("A) decidir sobre as medidas protetivas, encaminhar a ofendida à assistência judiciária, comunicar o Ministério Público e determinar a apreensão imediata de arma de fogo do agressor.","A) decidir sobre as medidas, encaminhar a ofendida à assistência judiciária e comunicar o Ministério Público."),
("A) por decisão de seu representante legal ou contratual, ou de órgão colegiado, no interesse ou benefício da entidade.","A) por decisão de seu representante legal ou de órgão colegiado, no interesse da entidade."),
("A) sob termo de compromisso e responsabilidade de apresentá-lo ao Ministério Público no mesmo dia ou no primeiro dia útil seguinte.","A) sob termo de compromisso e responsabilidade perante o Ministério Público."),
("A) Configura-se mesmo sem repassar o material, tendo pena de 3 a 6 anos de reclusão e multa.","A) Configura-se mesmo sem repassar o material; pena de 3 a 6 anos."),
]
for a,b in R:
    if s.count(a)!=1: sys.exit('count %d: %s'%(s.count(a),a[:60]))
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s); print('ok')
