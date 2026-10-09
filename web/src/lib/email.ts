import "server-only";

export interface SendEmailOptions {
  to: string;
  subject: string;
  html: string;
  text: string;
}

export async function sendEmail({ to, subject, html, text }: SendEmailOptions): Promise<{ success: boolean; error?: string }> {
  const from = process.env.EMAIL_FROM || "MentorIA CBMPE <acesso@mentoriacfo.com.br>";
  const resendKey = process.env.RESEND_API_KEY || process.env.EMAIL_API_KEY;

  // 1) Se houver Resend configurado
  if (resendKey) {
    try {
      const res = await fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${resendKey}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          from,
          to,
          subject,
          html,
          text,
        }),
      });

      if (!res.ok) {
        const errJson = await res.json().catch(() => ({}));
        console.error("Falha ao enviar e-mail via Resend:", errJson);
        return { success: false, error: JSON.stringify(errJson) };
      }
      return { success: true };
    } catch (err: unknown) {
      console.error("Erro na requisição para o Resend:", err);
      return { success: false, error: String(err) };
    }
  }

  // 2) Fallback para desenvolvimento / log seguro no servidor
  console.log(`\n================== [ENVIO DE E-MAIL] ==================`);
  console.log(`Para: ${to}`);
  console.log(`Assunto: ${subject}`);
  console.log(`Texto:\n${text}`);
  console.log(`=======================================================\n`);

  return { success: true };
}

