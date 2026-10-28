# Handoff — pagamentos do Mercado Pago

**Projeto:** Missão Mentoria (`web/` no repositório CFO-BM)  
**Atualizado em:** 12/10/2026  
**Estado:** integração implementada no código; incidente de webhook HTTP 502 em produção ainda sem causa-raiz comprovada.

## 1. Resumo executivo

O projeto tem três caminhos de cobrança:

1. **Acesso permanente — R$ 50, pagamento único:** Checkout Pro por meio da API de preferências (`POST /checkout/preferences`).
2. **Assinatura mensal — R$ 30/mês:** fluxo de assinatura/preapproval (`POST /preapproval`), com cobrança recorrente.
3. **PIX para acesso permanente — R$ 50:** pagamento criado diretamente pela API (`POST /v1/payments`, `payment_method_id: pix`), com QR Code e código copia-e-cola.

O backend não libera acesso pelo retorno do navegador nem pelo nome do evento recebido. Para pagamentos, consulta o recurso autenticado no Mercado Pago, valida o vínculo com uma compra local e confere valor e moeda. A aplicação persiste pagamentos e eventos para manter histórico e lidar com notificações repetidas.

Em 12/10/2026, o painel do Mercado Pago mostrou uma falha HTTP 502 na entrega do evento `payment.created`, recurso `182791299055`, às 19:39:48 UTC. **A causa do 502 e o estado atual desse pagamento continuam desconhecidos:** não havia acesso autenticado aos logs de produção da Vercel nem credencial do Mercado Pago no ambiente local. Não fazer deploy ou declarar o incidente resolvido até obter essas evidências e validar a entrega real.

## 2. Histórico da implementação e decisões

- O código da integração Checkout Pro, assinaturas, webhooks e tela de planos está no commit `264dc5d` (`feat(billing): mercado pago checkout, webhooks and plans integration`).
- O checkout direto por PIX e a tela do QR Code/copia-e-cola estão no commit `50f1f92` (`feat(billing): checkout direto via Pix do Mercado Pago com tela de QR Code e copia-e-cola`).
- No estado deste handoff, esses commits aparecem na branch local `codex/mercadopago-integration` e também em `origin/main`. Isso **não comprova** qual deployment está ativo na Vercel nem se as migrações já foram aplicadas em produção.
- No histórico anterior da tarefa consta que houve um deploy direto da integração inicial pela Vercel. Nesta investigação não foi possível confirmar o deployment atual, seu commit, ou se o PIX foi incluído no deployment de produção.
- A regra de autorização aprovada pelo responsável foi: cancelamento mensal interrompe cobranças futuras e mantém acesso até o período pago; falha de renovação não concede período extra; estorno total revoga a compra afetada; estorno parcial mantém acesso; contestação em análise não revoga automaticamente, perda revoga e vitória preserva; acesso permanente é independente da assinatura, mas estorno/perda de contestação da própria compra permanente revoga esse direito.
- Foi mantida a página de pagamentos atual, com as opções de mensalidade, acesso permanente e PIX. O retorno do checkout é apenas informativo; não concede acesso.
- Na tentativa anterior de testar o Checkout Pro, o responsável relatou a mensagem do Mercado Pago: “Uma das partes com as quais você está tentando efetuar o pagamento é de teste.” A hipótese mais compatível foi incompatibilidade de ambiente/conta compradora/cartão. Não foi possível capturar a sessão do checkout nem confirmar a configuração atual da Vercel; nenhum botão foi habilitado artificialmente e nenhuma credencial foi alterada.

## 3. Arquitetura e arquivos relevantes

### Página, início e retorno do checkout

- `web/src/app/(public)/pagamentos/page.tsx`: apresenta os planos, o estado das compras e as opções de pagamento.
- `web/src/app/(public)/pagamentos/retorno/page.tsx`: informa que o pagamento está em confirmação. Não ativa acesso.
- `web/src/app/(public)/pagamentos/pix/[purchaseId]/page.tsx`: apresenta as instruções do PIX.
- `web/src/lib/billing/actions.ts`: inicia checkout Pro, assinatura, PIX e cancelamento mensal. Valores definidos no servidor: R$ 30 mensal e R$ 50 permanente. O checkout guarda IDs e referências locais; no PIX, grava QR/copia-e-cola e o pagamento.

### API, autorização e notificações

