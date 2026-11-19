/**
 * Nome completo do titular: letras, espaços, apóstrofo, hífen e ponto; ao menos duas palavras. Devolve o nome em caixa alta
 * (é assim que ele fica na conta e no carimbo dos PDFs) ou `null` se não parecer um nome completo.
 */
export function normalizeFullName(raw: string): string | null {
  const name = (raw ?? "").normalize("NFC").replace(/\s+/g, " ").trim();
  if (name.length < 5 || name.length > 120) return null;
  if (!/^[\p{L}][\p{L} .'’-]*$/u.test(name)) return null;
  const words = name.split(" ").filter((w) => w.replace(/[^\p{L}]/gu, "").length >= 1);
  if (words.length < 2 || words.some((w) => !/\p{L}/u.test(w))) return null;
  if (words.filter((w) => w.replace(/[^\p{L}]/gu, "").length >= 2).length < 2) return null;
  return name.toLocaleUpperCase("pt-BR");
}
