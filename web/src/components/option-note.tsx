import { cx } from "@/components/ui";

/**
 * Nota de uma alternativa ("Correta: …" / "Errada: …"), mostrada depois da resposta. O veredito vai em negrito.
 * `inline-block`: a nota não herda o riscado (line-through) da alternativa marcada errada nas telas de resultado.
 */
export function OptionNote({ text, className, small }: { text: string | null | undefined; className?: string; small?: boolean }) {
  if (!text) return null;
  const m = text.match(/^(Correta|Errada|Incorreta)\s*[:.]\s*/);
  return (
    <p className={cx("inline-block w-full font-normal leading-relaxed text-text/80", small ? "text-xs" : "text-[13px]", className)}>
      {m ? (
        <>
          <strong className="font-semibold text-text">{m[1] === "Incorreta" ? "Errada" : m[1]}:</strong> {text.slice(m[0].length)}
        </>
      ) : (
        text
      )}
    </p>
  );
}

/** Notas por letra a partir das alternativas do banco (só as que têm nota). */
export function optionComments(options: { label: string; comment: string | null }[]): Record<string, string> | null {
  const entries = options.filter((o) => o.comment).map((o) => [o.label, o.comment as string] as const);
  return entries.length ? Object.fromEntries(entries) : null;
}