- `web/src/lib/billing/mercado-pago.ts`: chamadas HTTP ao host `https://api.mercadopago.com`, autenticação Bearer, validação HMAC da assinatura do webhook e resolução da URL pública.
- `web/src/app/api/webhooks/mercadopago/route.ts`: endpoint `POST /api/webhooks/mercadopago`; recebe pagamento, assinatura, pagamento autorizado e contestação/chargeback; consulta o recurso e persiste seu estado.
- `web/src/lib/billing/status.ts`: mapeia estados do Mercado Pago para estados internos.
- `web/src/lib/billing/access.ts`: decide se uma compra concede acesso, usando status e período de pagamento.
- `web/src/app/api/webhooks/mercadopago/route.test.ts`: testes adicionados durante a investigação do 502. Usa mocks; não chama o Mercado Pago ou banco reais.
- Testes relacionados existentes: `web/src/lib/billing/mercado-pago.test.ts`, `web/src/lib/billing/status.test.ts` e `web/src/lib/billing/access.test.ts`.

### Banco e migrações

As tabelas/modelos principais são `BillingPurchase`, `BillingPayment`, `BillingDispute` e `BillingWebhookEvent`, definidos em `web/prisma/schema.prisma`.

- `20261012120000_mercado_pago_billing`: tabelas e estados iniciais de compra, pagamento e evento.
- `20261012130000_billing_payment_states`: estados para estorno parcial e contestação.
- `20261012130100_billing_access_policy`: períodos pagos, estado da contestação e normalização dos registros legados.
- `20261012140000_billing_pix_checkout`: identificador e dados do PIX.

O script `npm run build` **não é apenas compilação**: executa `prisma migrate deploy`, `tsx prisma/seed-structure.ts` e `next build`. Não o use para uma validação local sem confirmar antes a conexão e o efeito do banco. Para validar somente o build Next local, foi usado `npx next build`.

## 4. Variáveis de ambiente e segurança

O código lê estes nomes no servidor:

| Variável | Uso |
| --- | --- |
| `MERCADOPAGO_ACCESS_TOKEN` | Token de API preferido. |
| `MERCADO_PAGO_ACCESS_TOKEN` | Nome alternativo legado; usado se o nome preferido não existir. |
| `MERCADOPAGO_WEBHOOK_SECRET` | Segredo HMAC para validar `x-signature`. Deve corresponder à aplicação e configuração de Webhooks do ambiente ativo. |
| `MERCADOPAGO_SELLER_ID` | `X-Caller-Id` na consulta de chargeback. Necessário para esse caminho. |
| `APP_URL` | URL base preferida para retorno e notificações. |
| `SITE_URL` | Fallback para a URL base. |
| `VERCEL_PROJECT_PRODUCTION_URL` | Fallback adicional, com HTTPS. |

`MERCADO_PAGO_PUBLIC_KEY` não é usada por esse fluxo server-side atual. Não registrar nem compartilhar valores de tokens, segredo de webhook, strings de conexão, cookies ou dados de cartão. O endpoint usa a API de produção do Mercado Pago; a compatibilidade entre credenciais, conta vendedora e compradora deve ser confirmada no painel sem revelar os valores.

Na investigação local de 12/10, os arquivos de ambiente do projeto não apresentaram as variáveis de token/segredo do Mercado Pago; a Vercel não estava autenticada por CLI. Não copiar credenciais para o repositório para contornar essa limitação.

## 5. Fluxo atual do webhook

1. Lê `data.id` da query (com fallback legado para `id`) e valida HMAC usando `x-signature`, `x-request-id`, o ID e `MERCADOPAGO_WEBHOOK_SECRET`.
2. Lê o JSON e, se `data.id` também vier no corpo, rejeita divergência entre corpo e query.
3. Usa o ID assinado para consultar a API autenticada (`GET /v1/payments/{id}`; ou o endpoint correspondente para assinatura, pagamento autorizado ou chargeback). O corpo da notificação não é considerado prova do estado financeiro.
4. Localiza a compra por ID de assinatura, `metadata.purchase_id` ou `external_reference`; exige valor esperado (30 ou 50) e moeda `BRL`.
5. Mapeia o estado real, grava `BillingPayment` com `upsert` e atualiza compra em transação de banco. O pagamento usa `providerPaymentId` único.
6. Grava `processedAt` e resultado no evento somente após a persistência. Se consulta ou persistência falhar, retorna 500 e deixa o evento sem marca de sucesso, permitindo que a entrega seja repetida.
7. Se a mesma chave de evento já foi processada, responde 200 sem refazer consultas/escritas.

