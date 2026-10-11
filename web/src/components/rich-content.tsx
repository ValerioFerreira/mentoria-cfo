"use client";

import React, { useState, type ReactNode } from "react";
import { Maximize2, X } from "lucide-react";

interface RichContentProps {
  content: string | null | undefined;
  className?: string;
  allowImages?: boolean;
}

/**
 * Renderiza formatação inline rica:
 * - Sublinhado com tag <u>...</u>
 * - Negrito com **...**
 * - Itálico com *...*
 * - Código inline com `...`
 */
export function formatInlineRich(text: string): ReactNode {
  if (!text) return null;

  // Regex para capturar <u>...</u>, **...**, *...*, `...`
  const regex = /(<u>[\s\S]*?<\/u>|\*\*[\s\S]*?\*\*|\*[\s\S]*?\*|`[\s\S]*?`)/g;
  const parts = text.split(regex);

  return parts.map((part, idx) => {
    if (!part) return null;

    if (part.startsWith("<u>") && part.endsWith("</u>")) {
      const inner = part.slice(3, -4);
      return (
        <u
          key={idx}
          className="underline decoration-primary decoration-2 underline-offset-4 font-medium text-text"
        >
          {formatInlineRich(inner)}
        </u>
      );
    }

    if (part.startsWith("**") && part.endsWith("**") && part.length > 4) {
      const inner = part.slice(2, -2);
      return (
        <strong key={idx} className="font-semibold text-text">
          {formatInlineRich(inner)}
        </strong>
      );
    }

    if (part.startsWith("*") && part.endsWith("*") && part.length > 2) {
      const inner = part.slice(1, -1);
      return (
        <em key={idx} className="italic text-text/95">
          {formatInlineRich(inner)}
        </em>
      );
    }

    if (part.startsWith("`") && part.endsWith("`") && part.length > 2) {
      return (
        <code
          key={idx}
          className="rounded bg-surface-3 px-1.5 py-0.5 font-mono text-xs font-semibold text-text"
        >
          {part.slice(1, -1)}
        </code>
      );
    }

    // Remove qualquer marcador ** residual solto para impedir exibição literal
    const sanitizedText = part.replace(/\*\*/g, "");
    return <React.Fragment key={idx}>{sanitizedText}</React.Fragment>;
  });
}

/**
 * Componente modal para visualização ampliada de figuras
 */
function ImageModal({ src, alt, onClose }: { src: string; alt: string; onClose: () => void }) {
  return (
    <div
      role="dialog"
      aria-modal="true"
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 p-4 backdrop-blur-xs animate-in fade-in duration-200"
      onClick={onClose}
    >
      <div
        className="relative max-h-[92vh] max-w-[92vw] overflow-auto rounded-2xl bg-surface p-2 shadow-2xl border border-border"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          type="button"
          onClick={onClose}
          aria-label="Fechar visualização"
          className="absolute top-3 right-3 z-10 rounded-full bg-surface-3/80 p-1.5 text-text transition hover:bg-surface-3 hover:scale-105"
        >
          <X className="h-5 w-5" />
        </button>
        {/* eslint-disable-next-line @next/next/no-img-element */}
        <img
          src={src}
          alt={alt}
          className="max-h-[85vh] max-w-full rounded-xl object-contain"
        />
        <p className="mt-2 text-center text-xs text-muted font-medium">{alt}</p>
      </div>
    </div>
  );
}

/**
 * Renderizador de conteúdo rico estruturado com blocos:
 * - Parágrafos normais com preservação de quebra de linha
 * - Imagens embutidas com zoom/lightbox
 * - Citações / Fontes (> ...)
 * - Tabelas markdown
 * - Listas e títulos
 */
