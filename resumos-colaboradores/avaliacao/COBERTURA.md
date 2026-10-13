# Cobertura automática dos resumos (triagem)

Gerado por `pipeline/summary_coverage.py`. Mede omissão de termos específicos do texto-fonte; **não** detecta conceito errado. O veredito compara cada resumo com os da mesma disciplina. REFAÇÃO/REVISAR vão para leitura por agente ou pessoa, com a lista de termos que faltam como ponto de partida.

## REFAÇÃO (10)

| ID | Trecho | Agente | Cobertura | % do alvo | Termos que faltam (mais pesados) |
| --- | --- | --- | --- | --- | --- |
| S0542 | biologia/a14/s03 | CODEX-L3D | 0.41 | 23% | metros africa particulares minima rbma entorno tradicionais montanhas amortecimento oriental normativas deliberativo |
| S0539 | biologia/a15/s01 | CODEX-L3D | 0.43 | 24% | photos viroses jaboatao campanha flickr domesticos gratuitamente phil details aspx soropositiva dengue |
| S0554 | biologia/a13/s01 | CODEX-L3D | 0.44 | 25% | louva deus terciarios predados lago morta insetos formigas girinos formigueiro americas passaros |
| S0519 | biologia/a13/s07 | CODEX-L3D | 0.44 | 27% | caesalpinia aspidosperma 150 pilosocereus ceara bahia paraiba tuco arenosos mista pernambuco 200 |
| S0512 | biologia/a14/s01 | CODEX-BIO-3 | 0.47 | 27% | ilhas biogeografia ilha bioticos relevantes pragas morro diabo reducao teoria pasto nota |
| S0583 | fisica/a06/s01 | EXT-L5 | 0.46 | 23% | 180 houver cos180 06 diminua aparecer desnivel freada situacoes anteriormente podendo resumindo |
| S0275 | lingua-inglesa/a05/s02 | EXT-L2 | 0.31 | 28% | encontrou hadnt progressivo mion encontrei terminado marcos colocando tinha aconteceu verbal japones |
| S0708 | matematica/a15/s02 | EXT-L5 | 0.42 | 29% | pizza acoroa asetor praca pedacos aexternoainterno imagine voltaremos utilize segmento chamamos destacada |
| S0683 | quimica/a17/s02 | EXT-L6 | 0.42 | 29% | butil pentil isopropil buzina relacionado regras dimetil aciclicos pertencem isooctano trimetilpentano trimetil |
| S0661 | quimica/a06/s01 | EXT-L6 | 0.42 | 28% | trivalentes clo2 estanho sulfito clorito carbon mercurio divalentes bromato mono tetravalentes plumboso |

## REVISAR (68)