export function generateTemporaryPassword(prefix = "CFO"): string {
  const chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";
  let random = "";
  for (let i = 0; i < 6; i++) {
    random += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return `${prefix}-${random}`;
}

export async function sendApprovalEmail(params: {
  to: string;
  name?: string;
  tempPassword: string;
  accessDuration: string;
  loginUrl: string;
}) {
  const durationText =
    params.accessDuration === "30_DAYS"
      ? "30 dias de acesso"
      : "Acesso por prazo indeterminado (até a homologação do concurso)";

  const greeting = params.name ? `Olá, ${params.name}!` : "Olá!";

  const subject = "Seu acesso ao MentorIA CBMPE foi liberado!";

  const text = `${greeting}

Seu cadastro na plataforma MentorIA — Missão Oficial CBMPE foi aprovado com sucesso!

Validade do Acesso: ${durationText}
Login / E-mail: ${params.to}
Senha Temporária: ${params.tempPassword}

Acesse pelo link: ${params.loginUrl}

Importante: Ao realizar o primeiro login com esta senha temporária, você será orientado a criar uma nova senha pessoal definitiva.

Bons estudos e conte conosco rumo à aprovação!
Equipe MentorIA CBMPE`;

  const html = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>${subject}</title>
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f7f7f8; margin: 0; padding: 32px 16px; color: #1c1c1e;">
  <div style="max-width: 560px; margin: 0 auto; background: #ffffff; border-radius: 16px; border: 1px solid #e5e5ea; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
    <div style="text-align: center; margin-bottom: 24px;">
      <h2 style="font-size: 22px; font-weight: 800; color: #c41c1c; text-transform: uppercase; margin: 0; letter-spacing: 0.5px;">MentorIA</h2>
      <p style="font-size: 12px; font-weight: 600; color: #8e8e93; margin: 4px 0 0; text-transform: uppercase;">Missão Oficial · CBMPE</p>
    </div>
    
    <h1 style="font-size: 20px; font-weight: 700; color: #111111; margin-bottom: 16px;">${greeting}</h1>
    <p style="font-size: 15px; line-height: 1.6; color: #3a3a3c; margin-bottom: 20px;">
      Seu pagamento foi confirmado e seu cadastro na plataforma <strong>MentorIA</strong> foi autorizado com sucesso!
    </p>

    <div style="background-color: #f2f2f7; border-radius: 12px; padding: 20px; margin-bottom: 24px;">
      <p style="margin: 0 0 10px; font-size: 14px; color: #636366;">
        <strong style="color: #1c1c1e;">Validade do Acesso:</strong> ${durationText}
      </p>
      <p style="margin: 0 0 10px; font-size: 14px; color: #636366;">
        <strong style="color: #1c1c1e;">E-mail de Acesso:</strong> ${params.to}
      </p>
      <p style="margin: 0; font-size: 14px; color: #636366;">
        <strong style="color: #1c1c1e;">Senha Temporária:</strong>
        <span style="display: inline-block; background: #ffffff; border: 1px solid #d1d1d6; border-radius: 6px; padding: 4px 10px; font-family: monospace; font-size: 16px; font-weight: bold; color: #c41c1c; margin-left: 6px;">
          ${params.tempPassword}
        </span>
      </p>
    </div>

    <div style="text-align: center; margin-bottom: 24px;">
      <a href="${params.loginUrl}" style="display: inline-block; background-color: #c41c1c; color: #ffffff; font-weight: 700; font-size: 15px; text-decoration: none; padding: 14px 28px; border-radius: 10px; box-shadow: 0 2px 6px rgba(196, 28, 28, 0.3);">
        Acessar a Plataforma
      </a>
    </div>

    <p style="font-size: 13px; color: #8e8e93; line-height: 1.5; margin: 0; border-top: 1px dashed #d1d1d6; pt: 16px; padding-top: 16px;">
      * Por segurança, ao fazer o primeiro login você será direcionado para escolher uma nova senha pessoal definitiva.
    </p>
  </div>
</body>
</html>`;

  return sendEmail({ to: params.to, subject, html, text });
}

export async function sendPasswordResetEmail(params: {
  to: string;
  name?: string;
  tempPassword: string;
  loginUrl: string;
}) {
  const greeting = params.name ? `Olá, ${params.name}!` : "Olá!";
  const subject = "Recuperação de Senha — MentorIA CBMPE";

  const text = `${greeting}

Uma solicitação de recuperação de senha foi realizada para sua conta no MentorIA CBMPE.

Sua nova Senha Temporária é: ${params.tempPassword}

Acesse o sistema pelo link: ${params.loginUrl}

Ao fazer login com esta senha, você será solicitado a cadastrar uma nova senha definitiva.
Se você não solicitou a redefinição de senha, entre em contato imediatamente com o suporte.

Equipe MentorIA CBMPE`;

  const html = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>${subject}</title>
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f7f7f8; margin: 0; padding: 32px 16px; color: #1c1c1e;">
  <div style="max-width: 560px; margin: 0 auto; background: #ffffff; border-radius: 16px; border: 1px solid #e5e5ea; padding: 32px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
    <div style="text-align: center; margin-bottom: 24px;">
      <h2 style="font-size: 22px; font-weight: 800; color: #c41c1c; text-transform: uppercase; margin: 0; letter-spacing: 0.5px;">MentorIA</h2>
      <p style="font-size: 12px; font-weight: 600; color: #8e8e93; margin: 4px 0 0; text-transform: uppercase;">Missão Oficial · CBMPE</p>
    </div>
    
    <h1 style="font-size: 20px; font-weight: 700; color: #111111; margin-bottom: 16px;">${greeting}</h1>
    <p style="font-size: 15px; line-height: 1.6; color: #3a3a3c; margin-bottom: 20px;">
      Recebemos um pedido para recuperar a senha da sua conta de acesso.
    </p>

    <div style="background-color: #f2f2f7; border-radius: 12px; padding: 20px; margin-bottom: 24px; text-align: center;">
      <p style="margin: 0 0 8px; font-size: 13px; font-weight: 600; color: #636366; text-transform: uppercase;">
        Sua Nova Senha Temporária:
      </p>
      <div style="display: inline-block; background: #ffffff; border: 1px solid #d1d1d6; border-radius: 6px; padding: 8px 16px; font-family: monospace; font-size: 18px; font-weight: bold; color: #c41c1c;">
        ${params.tempPassword}
      </div>
    </div>

    <div style="text-align: center; margin-bottom: 24px;">
      <a href="${params.loginUrl}" style="display: inline-block; background-color: #c41c1c; color: #ffffff; font-weight: 700; font-size: 15px; text-decoration: none; padding: 14px 28px; border-radius: 10px; box-shadow: 0 2px 6px rgba(196, 28, 28, 0.3);">
        Entrar e Trocar Senha
      </a>
    </div>

    <p style="font-size: 13px; color: #8e8e93; line-height: 1.5; margin: 0; border-top: 1px dashed #d1d1d6; padding-top: 16px;">
      * Por segurança, você deverá cadastrar uma nova senha pessoal logo após o login. Se você não solicitou este envio, desconsidere esta mensagem.
    </p>
  </div>
</body>
</html>`;

  return sendEmail({ to: params.to, subject, html, text });
}
