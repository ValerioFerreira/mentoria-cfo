import sys
p='scratch/draft_legpcpe.txt'
s=open(p,encoding='utf-8').read()
R=[
("A) a qualquer tempo, depois do estágio probatório e do enquadramento, a quem comprova nova titulação ou conclui pós-graduação reconhecida pelo MEC e relacionada às atividades do cargo.","A) a qualquer tempo, após o estágio probatório, a quem conclui pós-graduação reconhecida pelo MEC e relacionada ao cargo."),
("A) vedada, salvo para cargo em comissão compatível com as atribuições do cargo efetivo ou para a Assistência Policial Militar e Civil, com anuência do Secretário de Defesa Social.","A) vedada, salvo para cargo em comissão compatível ou para a Assistência Policial Militar e Civil, com anuência do Secretário."),
("O servidor policial civil prejudicado em seu enquadramento ou em sua progressão dispõe, segundo a Lei Complementar Estadual nº 137/2008, dos seguintes prazos:","Assinale a opção que apresenta os prazos de que dispõe o servidor policial civil prejudicado em seu enquadramento ou em sua progressão, segundo a Lei Complementar Estadual nº 137/2008."),
("A) É inválido, pois a remoção exige motivação que demonstre o interesse do serviço público, sendo vedada a relotação como punição disfarçada.","A) É inválido, pois a remoção exige motivação do interesse do serviço, sendo vedada como punição disfarçada."),
("A) A apuração das infrações penais pode ser compartilhada com particulares por meio de convênios de cooperação técnica.","A) A apuração penal pode ser compartilhada com particulares por convênio."),
("A) os brasileiros investidos em cargos exclusivos do quadro policial da Secretaria da Segurança Pública e, por equiparação, quem exerce cargo em comissão ou função gratificada de natureza policial.","A) os brasileiros investidos em cargos exclusivos do quadro policial e, por equiparação, em cargo em comissão ou função de natureza policial."),
("A) É inconstitucional toda modalidade de provimento que propicie ao servidor investir-se, sem concurso, em cargo que não integra a carreira na qual anteriormente investido.","A) É inconstitucional o provimento que permita investir-se, sem concurso, em cargo de outra carreira."),
("A) É permanente, podendo o candidato ser excluído até a nomeação se surgirem fatos incompatíveis com a idoneidade exigida, inclusive a omissão de informação relevante.","A) É permanente, podendo levar à exclusão do candidato até a nomeação se surgirem fatos incompatíveis com a idoneidade."),
("A) o chefe do serviço em que o policial está lotado deve explicar por escrito o motivo, e o policial perde os direitos e vantagens próprios das outras remoções.","A) o chefe do serviço deve justificar por escrito, e o policial perde as vantagens das outras remoções."),
("A) cobrir despesas médico-hospitalares decorrentes de ferimento ou acidente em serviço, atestado pelo chefe do órgão de lotação e homologado pelo Secretário da Segurança Pública.","A) cobrir despesas médico-hospitalares de ferimento ou acidente em serviço, homologado pelo Secretário da Segurança Pública."),
("A) trinta dias, com perda de vencimentos, podendo ser convertida em multa ou em detenção disciplinar.","A) trinta dias, com perda de vencimentos e possível conversão em multa."),
("A) tem natureza cautelar, não pressupõe culpa formada, dura até trinta dias prorrogáveis até noventa, e seus efeitos cessam após esse prazo ainda que o processo não esteja concluído.","A) tem natureza cautelar, não pressupõe culpa e dura até trinta dias, prorrogáveis até noventa."),
("A) doze meses, prorrogável apenas para concluir processos em fase avançada, com dedicação exclusiva e possibilidade de recondução.","A) doze meses, com dedicação exclusiva e possibilidade de recondução."),
("A) é acumulável com a pensão previdenciária e corresponde à remuneração do padrão imediatamente superior, somados o adicional de tempo de serviço e a gratificação de função policial.","A) é acumulável com a pensão previdenciária e equivale à remuneração do padrão imediatamente superior."),
("A) é honorífica, sem efeitos funcionais ou remuneratórios, e pode ser concedida a policiais e a personalidades externas que contribuíram para a causa policial.","A) é honorífica, sem efeitos funcionais ou remuneratórios, e pode ser dada a externos que contribuíram para a causa policial."),
]
def sw(t):
    return t[:3]+(t[3].lower() if t[3].isupper() else t[3].upper())+t[4:] if t.startswith('A) ') else t
for a,b in R:
    if s.count(a)!=1:
        a,b=sw(a),sw(b)
    if s.count(a)!=1: sys.exit('count %d: %s'%(s.count(a),a[:60]))
    s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
print('ok')
