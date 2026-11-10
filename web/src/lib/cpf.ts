/** CPF: só dígitos no banco; validação dos dígitos verificadores e formatação para exibição. */
export function cpfDigits(v: string): string {
  return (v ?? "").replace(/\D/g, "");
}

export function isValidCpf(v: string): boolean {
  const d = cpfDigits(v);
  if (d.length !== 11 || /^(\d)\1{10}$/.test(d)) return false;
  for (const n of [9, 10]) {
    let sum = 0;
    for (let i = 0; i < n; i++) sum += Number(d[i]) * (n + 1 - i);
    const dv = ((sum * 10) % 11) % 10;
    if (dv !== Number(d[n])) return false;
  }
  return true;
}

export function formatCpf(v: string): string {
  const d = cpfDigits(v);
  return d.length === 11 ? `${d.slice(0, 3)}.${d.slice(3, 6)}.${d.slice(6, 9)}-${d.slice(9)}` : v;
}

/** CPF parcialmente oculto, para telas: ***.456.789-** */
export function maskCpf(v: string): string {
  const d = cpfDigits(v);
  return d.length === 11 ? `***.${d.slice(3, 6)}.${d.slice(6, 9)}-**` : "";
}
