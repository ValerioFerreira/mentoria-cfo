import "server-only";
import { readFileSync } from "node:fs";
import path from "node:path";
import type { SegmentAnchor } from "@/lib/directive";

/** Âncoras das diretrizes do material-base (content/directive/anchors.json, espelhado em web/content). */
let cache: Record<string, SegmentAnchor> | null = null;

export function segmentAnchors(): Record<string, SegmentAnchor> {
  if (cache) return cache;
  try {
    cache = JSON.parse(readFileSync(path.join(process.cwd(), "content", "directive", "anchors.json"), "utf8")) as Record<string, SegmentAnchor>;
  } catch {
    cache = {};
  }
  return cache;
}