| ID | Trecho | Agente | Cobertura | % do alvo | Termos que faltam (mais pesados) |
| --- | --- | --- | --- | --- | --- |
| S0553 | biologia/a00/s01 | CODEX-L3B | 0.42 | 33% | vacina protetora prevencao gripe sars h1n1 covid19 corona chamou aegypti vetor redor |
| S0472 | direito-administrativo/a09/s05 | CODEX-L1 | 0.52 | 53% | prosperar ticio merece convola sair carlos surgimento aberto transforma abertura liquido suprimento |
| S0364 | direito-administrativo/a08/s03 | CLAUDE-L1 | 0.54 | 77% | cheque movida suframa resp 256 julgue mover movidas 676 ocasionou reaver lesoes |
| S0529 | direito-administrativo/a09/s09 | CODEX-L1 | 0.54 | 58% | grevista movimento negociacoes entraram 693 456 proceder demitidos gozar licito vocalizacao sustento |
| S0499 | direito-administrativo/a01/s01 | CODEX-L1 | 0.54 | 81% | ilha quiser separadas casa morar europeus deserta joao regidas desejar capitulo quisesse |
| S0530 | direito-administrativo/a09/s10 | CODEX-L1 | 0.56 | 44% | seletivo decimo acrescidas mara beta simplificado falecimentos anna procedente normais notadamente suprida |
| S0279 | direito-administrativo/a04/s05 | CLAUDE-L1 | 0.56 | 61% | acusado disse cessado loco abate 588322 visita renovacao debatido poderiamos argumentos energia |
| S0559 | direito-administrativo/a09/s08 | CODEX-L1 | 0.56 | 67% | julia sv13 joana quarto marido esconder 041 pressupor jorge 6655 210 federativo |
| S0046 | direito-constitucional/a04/s03 | CLAUDE-L1 | 0.57 | 59% | diarias normal assegurado higiene poucos dispensado dispensa cometer atribuidos grevista prevera fixara |
| S0203 | direito-constitucional/a02/s04 | CLAUDE-L1 | 0.58 | 85% | veiculo automotor dirigir usada colhida 63 dialogo 486 fisco subsidiar captacao nelson |
| S0061 | direito-constitucional/a08/s03 |  | 0.59 | 83% | 000 correspondera ordenar trezentos cinquenta quinhentos sete maximo ultrapassar maximos cento quarenta |
| S0182 | direito-constitucional/a03/s03 | CLAUDE-L1 | 0.59 | 82% | felipe battisti john cesare insuscetivel etapa armados magico infrator fugiu balao apenado |
| S0179 | direito-constitucional/a10/s02 | CLAUDE-L1 | 0.61 | 99% | 1994 886 371 039 trabalhos indio enfatize barbosa privilegio indiciados joaquim blocos |
| S0181 | direito-constitucional/a03/s02 | CLAUDE-L1 | 0.62 | 94% | preteritos vodca tras cominar sinal incriminadora confundi benigna 538 534 aquilo 2000 |
| S0113 | direito-constitucional/a08/s08 | CLAUDE-L1 | 0.63 | 100% | sacos portas virtual obrigue finalizado feira usuarios 139 caberao deixara relator extrai |
| S0162 | direito-constitucional/a02/s03 | CLAUDE-L1 | 0.63 | 86% | penetrar interior vigilia retratadas literarias inexigivel audiovisuais ingresso noturno ensejar livros desnecessaria |
| S0121 | direito-constitucional/a14/s01 | CLAUDE-L1 | 0.63 | 83% | solucionado assoalho assenta marques nunes wolfgang streck sarlet lenio ingo decorrer corolario |
| S0289 | direito-penal-militar/a00/s02 | CLAUDE-L4 | 0.44 | 93% | preservacao 216 regulares organizadas inquisa carlos pertencem passivos leitor elevacao compreendidos 9odocpm |
| S0267 | direito-penal-militar/a00/s01 | CLAUDE-L4 | 0.46 | 80% | docpm nestecaso veremos naopodemser naohamaisafiguradoassemelhado ematividade emalteracaoaleino14 ateoria respectivas inominado detalhes frente |
| S0346 | direito-penal-militar/a09/s02 | CLAUDE-L4 | 0.49 | 88% | cultural forcada incluido umterco desclassificacao grupo umaformaqualificadaemrazaodeaumentaroslimitesdaspenasminimae seoresultadofornaformagraveougravissima semparnocodigo seaquiverdadeiramodalidadepreterdolosa ominimoeomaximoeomesmocasofosseocasionadointencionalmentealgumdosresultados ojuizsopesarafavordoreunafixacaodapenabase |
| S0378 | direito-penal-militar/a09/s05 | CLAUDE-L4 | 0.53 | 88% | quatorze 217 829 oferecer resp porqualquer ouseavitimaemenorde18 afastada majoracao inocorrencia conviccao 236 |
| S0410 | estatistica/a02/s05 | CLAUDE-L4 | 0.34 | 47% | quilometros pp27 facant jogando etapa comecamos distancia determinando 77 filhos linf teatros |
| S0439 | estatistica/a04/s03 | CLAUDE-L4 | 0.34 | 59% | visualizacoes estaturas 166 158 162 154 revisao 184 mensais 200 170 registradas |
| S0401 | estatistica/a00/s03 | CLAUDE-L4 | 0.36 | 56% | 145 115 130 175190 175 85100 160175 145160 130145 115130 100115 quarta |
| S0382 | estatistica/a01/s02 | CLAUDE-L4 | 0.36 | 47% | delitos paraguaios 57300 xquim xmat quimica trimestre imigrantes sequencia 2009 demonstrar ocorridos |
| S0360 | estatistica/a03/s03 | CLAUDE-L4 | 0.37 | 50% | fpos presidiarios fant fpost dfmodfant 74 classificados projecao dfpos 5560 3555 2035 |
| S0454 | estatistica/a06/s05 | CLAUDE-L4 | 0.39 | 67% | imunizada 1000h atividade agropecuaria vara gratuidade carlos presente pagadores imunizado dose acoes |
| S0408 | estatistica/a06/s04 | CLAUDE-L4 | 0.39 | 60% | enfermeiro emprego enfermeiros contrair godel falhar homem russel ganham materia familia tuberculose |
| S0409 | estatistica/a02/s01 | CLAUDE-L4 | 0.40 | 46% | x251 satisfacao x250 atribuiram contendo 250 luis imediatamente nota vigesima emprestados avaliaram |
| S0513 | estatistica/a10/s04 | CLAUDE-L4 | 0.40 | 68% | 4999 4998 4997 4996 4995 4994 4993 4992 4991 4990 4989 4015 |
| S0598 | fisica/a11/s01 | EXT-L5 | 0.44 | 38% | vapor termometrica gelo termometro chumbo termologia 540cal chamamos suma termometricas relativas versara |
| S0616 | fisica/a13/s01 | EXT-L5 | 0.45 | 34% | nodo complexa identificar serve demonstracao abordado cair disso quisermos ordenada intermediario perceber |
| S0604 | fisica/a02/s01 | EXT-L5 | 0.45 | 38% | espacos horizonte 5400 policial responsavel previsivel historia conceito suposta aderbal viatura pessoa |
| S0211 | informatica/a06/s01 | EXT-L2 | 0.39 | 31% | powerpivot view quick fill analysis novidades escolherfuncao modelagem trouxe previsoes suite fortaleceu |
| S0209 | informatica/a00/s01 | EXT-L2 | 0.40 | 36% | quilometros comutacao metros extensa lans isolamento centenas proximidade dezenas paises wpan wman |
| S0191 | informatica/a02/s05 | EXT-L2 | 0.41 | 39% | resto investigacao dividendo digito boleto divisor maria digitos cadeado assinou verificador gente |
| S0240 | informatica/a12/s10 | EXT-L2 | 0.41 | 32% | apps dificuldades capturas idioma jogo jogos xbox game experiencias desejam lembretes chamadas |
| S0225 | informatica/a03/s06 | EXT-L2 | 0.42 | 33% | bradesco middle impulso desconfie enganar comercio ddos golpista falsa link site banking |
| S0206 | informatica/a14/s04 | EXT-L2 | 0.43 | 31% | board ruido prancheta pipoca aperta workstation palmtop netbook parou aquecimento alimentacao alto |
| S0239 | informatica/a12/s07 | EXT-L2 | 0.43 | 31% | multitarefas ativar distracoes sons desabilitar reunioes foco concentracao economia tecnicos adaptada exibidas |
| S0233 | informatica/a12/s05 | EXT-L2 | 0.43 | 32% | winkey pdfs aparece arredondadas abri modificacao tiradas players super marcar pasta edge |
| S0228 | informatica/a12/s12 | EXT-L2 | 0.43 | 33% | edificacoes pasta1 esvaziar contenham contrato excluidos excluir detalhe sugerido datemodified confirmacao intacto |
| S0230 | informatica/a02/s02 | EXT-L2 | 0.43 | 38% | carta requisito criticidade implica destinatario severidade append confiabilidade roubado chegou sinaliza negue |
| S0285 | lingua-espanhola/a05/s02 | EXT-L6 | 0.25 | 33% | jamais quica possivelmente ejemplosde retirados voltarei depressa trabalham provavelmente site locucoes ejemplode |
| S0326 | lingua-espanhola/a01/s02 | EXT-L6 | 0.32 | 43% | casas elaboracion principios cualquiera libre destacados deberes representantes relaciones publicos humanos almas |
| S0533 | lingua-espanhola/a00/s01 | EXT-L6 | 0.33 | 36% | britanicos islas resolucion respetar pueblos habitantes autodeterminacion 00 similar sentimientos derecho china |
| S0307 | lingua-espanhola/a11/s01 | EXT-L6 | 0.34 | 44% | lazpiur 1914 zapatos lisboa gipuzkoa cooperativismo 1970 producir auge jose clavos ligado |
| S0270 | lingua-inglesa/a06/s01 | EXT-L2 | 0.37 | 43% | menino fome relata muita relato disseram disse laura smartphones relatar relatado tinha |
| S0301 | lingua-inglesa/a01/s04 | EXT-L2 | 0.38 | 43% | moedas coins lidios ouro prata preditivas analises liga critico feitas jairo eram |
| S0035 | lingua-portuguesa/a10/s01 | EXT-L3 | 0.25 | 35% | catar feijao letargia colombo ticar flagrante janelas delicia obvia manzato atleta aplicativo |
| S0028 | lingua-portuguesa/a11/s03 | EXT-L3 | 0.28 | 40% | mamifero beleza alfabetos potencial musica violentamente repudiamos moralistas melindre atomicas feroz ataques |
| S0038 | lingua-portuguesa/a11/s02 | EXT-L3 | 0.38 | 42% | sopa colher sabao esfregar escova enxague colheres repousar aplique lustra inacabados ilha |
| S0029 | lingua-portuguesa/a09/s01 |  | 0.40 | 54% | bufalos saltos palmeiras ateniense ticar canta advento desorientaram paul mccartney retorica compositor |
| S0070 | lingua-portuguesa/a03/s02 |  | 0.41 | 46% | democratico climaticas icms terrestre vislumbrar entrelacamento satelites estadual limpas sete ecologicas gritar |
| S0031 | lingua-portuguesa/a03/s03 |  | 0.45 | 53% | atenas concorrencia tributacao custos referido setor confissao democracia eleitorado comercio 03 terriveis |
| S0680 | matematica/a17/s11 | EXT-L5 | 0.40 | 37% | variando 3cosx expiracao aspiracao trigonometrica tanx destaca variar completas percebe associa cosx |
| S0590 | matematica/a04/s01 | EXT-L5 | 0.41 | 37% | plantao p2t2 p1t1 durara alimentos alimentar 6000 acham p2m1 p1m2 facilitador complexidade |
| S0736 | matematica/a17/s09 | EXT-L5 | 0.41 | 56% | trigonometrico cosx2 desenvolvendo deveriamos ficariamos didaticos inedita extrapolando angulos fins simultanea cumpre |
| S0696 | matematica/a13/s01 | EXT-L5 | 0.42 | 35% | aplicaremos loga confortavel logax log24 log16 log1 050 decore logx243 log7 trabalhar |
| S0622 | matematica/a14/s03 | EXT-L5 | 0.42 | 34% | marinheiros nivel 1000 olhar informacao tender previsivel notificados 2046 novas 2048 1536 |
| S0735 | matematica/a17/s07 | EXT-L5 | 0.42 | 34% | formatos replementares possibilidades escrita solucao explementares 3tgx fora referentes extrapolar mostram ciclos |
| S0730 | matematica/a08/s03 | EXT-L5 | 0.43 | 40% | artificio 164 divisor 164x2 bhaskara demonstracao multiplo 1296 quarto delas voces 121 |
| S0603 | quimica/a12/s02 | EXT-L6 | 0.40 | 35% | semi 176 cortar somatorio trocar vizinhanca platos hformacao global cruza 46110 334 |
| S0657 | quimica/a18/s03 | EXT-L6 | 0.42 | 32% | petanol etanamida nulo virus aminoetil clorobutan pentanol oxopentanamida brilhante diol nitrocomposto organicas |
| S0723 | quimica/a03/s01 | EXT-L6 | 0.42 | 54% | 21bacl2 1c2h6 1na2co3 2o22co2 1mno2 acertar 1mncl2 vindo 1nh3 frente 03 o22co2 |
| S0698 | quimica/a04/s01 | EXT-L6 | 0.42 | 38% | acha otimo pergunta levara explorar perguntou ultima liquefazer cozinha aluminio unicas azuis |
| S0615 | quimica/a02/s03 | EXT-L6 | 0.43 | 32% | exercida fosforo exerce externos arrancar origem descemos luminol localizados niveis blindando positivas |
| S0587 | quimica/a14/s01 | EXT-L6 | 0.43 | 34% | semireacao voltagem sofrendo bateria comunicam noxs pecas ocorrera puxar 5no3 5no2 mnemonico |
