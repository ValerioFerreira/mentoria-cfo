// Quadros da chama do ícone da aba (SVG gerado). Cada quadro balança e estica um pouco diferente.
const OUTER = "M16 4.2c.5 3.8-1.8 6-3.8 8.5C10.2 15 8 17.4 8 21.3 8 26.2 11.5 29 16 29s8-2.8 8-7.7c0-2.8-1.2-4.700-2.700-6.400-.1 1.900-1 3.300-2.400 4 .8-4.400-.3-9.600-2.900-14.700Z";
const MID = "M16 28.1c-3.100 0-5.300-2.300-5.300-5.400 0-2.200 1.200-3.600 2.500-4.900.9-.9 1.700-1.800 2-3.100 2.300 2 4.800 4.100 4.800 8 0 3.200-1.600 5.400-4 5.400Z";
const CORE = "M16 28.1c-1.700 0-2.800-1.300-2.800-3 0-1.700.9-2.500 1.900-3.400.5-.5.8-.9.9-1.600 1.300 1.200 2.800 2.200 2.800 4.200 0 2.100-1.200 3.800-2.800 3.800Z";

export const FLAME_FRAMES = 10;

/** Quadro `i` (0 … FLAME_FRAMES-1) como string SVG 32×32. */
export function flameFrameSvg(i: number): string {
  const p = (i / FLAME_FRAMES) * Math.PI * 2;
  const sway = Math.sin(p) * 5; // graus
  const stretchO = 1 + Math.sin(p * 2 + 0.6) * 0.07;
  const stretchM = 1 + Math.sin(p * 3 + 1.9) * 0.09;
  const stretchC = 1 + Math.sin(p * 4 + 0.2) * 0.12;
  const skewO = Math.sin(p * 2 + 2.4) * 5;
  const skewM = Math.sin(p * 3) * 7;
  const t = (rot: number, sy: number, sx: number, skew: number) =>
    `translate(16 29) rotate(${rot.toFixed(2)}) skewX(${skew.toFixed(2)}) scale(${sx.toFixed(3)} ${sy.toFixed(3)}) translate(-16 -29)`;
  const ex = Math.sin(p) * 1.5;
  return (
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">` +
    `<rect width="32" height="32" rx="7" fill="#0e1b2e"/>` +
    `<circle cx="16" cy="19" r="12" fill="#ff5a36" opacity=".16"/>` +
    `<path d="${OUTER}" fill="#ff5a36" transform="${t(sway, stretchO, 1 / Math.sqrt(stretchO), skewO)}"/>` +
    `<path d="${MID}" fill="#ff9a2e" transform="${t(sway * 0.7, stretchM, 1 / Math.sqrt(stretchM), skewM)}"/>` +
    `<path d="${CORE}" fill="#ffe27a" transform="${t(sway * 0.4, stretchC, 1 / Math.sqrt(stretchC), -skewM * 0.6)}"/>` +
    `<circle cx="${(12 + ex).toFixed(2)}" cy="${(8 - ((i * 3) % 6) * 0.5).toFixed(2)}" r="0.9" fill="#ffd964" opacity="${(0.9 - ((i * 3) % 6) * 0.15).toFixed(2)}"/>` +
    `</svg>`
  );
}

export const flameFrameHref = (i: number) => `data:image/svg+xml,${encodeURIComponent(flameFrameSvg(i))}`;