Respostas explícitas atuais: assinatura inválida → 401; JSON/ID inconsistente → 400; evento processado/repetido → 200; falha de processamento capturada → 500. O código não emite 502 diretamente. Um 502 pode ser retornado pela infraestrutura por erro de execução, interrupção ou timeout, mas isso só pode ser afirmado após examinar os logs da invocação.

## 6. Regras atuais de estado e acesso

- Pagamento `approved` só ativa uma compra se corresponder à compra local e tiver valor/moeda esperados.
- `pending`, `in_process` e `authorized` ficam pendentes; `rejected` é registrado sem ativar compra permanente. O pagamento rejeitado de mensalidade marca a compra como `PAST_DUE`.
- `cancelled` e `refunded` são estados distintos; estorno total da compra permanente altera sua compra para `REFUNDED`.
- `partially_refunded`, `in_mediation`/`charged_back` em análise e disputa ganha mantêm acesso conforme a política; contestação perdida revoga o acesso permanente associado.
- O acesso mensal depende de pagamento elegível com `accessUntil` futuro. A data é calculada a partir da data aprovada do pagamento, não da chegada de um webhook potencialmente atrasado.
- O cancelamento da assinatura usa `PUT /preapproval/{id}` e só marca cancelada localmente após a confirmação da API. O fim do período já pago é avaliado separadamente pelo pagamento e seu `accessUntil`.
- Repetições são protegidas por `BillingWebhookEvent.eventKey` único e `BillingPayment.providerPaymentId` único. As atualizações são feitas via `upsert`/transações.

## 7. Incidente HTTP 502 em produção

**Relato do painel Mercado Pago:**

- Ambiente: produção.
- Evento: `payment.created` (`type: payment`).
- Recurso: pagamento `182791299055`.
- Horário: 12/10/2026, 19:39:48 UTC (16:39:48 em Recife).
- Endpoint esperado: `https://missaomentoria.com.br/api/webhooks/mercadopago`.
- Resultado de entrega: HTTP 502.

**O que foi verificado:**

- Auditoria estática do handler e dependências descritos acima.
- Confirmação de que a busca do pagamento é feita pelo ID do recurso e que o acesso depende do estado consultado, valor, moeda e vínculo local.
- Testes novos de integração unitária do handler para assinatura inválida, pagamento aprovado, pendente, em processo e recusado, duplicidade, falha de API, falha de persistência/retry e valor divergente.
- Não foi consultado nem reprocessado o pagamento de produção. Nenhuma cobrança foi criada.
- Não houve acesso à linha de log da Vercel, ao status de deployment no horário, à resposta real da API do Mercado Pago nem ao estado do banco para este pagamento. Portanto, **não existe causa-raiz comprovada e o incidente permanece aberto**.

**Limitações específicas encontradas:**

- `vercel` CLI não está instalado/autenticado nesta sessão; não há conector de Vercel disponível.
- Nenhum token/segredo do Mercado Pago está presente nos arquivos locais do projeto. O responsável não deve enviar esses segredos no chat; a consulta deve ocorrer em ambiente autorizado ou ser feita por um colaborador com acesso seguro.
- A rota registra erros de processamento com tópico, ID do recurso e mensagem de erro; não registra token nem corpo bruto da notificação. `mpRequest` não expõe o corpo de erro da API, apenas status HTTP. Assim, os logs podem indicar o erro interno, mas uma falha de API pode exigir correlação com logs de resposta do provedor ou consulta autenticada.

**Dados que o próximo colaborador deve obter:**

1. Na Vercel, projeto `mentoria-cfo` → Logs/Observability; selecionar **Production** e a janela `2026-10-12 19:39:40–19:40:00 UTC`; filtrar a rota `/api/webhooks/mercadopago` e incluir o status, request/invocation ID, deployment associado, região/duração e mensagens completas da função/erro de runtime. Se não aparecer no filtro de 20 segundos, ampliar a busca alguns minutos em torno de 19:39:48 UTC.
2. Conferir se a entrada de request chegou à função, se há log `[billing-webhook] Event processing failed`, erro de inicialização, encerramento forçado, timeout ou falha de conexão. Comparar status registrado pela plataforma com o 502 mostrado no Mercado Pago.
3. Consultar o pagamento com `GET /v1/payments/182791299055` usando o token de produção, sem compartilhar o token. Registrar apenas estes campos não secretos: `id`, `status`, `status_detail`, `transaction_amount`, `currency_id`, `external_reference`, `metadata.purchase_id`, `live_mode`, `date_created`, `date_approved` e `collector_id`. Não alterar o pagamento.
4. Correlacionar o pagamento com a compra (`externalReference` ou `metadata.purchase_id`) e registros `BillingWebhookEvent`/`BillingPayment` no banco. Se houver falha e evento não processado, decidir reprocessamento seguro a partir do estado atual consultado, sem editar manualmente status para `APPROVED`.
5. Depois da correção sustentada pelos logs, executar testes, publicar por fluxo aprovado, usar o simulador de Webhooks do Mercado Pago contra a URL pública e confirmar resposta 200 e registro persistido. Reconsultar o pagamento real para determinar se o evento histórico ainda precisa de retry; não fazer nova cobrança.

