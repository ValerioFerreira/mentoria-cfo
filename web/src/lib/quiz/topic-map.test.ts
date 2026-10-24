import { describe, expect, it } from "vitest";
import { OTHER_TOPIC, filterByTopics, makeTopicResolver, type TopicItem } from "./topic-map";

const items: TopicItem[] = [
  // assuntos padrão (CBMPE/PMPE), tirados do PCPE e CFOA
  { id: "direito-administrativo/e4", subjectId: "direito-administrativo", onlyContests: [], excludeContests: ["PCPE_AGENTE", "CBMPE_CFOA"], aulaIds: ["direito-administrativo/a04"] },
  // assuntos próprios do PCPE
  { id: "direito-administrativo/p4.1", subjectId: "direito-administrativo", onlyContests: ["PCPE_AGENTE"], excludeContests: [], aulaIds: ["direito-administrativo/a04", "direito-administrativo/a05"] },
  { id: "direito-administrativo/p4.2", subjectId: "direito-administrativo", onlyContests: ["PCPE_AGENTE"], excludeContests: [], aulaIds: ["direito-administrativo/a04"] },
  // assunto próprio do CFOA
  { id: "direito-administrativo/f3", subjectId: "direito-administrativo", onlyContests: ["CBMPE_CFOA"], excludeContests: [], aulaIds: ["direito-administrativo/a04"] },
  // disciplina só do PCPE: o assunto padrão vale
  { id: "direito-penal/e1", subjectId: "direito-penal", onlyContests: [], excludeContests: [], aulaIds: ["direito-penal/a00"] },
];

const q = (editalItemId: string | null, subjectId: string, aulaId: string) => ({ editalItemId, subjectId, aulaId });

describe("makeTopicResolver", () => {
  it("CBMPE e PMPE mantêm o assunto gravado", () => {
    const r = makeTopicResolver(items, "CBMPE_OFICIAL");
    expect(r(q("direito-administrativo/e4", "direito-administrativo", "direito-administrativo/a04"))).toBe("direito-administrativo/e4");
  });

  it("no PCPE, a questão de assunto padrão vai para o assunto do edital dele que trata da mesma aula (o mais específico)", () => {
    const r = makeTopicResolver(items, "PCPE_AGENTE");
    expect(r(q("direito-administrativo/e4", "direito-administrativo", "direito-administrativo/a04"))).toBe("direito-administrativo/p4.2");
    expect(r(q(null, "direito-administrativo", "direito-administrativo/a05"))).toBe("direito-administrativo/p4.1");
  });

  it("no CFOA, a questão de direito-administrativo com item /e cai no item /f correspondente", () => {
    const r = makeTopicResolver(items, "CBMPE_CFOA");
    expect(r(q("direito-administrativo/e4", "direito-administrativo", "direito-administrativo/a04"))).toBe("direito-administrativo/f3");
  });

  it("assunto próprio do PCPE e disciplina só do PCPE ficam como estão", () => {
    const r = makeTopicResolver(items, "PCPE_AGENTE");
    expect(r(q("direito-administrativo/p4.1", "direito-administrativo", "direito-administrativo/a04"))).toBe("direito-administrativo/p4.1");
    expect(r(q("direito-penal/e1", "direito-penal", "direito-penal/a00"))).toBe("direito-penal/e1");
  });

  it("aula que o edital do concurso não trata cai em 'outros'", () => {
    const r = makeTopicResolver(items, "PCPE_AGENTE");
    expect(r(q("direito-administrativo/e4", "direito-administrativo", "direito-administrativo/a09"))).toBe(OTHER_TOPIC);
  });
});

describe("filterByTopics", () => {
  it("lista vazia devolve tudo; com assuntos, só os do concurso", () => {
    const r = makeTopicResolver(items, "PCPE_AGENTE");
    const qs = [
      q("direito-administrativo/e4", "direito-administrativo", "direito-administrativo/a04"),
      q(null, "direito-administrativo", "direito-administrativo/a05"),
    ];
    expect(filterByTopics(qs, [], r)).toHaveLength(2);
    expect(filterByTopics(qs, ["direito-administrativo/p4.1"], r)).toEqual([qs[1]]);
  });
});
