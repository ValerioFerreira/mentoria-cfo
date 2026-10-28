##### informatica/a13/s01
Este trecho (incidência altíssima) define computação em nuvem, mostra sua principal vantagem (redução de custos) e detalha as cinco características essenciais definidas pelo NIST, com as diferenças entre escalabilidade e elasticidade e entre autosserviço e elasticidade.

### Conceito: o que é a nuvem

- "Nuvem" é uma **metáfora para a Internet**: o desenho de uma nuvem sempre representou, nos diagramas de rede, primeiro a rede telefônica e depois a Internet, escondendo a infraestrutura (servidores, redes, centros de dados). Nada fica literalmente "dentro de uma nuvem".
- **Computação em nuvem** é um conjunto de recursos virtuais, facilmente utilizáveis e acessíveis, como hardware, plataformas de desenvolvimento, serviços, data centers e servidores distribuídos pelo mundo, oferecidos pela Internet. É um modelo de acesso via rede, **onipresente, conveniente e sob demanda**, a recursos configuráveis (redes, servidores, armazenamento, aplicações e serviços), em geral com preço conforme o uso.
- O usuário, de qualquer lugar, com qualquer sistema operacional e dispositivo, usa os recursos da Internet como se estivessem instalados na própria máquina. Muitas aplicações são acessadas por navegador.
- O **NIST** (agência americana de padrões) publicou em 2011 o documento de referência adotado por concursos: **5 características essenciais, 3 modelos de serviço e 4 modelos de implantação** (tipos de nuvem).

### Principal vantagem: redução de custos

- Antes, a empresa mantinha um **Centro de Processamento de Dados (CPD, ou data center)** próprio, com servidores, segurança, redundância, refrigeração, equipe 24 horas por dia e compra constante de equipamentos. Com a nuvem, terceiriza tudo isso a um provedor remoto.
- Outras vantagens: libera espaço físico, reduz consumo de energia e folha de pagamento, transfere a responsabilidade pela manutenção ao provedor, otimiza recursos; os preços tendem a cair com a concorrência. Também serve a pessoas físicas.
- Exemplo: o Office 365 é o pacote Office como serviço por assinatura mensal (cerca de R$ 30, no exemplo), sempre atualizado, acessível por navegador em qualquer sistema, com trabalho colaborativo no mesmo arquivo; pode também ser instalado em até cinco computadores (isso, em si, não é nuvem).
- Em regra, na nuvem o armazenamento, a atualização, o backup e a manutenção da aplicação são **responsabilidade do provedor, não do usuário**.
- Despesa de capital (comprar equipamento) dá lugar a despesa operacional: paga-se pelo que se usa.

### As cinco características essenciais (NIST)

| Característica | Ideia central |
| --- | --- |
| Autosserviço sob demanda (*on-demand self-service*) | O usuário provisiona recursos por conta própria, sem interação humana com o provedor |
| Amplo acesso à rede (*broad network access*) | Recursos disponíveis pela rede e acessados por mecanismos padronizados, por plataformas heterogêneas (celular, tablet, notebook, IoT) |
| Agrupamento de recursos (*resource pooling*) | Recursos físicos e virtuais agrupados para vários consumidores (multi-tenant) e realocados conforme a demanda |
| Elasticidade rápida (*rapid elasticity*) | Aumentar ou reduzir recursos quase instantaneamente e de forma automática |
| Serviço mensurado (*measured service*) | O uso é monitorado, controlado e reportado, com cobrança proporcional |

1. **Autosserviço sob demanda**: com alguns cliques em um portal ou por API, o usuário ativa máquinas virtuais, amplia armazenamento, cria bancos de dados; não abre chamado nem espera aprovação do provedor. Exemplo: aumentar sozinho a cota do Google Drive de 50 GB para 200 GB. Analogia: máquina de refrigerantes.
2. **Amplo acesso à rede**: baseia-se em protocolos abertos (como HTTP/HTTPS) e dá acesso por celular, tablet, notebook, desktop e sensores IoT. É a base do home office e da educação online. O nome em inglês às vezes é mal traduzido como "acesso por banda larga", "ampla disponibilidade" ou "acesso à rede ubíqua". Analogia: tomada de energia.
3. **Agrupamento de recursos**: modelo de **multi-tenancy** (vários clientes dividindo a mesma infraestrutura, mas isolados, como apartamentos em um prédio). O usuário não sabe a localização exata dos recursos, mas pode definir uma localização em nível alto (país, estado, região ou datacenter). Permite balancear cargas, manter alta disponibilidade e dá base à escalabilidade e à elasticidade. A virtualização e a criptografia garantem o isolamento. Analogia: piscina compartilhada (*pool*).
4. **Elasticidade rápida**: expandir e reduzir recursos conforme a demanda, de forma automática e quase imediata (por exemplo, loja virtual na Black Friday). Evita manter servidores ociosos e pagar por capacidade sem uso; torna o sistema mais resiliente a picos. Analogia: elástico da calça.
5. **Serviço mensurado**: o sistema mede o consumo (armazenamento, processamento, largura de banda, contas ativas, requisições a API), o que permite pagar só o que se usou, dá transparência a provedor e cliente (painéis em tempo real) e ajuda a otimizar o uso. Analogia: hidrômetro. É a base do modelo pagar por uso.

### Escalabilidade x elasticidade e autosserviço x elasticidade

- **Escalabilidade**: capacidade de aumentar ou diminuir recursos para atender a mudanças de demanda, com **planejamento**, de longo prazo. Pode ser **vertical** (mais CPU ou memória em um servidor) ou **horizontal** (mais servidores). Exemplo: ampliar servidores antes de uma promoção.
- **Elasticidade**: alocar e liberar recursos **dinamicamente e de forma automática** para variações **imprevisíveis** e repentinas. Exemplo: site de notícias que ganha recursos durante uma notícia de última hora e os devolve depois.
- **Autosserviço x elasticidade**: no autosserviço, **quem inicia a ação é o usuário** (cria manualmente um servidor no console); na elasticidade, **quem age é o próprio sistema**, por regras e métricas (cria instâncias sozinho ao subir o tráfego).

> ⚠️ Pegadinha: as cinco características formam o pacote do NIST. Afirmar que o usuário precisa cuidar do backup da aplicação na nuvem, ou que a nuvem exige contato humano com o provedor para cada recurso, está errado.

### Para fixar

- Nuvem é metáfora para a Internet; a principal vantagem é a redução de custos (no lugar de CPD próprio, equipe e equipamentos).
- O NIST define 5 características essenciais, 3 modelos de serviço e 4 modelos de implantação.
- Autosserviço sob demanda: o usuário provisiona recursos sem interação humana com o provedor.
- Amplo acesso à rede: acesso por mecanismos padronizados e dispositivos heterogêneos; agrupamento de recursos: multi-tenant, localização só em nível alto.
- Elasticidade rápida: expande e reduz automaticamente conforme a demanda; serviço mensurado: uso medido e cobrado proporcionalmente.
- Escalabilidade é planejada (vertical ou horizontal); elasticidade é automática e para variações imprevisíveis.
- No autosserviço o usuário age; na elasticidade o sistema age.