Compartilhar/exportar os logs com tokens, cookies, cabeçalhos de autorização, e-mails e dados pessoais removidos. A [CLI de logs da Vercel](https://vercel.com/docs/cli/logs) documenta filtros por ambiente, status, request ID, deployment e intervalo de tempo.

## 8. Validação feita nesta sessão

Na investigação do incidente, foi criado `web/src/app/api/webhooks/mercadopago/route.test.ts`. A suíte completa terminou com **417 testes em 39 arquivos aprovados**. Também passaram ESLint nos arquivos relacionados, `npm run typecheck` e `npx next build`.

O build foi local; não aplicou migrações, não fez seed, não publicou e não chamou o Mercado Pago. Os testes do endpoint usam mocks, portanto validam o fluxo local de código, não credenciais/assinatura de produção, disponibilidade do banco remoto ou entrega real do Mercado Pago. Nenhum teste executou cobrança.

## 9. Pontos de atenção e trabalho em aberto

- **Incidente 502:** precisa de logs da Vercel e estado atual da API antes de qualquer afirmação causal ou correção de runtime.
- **Reprocessamento resiliente:** hoje o retry depende do Mercado Pago reenviar. O registro de webhook não processado fica persistido, mas não há worker/outbox/job próprio para varrer e recuperar eventos que deixem de ser reenviados. Avaliar fila ou job com lease/backoff depois do diagnóstico.
- **Concorrência de duplicatas:** a chave única e os `upsert`s protegem duplicidade sequencial; não há lease/lock explícito em `BillingWebhookEvent` para impedir duas invocações concorrentes de processarem simultaneamente a mesma linha não processada. Avaliar claim atômico se a carga/observabilidade demonstrar necessidade.
- **Timeout de API:** `mpRequest` usa `fetch` sem timeout explícito. Considerar timeout/retry limitado e seguro somente após entender a duração e a falha vistas nos logs; falhas devem continuar retornando não-2xx para permitir recuperação.
- **Estado do PIX/migrações em produção:** o código e migração existem no repositório, mas deployment ativo e aplicação das migrações precisam ser confirmados no painel antes de assumir disponibilidade em produção.
- **Estado de credenciais:** confirmar na Vercel que Access Token, segredo de Webhook, seller ID e URL estão no ambiente Production correto e pertencem à aplicação esperada. Não imprimir valores.
- **`npm run build`:** contém migração e seed; para build isolado usar `npx next build`, ou executar o script completo somente em pipeline/ambiente cujo banco alvo tenha sido confirmado.

## 10. Checklist de transferência

- [ ] Obter os logs de produção e o deployment exato para a janela do incidente.
- [ ] Obter consulta autenticada e somente leitura do pagamento `182791299055`.
- [ ] Correlacionar compra, pagamento e evento persistido; registrar se o evento está pendente, processado ou ausente.
- [ ] Definir causa-raiz com evidência do runtime/API/banco.
- [ ] Implementar correção mínima e acrescentar teste para a falha observada.
- [ ] Reexecutar 417+ testes, lint, typecheck e build isolado.
- [ ] Fazer deploy pelo fluxo aprovado; confirmar migrations necessárias.
- [ ] Executar o simulador do Mercado Pago e verificar HTTP 200 e persistência idempotente.
- [ ] Confirmar que o pagamento real só concede acesso se a consulta autenticada indicar aprovação e compra/valor/moeda coincidirem.
- [ ] Documentar resultado e manter segredo, token e dados do comprador fora dos logs/documentos.

## Referências oficiais

- [Webhooks do Mercado Pago — validação de origem e assinatura](https://www.mercadopago.com.br/developers/en/docs/links-and-debts/additional-content/your-integrations/notifications/webhooks)
- [Mercado Pago — consulta de status de pagamentos](https://www.mercadopago.com.br/developers/pt/docs/checkout-api-payments/response-handling/query-results)
- [Vercel — logs da CLI e da função](https://vercel.com/docs/cli/logs)