export function RichContent({ content, className = "", allowImages = true }: RichContentProps) {
  const [modalImg, setModalImg] = useState<{ src: string; alt: string } | null>(null);

  if (!content) return null;

  // Separação em blocos por linhas em branco duplas
  const blocks = content.split(/\n\s*\n/).map((b) => b.trim()).filter(Boolean);

  return (
    <div className={`space-y-3 leading-relaxed ${className}`}>
      {modalImg && (
        <ImageModal
          src={modalImg.src}
          alt={modalImg.alt}
          onClose={() => setModalImg(null)}
        />
      )}

      {blocks.map((block, bIdx) => {
        // Bloco de Imagem Markdown pura: ![alt](url)
        const imgMatch = block.match(/^!\[(.*?)\]\((.*?)\)$/);
        if (allowImages && imgMatch) {
          const alt = imgMatch[1] || "Figura da questão";
          const src = imgMatch[2];
          return (
            <div key={bIdx} className="my-3 flex flex-col items-center group">
              <div
                className="relative cursor-pointer overflow-hidden rounded-xl border border-border/80 bg-surface-2/40 shadow-xs transition hover:border-primary/50 hover:shadow-md"
                onClick={() => setModalImg({ src, alt })}
                title="Clique para ampliar a imagem"
              >
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={src}
                  alt={alt}
                  className="max-h-80 max-w-full object-contain p-2"
                  loading="lazy"
                />
                <div className="absolute bottom-2 right-2 rounded-lg bg-surface/90 p-1 text-muted shadow-xs opacity-0 transition group-hover:opacity-100">
                  <Maximize2 className="h-4 w-4" />
                </div>
              </div>
              {alt && alt !== "Figura da questão" && (
                <span className="mt-1 text-center text-xs text-muted italic">
                  {alt}
                </span>
              )}
            </div>
          );
        }

        // Citações / Fontes e Referências bibliográficas (> ...)
        if (block.startsWith("> ") || block.startsWith(">")) {
          const quoteText = block.replace(/^>\s*/, "").replace(/\n>\s*/g, "\n");
          return (
            <blockquote
              key={bIdx}
              className="my-2.5 rounded-r-xl border-l-3 border-primary/70 bg-surface-2/50 px-3.5 py-2 text-xs italic text-text/80 shadow-2xs"
            >
              {formatInlineRich(quoteText)}
            </blockquote>
          );
        }

        // Tabela Markdown
        if (block.includes("|") && block.split("\n").length >= 2) {
          const lines = block.split("\n").map((l) => l.trim()).filter(Boolean);
          const header = lines[0];
          const rows = lines.slice(1).filter((l) => !/^\|?[\s|:-]+\|?$/.test(l));
          const parseRow = (r: string) =>
            r.replace(/^\|/, "").replace(/\|$/, "").split("|").map((c) => c.trim());
          const headers = parseRow(header);

          return (
            <div
              key={bIdx}
              className="my-3 overflow-x-auto rounded-xl border border-border/70 bg-surface shadow-xs"
            >
              <table className="w-full text-left text-xs">
                <thead className="border-b border-border/70 bg-surface-2 text-muted font-bold uppercase tracking-wider">
                  <tr>
                    {headers.map((h, i) => (
                      <th key={i} className="px-3 py-2">
                        {formatInlineRich(h)}
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody className="divide-y divide-border/40">
                  {rows.map((row, rIdx) => (
                    <tr key={rIdx} className="hover:bg-surface-2/40">
                      {parseRow(row).map((cell, cIdx) => (
                        <td key={cIdx} className="px-3 py-2 align-top">
                          {formatInlineRich(cell)}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          );
        }

        // Listas não ordenadas
        if (block.startsWith("- ") || block.startsWith("* ")) {
          const items = block
            .split("\n")
            .map((l) => l.replace(/^[-*]\s+/, "").trim())
            .filter(Boolean);
          return (
            <ul key={bIdx} className="space-y-1.5 pl-4 list-disc marker:text-primary">
              {items.map((item, iIdx) => (
                <li key={iIdx}>{formatInlineRich(item)}</li>
              ))}
            </ul>
          );
        }

        // Títulos Markdown
        if (block.startsWith("### ")) {
          return (
            <h4 key={bIdx} className="font-display text-base font-bold text-text pt-1">
              {formatInlineRich(block.replace(/^###\s+/, ""))}
            </h4>
          );
        }
        if (block.startsWith("## ")) {
          return (
            <h3 key={bIdx} className="font-display text-lg font-bold text-text pt-2">
              {formatInlineRich(block.replace(/^##\s+/, ""))}
            </h3>
          );
        }

        // Bloco de texto com parágrafo e imagens misturadas
        if (allowImages && block.includes("![") && block.includes("](")) {
          // Se tiver imagem dentro de um parágrafo maior, quebra em subpartes
          const subparts = block.split(/(!\[.*?\]\(.*?\))/g);
          return (
            <div key={bIdx} className="space-y-2">
              {subparts.map((sp, spIdx) => {
                const subImgMatch = sp.match(/^!\[(.*?)\]\((.*?)\)$/);
                if (subImgMatch) {
                  const alt = subImgMatch[1] || "Figura da questão";
                  const src = subImgMatch[2];
                  return (
                    <div key={spIdx} className="my-3 flex flex-col items-center group">
                      <div
                        className="relative cursor-pointer overflow-hidden rounded-xl border border-border/80 bg-surface-2/40 shadow-xs transition hover:border-primary/50 hover:shadow-md"
                        onClick={() => setModalImg({ src, alt })}
                        title="Clique para ampliar a imagem"
                      >
                        {/* eslint-disable-next-line @next/next/no-img-element */}
                        <img
                          src={src}
                          alt={alt}
                          className="max-h-80 max-w-full object-contain p-2"
                          loading="lazy"
                        />
                        <div className="absolute bottom-2 right-2 rounded-lg bg-surface/90 p-1 text-muted shadow-xs opacity-0 transition group-hover:opacity-100">
                          <Maximize2 className="h-4 w-4" />
                        </div>
                      </div>
                    </div>
                  );
                }
                const lines = sp.split("\n");
                return (
                  <p key={spIdx}>
                    {lines.map((line, lIdx) => (
                      <span key={lIdx}>
                        {lIdx > 0 && <br />}
                        {formatInlineRich(line)}
                      </span>
                    ))}
                  </p>
                );
              })}
            </div>
          );
        }

        // Parágrafo padrão com quebras de linha preservadas
        const lines = block.split("\n");
        return (
          <p key={bIdx}>
            {lines.map((line, lIdx) => (
              <span key={lIdx}>
                {lIdx > 0 && <br />}
                {formatInlineRich(line)}
              </span>
            ))}
          </p>
        );
      })}
    </div>
  );
}
