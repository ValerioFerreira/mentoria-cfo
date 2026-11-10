import type { Metadata } from "next";
import Link from "next/link";
import { LegalDoc, LegalSection } from "@/components/legal-page";
import { LEGAL } from "@/lib/legal";

export const metadata: Metadata = {
  title: "Termos de Uso",
  description: "Regras de uso da plataforma MentorIA: cadastro, acesso, pagamento, garantia de 7 dias, licença do material e responsabilidades.",
};

export default function TermosPage() {
  return (
    <LegalDoc
      title="Termos de Uso"
      intro={
        <>
          <p>
            Estes Termos regulam o uso da plataforma {LEGAL.brand}, operada por {LEGAL.companyName}, inscrita no CNPJ {LEGAL.cnpj}, com sede na {LEGAL.address} (&quot;nós&quot;). Ao criar sua conta, pagar pelo acesso ou usar a plataforma, você declara que leu e concorda com estes Termos e com a{" "}
            <Link href="/privacidade" className="font-semibold text-primary underline">
              Política de Privacidade
            </Link>
            .
          </p>
          <p>Se não concordar com algum ponto, não use a plataforma. Em caso de dúvida, escreva para {LEGAL.contactEmail}.</p>
        </>
      }
    >
      <LegalSection n={1} title="O que é a plataforma">
        <p>
          A {LEGAL.brand} é uma plataforma de estudos para concursos públicos. Ela monta um plano de estudos a partir das informações que você fornece (concurso, data da prova, horas semanais e assuntos que você já domina), organiza as atividades de cada dia, oferece resumos, questões, simulados, acompanhamento de desempenho e material de estudo próprio em PDF.
        </p>
        <p>
          A plataforma é independente: não temos vínculo com bancas organizadoras, órgãos ou instituições responsáveis pelos concursos, e o uso do nome de um concurso serve apenas para indicar a qual edital o plano se refere.
        </p>
      </LegalSection>

      <LegalSection n={2} title="Sem promessa de aprovação">
        <p>
          Nosso trabalho é organizar e orientar seus estudos. A aprovação em um concurso depende de muitos fatores fora do nosso controle, como a sua dedicação, a concorrência e a forma como a banca elabora a prova. Por isso, não garantimos aprovação, classificação ou nota.
        </p>
        <p>
          O conteúdo é elaborado com cuidado e revisado, mas a legislação e os editais mudam. Confira sempre o texto oficial da norma e o edital do seu concurso. Se encontrar um erro, use o botão de reportar erro na atividade: ele chega até nós e é analisado.
        </p>
      </LegalSection>

      <LegalSection n={3} title="Cadastro e conta">
        <ul>
          <li>A conta é pessoal e intransferível. Você é responsável por manter a senha em sigilo e por tudo o que for feito com ela.</li>
          <li>Você deve informar dados verdadeiros e mantê-los atualizados. O CPF é necessário para abrir os PDFs do material (veja a seção 6).</li>
          <li>A plataforma é destinada a maiores de 18 anos.</li>
          <li>Se suspeitar de uso indevido da sua conta, avise-nos imediatamente pelo e-mail {LEGAL.contactEmail}.</li>
        </ul>
      </LegalSection>

      <LegalSection n={4} title="Acesso e prazo">
        <p>
          O acesso é ilimitado, por pagamento único, e vale até a data da prova do concurso contratado. Depois dessa data, o acesso é encerrado. Se o concurso ainda não tiver data de prova definida, o acesso é liberado sem prazo e passa a valer até a data da prova assim que ela for divulgada e cadastrada.
        </p>
        <p>
          O acesso é liberado depois da confirmação do pagamento. Ele pode ser feito pelo site, em computador ou celular, com conexão à internet.
        </p>
      </LegalSection>

      <LegalSection n={5} title="Preço e pagamento">
        <ul>
          <li>O valor total e os descontos aplicados aparecem antes da confirmação da contratação. O cálculo é feito pelo sistema, e não pelo seu navegador.</li>
          <li>O pagamento pode ser feito por Pix ou por cartão, conforme as opções exibidas. Os dados do cartão são digitados no ambiente do Mercado Pago e não passam pelos nossos servidores.</li>
          <li>Cupons de desconto têm regras próprias, são pessoais e podem ser limitados em quantidade. Descontos somam-se sobre o valor original, até o limite de 100%.</li>
          <li>Podemos alterar preços e condições de novas contratações. Contratações já feitas não mudam de valor.</li>
        </ul>
      </LegalSection>

      <LegalSection n={6} title="Garantia de 7 dias">
        <p>
          Você tem até {LEGAL.refundDays} dias corridos, contados da contratação, para testar a plataforma. Se desistir nesse prazo, devolvemos o valor pago. Esse direito é independente do motivo e está de acordo com o art. 49 do Código de Defesa do Consumidor.
        </p>
        <p>
          Para pedir a devolução, escreva para {LEGAL.contactEmail} informando o nome e o e-mail da conta. A devolução é feita pelo mesmo meio de pagamento, e o acesso é encerrado.
        </p>
      </LegalSection>

      <LegalSection n={7} title="Material de estudo e direitos autorais">
        <p>
          Os textos, resumos, questões comentadas, esquemas, PDFs e demais conteúdos da plataforma são de nossa autoria ou usados com a devida autorização, e protegidos pela legislação de direitos autorais. A contratação concede a você uma licença pessoal, não exclusiva e intransferível de uso para estudo próprio, enquanto o acesso estiver ativo.
        </p>
        <p>Cada PDF do material é entregue com o seu nome e o seu CPF no rodapé de todas as páginas. Isso identifica o titular da licença. É proibido:</p>
        <ul>
          <li>compartilhar, publicar, vender, alugar ou distribuir os PDFs ou qualquer outro conteúdo, no todo ou em parte;</li>
          <li>remover, ocultar ou alterar o carimbo de identificação;</li>
          <li>usar robôs, extratores automáticos ou qualquer meio para copiar o conteúdo em massa;</li>
          <li>compartilhar sua conta ou sua senha com outra pessoa.</li>
        </ul>
        <p>
          Como o PDF carimbado traz o seu CPF, quem o compartilha também expõe os próprios dados. Cuide do arquivo como cuida de um documento pessoal.
        </p>
      </LegalSection>

      <LegalSection n={8} title="Condutas não permitidas">
        <ul>
          <li>Tentar acessar áreas, contas ou dados de outras pessoas, ou testar falhas de segurança sem autorização.</li>
          <li>Interferir no funcionamento da plataforma ou sobrecarregá-la de forma indevida.</li>
          <li>Usar a plataforma para fins ilícitos ou para ofender, ameaçar ou prejudicar terceiros.</li>
          <li>Abusar de cupons ou de indicações de parceiros, como criar contas falsas para obter desconto ou comissão.</li>
        </ul>
      </LegalSection>

      <LegalSection n={9} title="Suspensão e encerramento">
        <p>
          Podemos suspender ou encerrar o acesso, com aviso sempre que possível, se houver descumprimento destes Termos, em especial violação da licença do material (seção 7), fraude ou uso indevido da conta. Nesses casos, não há devolução do valor pago além do que a lei exigir.
        </p>
        <p>Você pode pedir o encerramento da sua conta a qualquer momento pelo e-mail {LEGAL.contactEmail}. O tratamento dos seus dados nessa situação está descrito na Política de Privacidade.</p>
      </LegalSection>

      <LegalSection n={10} title="Disponibilidade e responsabilidade">
        <p>
          Trabalhamos para manter a plataforma disponível, mas podem ocorrer interrupções por manutenção, falhas de internet ou de serviços de terceiros. Faremos o possível para restabelecer o serviço rapidamente.
        </p>
        <p>
          Respondemos pelos danos que a lei determinar. Não respondemos por decisões tomadas apenas com base no conteúdo sem a conferência da norma oficial e do edital, nem por prejuízos causados por uso indevido da conta por quem tenha recebido sua senha.
        </p>
      </LegalSection>

      <LegalSection n={11} title="Mudanças nestes Termos">
        <p>
          Podemos atualizar estes Termos. A data de atualização fica no topo desta página. Mudanças relevantes serão informadas na plataforma ou por e-mail, e não alteram as condições de uma contratação já feita em prejuízo de quem a fez.
        </p>
      </LegalSection>

      <LegalSection n={12} title="Contato">
        <p>
          {LEGAL.companyName} · CNPJ {LEGAL.cnpj}
          <br />
          {LEGAL.address}
          <br />
          {LEGAL.contactEmail}
        </p>
      </LegalSection>

      <LegalSection n={13} title="Lei aplicável e foro">
        <p>
          Estes Termos são regidos pelas leis do Brasil. Fica eleito o foro da {LEGAL.forum}, para resolver qualquer controvérsia, ressalvado o direito do consumidor de propor a ação no foro do seu próprio domicílio, como garante o Código de Defesa do Consumidor.
        </p>
      </LegalSection>
    </LegalDoc>
  );
}
