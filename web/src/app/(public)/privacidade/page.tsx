import type { Metadata } from "next";
import Link from "next/link";
import { LegalDoc, LegalSection } from "@/components/legal-page";
import { LEGAL } from "@/lib/legal";

export const metadata: Metadata = {
  title: "Política de Privacidade",
  description: "Como a MentorIA trata seus dados pessoais: o que coletamos, por quê, com quem compartilhamos e como exercer seus direitos (LGPD).",
};

export default function PrivacidadePage() {
  return (
    <LegalDoc
      title="Política de Privacidade"
      intro={
        <>
          <p>
            Esta Política explica como a {LEGAL.brand} trata os seus dados pessoais, de acordo com a Lei Geral de Proteção de Dados (Lei 13.709/2018). Ela vale junto com os{" "}
            <Link href="/termos" className="font-semibold text-primary underline">
              Termos de Uso
            </Link>
            .
          </p>
          <p>Em resumo: pedimos só o que a plataforma precisa, não vendemos seus dados, não usamos rastreadores de publicidade e você pode pedir acesso, correção ou exclusão quando quiser.</p>
        </>
      }
    >
      <LegalSection n={1} title="Quem é o responsável pelos dados">
        <p>
          O responsável (controlador) é {LEGAL.companyName}, CNPJ {LEGAL.cnpj}, com sede na {LEGAL.address}, que opera a plataforma {LEGAL.brand}.
        </p>
        <ul>
          <li>Contato geral: {LEGAL.contactEmail}</li>
          <li>Encarregado pelo tratamento de dados pessoais: {LEGAL.dpoEmail}</li>
        </ul>
      </LegalSection>

      <LegalSection n={2} title="Quais dados coletamos e para quê">
        <ul>
          <li>
            <strong>Conta:</strong> nome, e-mail e nome de usuário. A senha é guardada de forma irreversível (nem nós a conseguimos ler). Usamos esses dados para criar e proteger sua conta e para o contrato de acesso.
          </li>
          <li>
            <strong>CPF:</strong> pedido uma única vez, quando você abre um PDF do material pela primeira vez. Ele aparece, com o seu nome, no rodapé de todas as páginas do PDF que você baixa, para identificar o titular da licença e coibir o compartilhamento indevido do material. O PDF carimbado contém o seu CPF, por isso não o repasse a ninguém.
          </li>
          <li>
            <strong>Estudo:</strong> concurso escolhido, data da prova, horas semanais, idioma estrangeiro, assuntos que você marcou como estudados, planos gerados, atividades concluídas, tempo de estudo lançado, anotações e resumos que você escreve, respostas a questões e simulados e o seu desempenho. Usamos esses dados para montar o plano, mostrar o seu progresso e calibrar as próximas atividades.
          </li>
          <li>
            <strong>Contratação e pagamento:</strong> concurso contratado, valor, cupons usados, datas, situação do pagamento e identificadores da transação. Os dados do cartão são digitados direto no Mercado Pago e não chegam a nós. No Pix, recebemos a confirmação do pagamento e as informações que acompanham a transação.
          </li>
          <li>
            <strong>Indicação por parceiros:</strong> se você usar o cupom de um parceiro, registramos essa indicação. O parceiro recebe apenas totais (quantidade de indicados e valores de comissão), e não os seus dados pessoais.
          </li>
          <li>
            <strong>Mensagens e relatos:</strong> o que você escreve ao reportar um erro em um PDF ou em uma questão, ou ao falar conosco, junto com a sua identificação na conta.
          </li>
          <li>
            <strong>Dados técnicos e de segurança:</strong> cookies de sessão, registros de acesso (como data, hora e endereço IP, mantidos pela hospedagem) e registros de ações administrativas. Servem para manter você conectado, proteger a plataforma contra fraudes e cumprir a lei.
          </li>
        </ul>
        <p>Enviamos e-mails apenas relacionados ao serviço, como confirmação de acesso, senha temporária, recuperação de senha e respostas a pedidos seus.</p>
      </LegalSection>

      <LegalSection n={3} title="Em que a lei nos apoia (bases legais)">
        <ul>
          <li>Execução do contrato de acesso à plataforma, para conta, plano de estudos, desempenho e entrega do material (LGPD, art. 7º, V).</li>
          <li>Cumprimento de obrigações legais, como registros fiscais e de acesso (art. 7º, II).</li>
          <li>Legítimo interesse, em especial para o carimbo do CPF no material, a segurança da conta e a prevenção de fraudes (art. 7º, IX), sempre respeitando os seus direitos e as suas expectativas.</li>
          <li>Exercício regular de direitos, em caso de disputa ou processo (art. 7º, VI).</li>
        </ul>
      </LegalSection>

      <LegalSection n={4} title="Cookies e armazenamento no navegador">
        <ul>
          <li>
            <strong>Cookie de sessão:</strong> essencial. Mantém você conectado. Sem ele, o login não funciona.
          </li>
          <li>
            <strong>Cookie de aparência:</strong> guarda se você escolheu o tema claro, sépia ou escuro.
          </li>
          <li>
            <strong>Armazenamento local do navegador:</strong> o cronômetro de estudo funciona só no seu navegador, e os tempos dele não são enviados para nós.
          </li>
        </ul>
        <p>
          Não usamos cookies de publicidade nem ferramentas de análise de terceiros. O ambiente de pagamento do Mercado Pago pode usar os próprios cookies, regidos pela política dele.
        </p>
      </LegalSection>

      <LegalSection n={5} title="Com quem compartilhamos">
        <p>Não vendemos nem alugamos seus dados. Compartilhamos apenas com empresas que nos prestam serviços, para que a plataforma funcione:</p>
        <ul>
          <li>Vercel: hospedagem do site e dos servidores da aplicação.</li>
          <li>Neon: banco de dados onde ficam os dados da sua conta e do seu estudo.</li>
          <li>Cloudflare: armazenamento privado dos PDFs do material.</li>
          <li>Mercado Pago: processamento dos pagamentos.</li>
          <li>Provedor de envio de e-mails: mensagens do serviço.</li>
        </ul>
        <p>Também podemos informar dados a autoridades, quando a lei ou uma ordem judicial exigir.</p>
      </LegalSection>

      <LegalSection n={6} title="Transferência para fora do Brasil">
        <p>
          Alguns desses fornecedores processam dados em servidores fora do Brasil. Nesses casos, a transferência é feita para fornecedores que oferecem garantias de proteção compatíveis com a LGPD (art. 33), e só para as finalidades descritas nesta Política.
        </p>
      </LegalSection>

      <LegalSection n={7} title="Por quanto tempo guardamos">
        <p>
          Guardamos seus dados enquanto a sua conta existir. Depois do encerramento, mantemos apenas o que a lei nos obriga a manter (por exemplo, registros fiscais e contábeis, em regra por cinco anos, e registros de acesso pelo prazo legal) e o necessário para nos defender em eventuais disputas. Passado esse período, os dados são apagados ou tornados anônimos.
        </p>
      </LegalSection>

      <LegalSection n={8} title="Seus direitos">
        <p>A LGPD garante a você, a qualquer momento e sem custo:</p>
        <ul>
          <li>confirmar se tratamos seus dados e acessá-los;</li>
          <li>corrigir dados incompletos, inexatos ou desatualizados;</li>
          <li>pedir a anonimização, o bloqueio ou a eliminação de dados desnecessários ou tratados de forma irregular;</li>
          <li>pedir a eliminação dos dados tratados com o seu consentimento e a portabilidade para outro fornecedor;</li>
          <li>saber com quem compartilhamos seus dados;</li>
          <li>revogar o consentimento, quando ele for a base do tratamento, e se opor a um tratamento que considere indevido.</li>
        </ul>
        <p>
          Para exercer qualquer um desses direitos, escreva ao encarregado, em {LEGAL.dpoEmail}. Respondemos e, quando o pedido for de correção, corrigimos os dados em até {LEGAL.rightsDays} dias corridos. Para sua segurança, podemos pedir a confirmação da sua identidade. Se não ficar satisfeito, você também pode reclamar à Autoridade Nacional de Proteção de Dados (ANPD).
        </p>
        <p>Parte dos dados pode precisar ser mantida por obrigação legal. Nesse caso, explicamos o motivo quando respondermos ao seu pedido.</p>
      </LegalSection>

      <LegalSection n={9} title="Como protegemos os dados">
        <ul>
          <li>Senhas armazenadas de forma irreversível e sessões por cookie protegido.</li>
          <li>Acesso restrito aos dados, só para quem precisa deles no trabalho, com registro das ações administrativas.</li>
          <li>PDFs guardados em armazenamento privado, entregues apenas a quem está conectado e com acesso ativo.</li>
          <li>Comunicação protegida por criptografia (HTTPS).</li>
        </ul>
        <p>
          Nenhum sistema é totalmente imune a falhas. Se ocorrer um incidente que possa causar risco ou dano relevante a você, avisaremos você e a ANPD, como a lei determina.
        </p>
      </LegalSection>

      <LegalSection n={10} title="Crianças e adolescentes">
        <p>A plataforma é destinada a maiores de 18 anos. Não coletamos intencionalmente dados de menores. Se perceber que isso aconteceu, fale com o encarregado para que possamos apagar os dados.</p>
      </LegalSection>

      <LegalSection n={11} title="Mudanças nesta Política">
        <p>Podemos atualizar esta Política. A data de atualização fica no topo desta página, e mudanças relevantes serão avisadas na plataforma ou por e-mail.</p>
      </LegalSection>
    </LegalDoc>
  );
}
