"use client";

import type { ReactNode } from "react";

/** Select que envia o formulário ao mudar; `resetOnChange` zera os campos dependentes (ex.: assunto ao trocar a matéria). */
export function AutoSelect({ name, defaultValue, disabled, className, resetOnChange, children }: { name: string; defaultValue: string; disabled?: boolean; className?: string; resetOnChange?: string[]; children: ReactNode }) {
  return (
    <select
      name={name}
      defaultValue={defaultValue}
      disabled={disabled}
      className={className}
      onChange={(e) => {
        const form = e.currentTarget.form;
        if (!form) return;
        for (const n of resetOnChange ?? []) {
          const el = form.elements.namedItem(n);
          if (el instanceof HTMLSelectElement) el.value = "";
        }
        form.requestSubmit();
      }}
    >
      {children}
    </select>
  );
}
