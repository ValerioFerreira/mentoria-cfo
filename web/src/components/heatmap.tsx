import type { CSSProperties } from "react";
import type { DayTotal } from "@/lib/metrics";
import { fmtDuration } from "@/lib/ui-format";

const DOW = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"];
const level = (s: number) => (s <= 0 ? 0 : s < 1800 ? 1 : s < 5400 ? 2 : s < 10800 ? 3 : 4);
const SHADE = ["var(--surface-3)", "color-mix(in srgb, var(--primary) 28%, var(--surface-3))", "color-mix(in srgb, var(--primary) 52%, var(--surface-3))", "color-mix(in srgb, var(--primary) 78%, var(--surface-3))", "var(--primary)"];

/** Mapa de calor de estudo: colunas = semanas (começando na segunda), linhas = dias. */
export function Heatmap({ days }: { days: DayTotal[] }) {
  if (days.length === 0) return null;
  const first = new Date(`${days[0].date}T00:00:00Z`);
  const lead = (first.getUTCDay() + 6) % 7; // casas vazias até a primeira segunda
  const today = days[days.length - 1].date;
  const cells: (DayTotal | null)[] = [...Array.from({ length: lead }, () => null), ...days];
  const cols = Math.ceil(cells.length / 7);
  return (
    <div>
      <div className="flex gap-2">
        <div className="grid grid-rows-7 gap-[3px] pt-px text-[10px] font-semibold uppercase leading-none text-muted" aria-hidden>
          {DOW.map((d, i) => (
            <span key={d} className="flex items-center" style={{ height: "clamp(11px, 1.6vw, 17px)", visibility: i % 2 === 0 ? "visible" : "hidden" }}>{d}</span>
          ))}
        </div>
        <div className="grid min-w-0 flex-1 grid-flow-col grid-rows-7 gap-[3px]" style={{ gridTemplateColumns: `repeat(${cols}, minmax(0, 1fr))` }} role="img" aria-label="Mapa de calor das horas estudadas por dia">
          {cells.map((c, i) =>
            c ? (
              <span
                key={c.date}
                title={`${new Date(`${c.date}T12:00:00Z`).toLocaleDateString("pt-BR", { day: "2-digit", month: "short", timeZone: "UTC" })} · ${c.seconds ? fmtDuration(c.seconds) : "sem estudo"}`}
                className={`heat-cell block rounded-[4px] ${c.date === today ? "outline outline-2 outline-offset-1 outline-gold" : ""}`}
                style={{ background: SHADE[level(c.seconds)], height: "clamp(11px, 1.6vw, 17px)", "--i": i } as CSSProperties}
              />
            ) : (
              <span key={`pad${i}`} />
            ),
          )}
        </div>
      </div>
      <div className="mt-3 flex items-center justify-end gap-1.5 text-[11px] font-medium text-muted">
        menos
        {SHADE.map((s, i) => (
          <span key={i} className="h-3 w-3 rounded-[3px]" style={{ background: s }} />
        ))}
        mais
      </div>
    </div>
  );
}
