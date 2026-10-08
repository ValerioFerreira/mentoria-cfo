import { FileText } from "lucide-react";
import { LinkButton } from "@/components/ui";

/** Abre o PDF do material complementar do MentorIA (já na página em que o trecho começa). */
export function MaterialLink({ path, page }: { path?: string | null; page?: number }) {
  if (!path) return null;
  return (
    <div className="space-y-1.5 rounded-xl border border-gold/50 bg-gold-soft/50 p-3.5">
      <p className="text-sm font-semibold text-gold-text">Material complementar do MentorIA</p>
      <p className="text-xs text-muted">Texto preparado pelo MentorIA para fechar uma lacuna do edital.</p>
      <LinkButton href={`/${path}${page ? `#page=${page}` : ""}`} target="_blank" rel="noopener" variant="secondary" size="sm">
        <FileText className="h-4 w-4" aria-hidden />
        Abrir material (PDF){page ? `, página ${page}` : ""}
      </LinkButton>
    </div>
  );
}
