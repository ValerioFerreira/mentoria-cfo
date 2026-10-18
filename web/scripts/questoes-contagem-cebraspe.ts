// Consulta questões Cebraspe aprovadas no banco por disciplina e aula/item
import "dotenv/config";
import { db } from "../src/lib/db";

async function main() {
  try {
    const q = await db.question.groupBy({
      by: ["subjectId", "aulaId", "editalItemId"],
      where: {
        status: "APPROVED",
        banca: { contains: "CEBRASPE", mode: "insensitive" },
      },
      _count: { id: true },
    });
    console.log("JSON_START" + JSON.stringify(q) + "JSON_END");
  } catch {
    console.log("JSON_START[]JSON_END");
  }
}

main().finally(() => db["$disconnect"]());
