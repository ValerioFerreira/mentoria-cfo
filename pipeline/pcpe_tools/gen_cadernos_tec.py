"""Gera a lista de cadernos que o dono deve montar no TecConcursos para o PCPE Agente (Cebraspe).

Saída: PCPE-CADERNOS-TEC.md e PCPE-CADERNOS-TEC.csv na raiz. Cada caderno agrupa itens consecutivos do edital de uma
disciplina até ~220 questões (o tamanho dos cadernos já importados). Meta de questões = trechos do item × 8 (mínimo
12, máximo 320 por item); piso = trechos × 5 (o caderno do plano usa 25 questões a cada até 4 Teorias).

Uso: python pipeline/pcpe_tools/gen_cadernos_tec.py
"""
from __future__ import annotations

import csv
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "content"
K = "PCPE_AGENTE"
CAP_CADERNO = 220

# disciplina -> (nome da matéria no TEC, observação de filtro)
MATERIA = {
    "lingua-portuguesa": ("Língua Portuguesa (Português)", ""),
    "informatica": ("Informática", ""),
    "raciocinio-logico": ("Raciocínio Lógico", "Se a matéria não tiver o assunto, use também 'Matemática'."),
    "matematica": ("Matemática", ""),
    "estatistica": ("Estatística", ""),
    "contabilidade-geral": ("Contabilidade Geral", "Cebraspe cobra pouco: veja a observação sobre outras bancas."),
    "legislacao-pcpe": ("Legislação Estadual (Pernambuco) / Legislação Específica", "Filtre Órgão = PC-PE; se a matéria não existir, pesquise pelo nome da lei."),
    "direito-constitucional": ("Direito Constitucional (CF/1988 e Doutrina)", ""),
    "direito-administrativo": ("Direito Administrativo (Doutrina e Leis Federais)", ""),
    "direito-penal": ("Direito Penal (Doutrina e Código Penal)", ""),
    "legislacao-penal-especial": ("Legislação Penal e Processual Penal Especial", ""),
    "direito-processual-penal": ("Direito Processual Penal (Doutrina e CPP)", ""),
}

# código do item do edital -> dicas de assunto para o filtro do TEC (aproximadas: use a busca por assunto do TEC)
DICAS = {
    "legislacao-pcpe": {
        "1": "Constituição Estadual (PE) – Segurança Pública, arts. 101 a 105-B",
        "2": "Estatuto do Policial Civil de PE (Lei 6.425/1972)",
        "3": "Estatuto dos Servidores Públicos do Estado de PE (Lei 6.123/1968)",
        "4": "Lei Complementar Estadual 137/2008",
        "5": "Lei Complementar Estadual 317/2015",
    },
    "direito-constitucional": {
        "1": "Princípios fundamentais; Poder constituinte; Teoria da Constituição",
        "2": "Aplicabilidade e eficácia das normas constitucionais",
        "3": "Direitos e garantias fundamentais (individuais, coletivos, sociais, nacionalidade, políticos); remédios constitucionais",
        "4": "Organização do Estado: federação, União, estados, DF, municípios, territórios; intervenção",
        "5": "Administração pública (art. 37) e servidores públicos",
        "6": "Poder Executivo",
        "7": "Poder Legislativo; processo legislativo; CPI",
        "8": "Poder Judiciário",
        "9": "Funções essenciais à justiça: MP, advocacia pública, defensoria",
        "10": "Defesa do Estado e das instituições democráticas; Segurança Pública (art. 144)",
        "11": "Constituição do Estado de Pernambuco – Segurança Pública",
    },
    "direito-administrativo": {
        "1": "Estado, governo e administração; princípios",
        "2": "Conceito, objeto e fontes do Direito Administrativo",
        "3": "Atos administrativos",
        "4": "Poderes administrativos; uso e abuso de poder",
        "5": "Regime jurídico-administrativo; princípios",
        "6": "Responsabilidade civil do Estado",
        "7": "Serviços públicos; concessão, permissão, autorização",
        "8": "Organização administrativa; administração direta e indireta",
        "9": "Controle da administração; improbidade (Lei 8.429/1992); Lei de Abuso/Acesso quando constar",
        "10": "Processo administrativo (Lei 9.784/1999 e Lei estadual 11.781/2000)",
        "11": "Licitações e contratos (Lei 14.133/2021 e, para provas antigas, 8.666/1993)",
        "12": "Agentes públicos; Estatuto federal (Lei 8.112/1990) como base",
        "13": "Cargo, emprego e função; provimento, vacância; responsabilidades",
    },
    "direito-penal": {
        "1": "Princípios do Direito Penal",
        "2": "Teoria do crime: fato típico, ilicitude, culpabilidade, erro",
        "3": "Aplicação da lei penal no tempo e no espaço; conflito aparente",
        "4": "Crimes contra a pessoa (homicídio, lesões, periclitação, honra, liberdade individual)",
        "5": "Crimes contra o patrimônio",
        "6": "Crimes contra a dignidade sexual",
        "7": "Crimes contra a administração pública (peculato, corrupção, contrabando, desacato, falso testemunho…)",
        "20": "Direito penal na Constituição (art. 5º)",
    },
    "legislacao-penal-especial": {
        "8": "Crimes hediondos (Lei 8.072/1990)",
        "9": "Racismo (Lei 7.716/1989)",
        "10": "Abuso de autoridade (Lei 13.869/2019)",
        "11": "Tortura (Lei 9.455/1997)",
        "12": "ECA – crimes e infrações administrativas (Lei 8.069/1990)",
        "13": "Organização criminosa (Lei 12.850/2013)",
        "14": "Crimes de trânsito (Lei 9.503/1997 – CTB)",
        "15": "Violência doméstica (Lei Maria da Penha 11.340/2006)",
        "16": "Lei de Drogas (Lei 11.343/2006)",
        "17": "Violência contra criança e adolescente (Lei 14.344/2022 – Henry Borel)",
        "18": "Crimes ambientais (Lei 9.605/1998)",
        "19": "Estatuto do Desarmamento (Lei 10.826/2003)",
    },
    "direito-processual-penal": {
        "1": "Lei processual penal no tempo, no espaço e quanto às pessoas",
        "2": "Inquérito policial",
        "3": "Provas; cadeia de custódia; interrogatório; testemunhas",
        "4": "Prisão em flagrante, preventiva, liberdade provisória e fiança",
        "5": "Medidas cautelares diversas da prisão",
        "6": "Prisão temporária (Lei 7.960/1989)",
        "7": "Juizados Especiais Criminais (Lei 9.099/1995)",
        "8": "Investigação criminal conduzida por delegado (Lei 12.830/2013)",
        "9": "Princípios constitucionais do processo penal",
    },
    "lingua-portuguesa": {
        "1": "Compreensão e interpretação de textos",
        "2": "Tipologia e gêneros textuais",
        "3": "Ortografia oficial; acentuação",
        "4": "Coesão textual; coesão e coerência; pronomes e conectivos",
        "5": "Morfossintaxe: classes de palavras, termos da oração, período composto, pontuação, concordância, regência, crase",
        "6": "Reescrita de frases e parágrafos",
        "7": "Correspondência oficial (Manual de Redação da Presidência)",
    },
    "informatica": {
        "1": "Windows (explorador, configurações, atalhos)",
        "2": "Microsoft 365: Word, Excel, PowerPoint",
        "3": "Redes, Internet/intranet, segurança, nuvem, redes sociais",
    },
    "raciocinio-logico": {
        "1": "Conjuntos numéricos", "2": "Sistema legal de medidas", "3": "Razão, proporção, regra de três, porcentagem",
        "4": "Equações e inequações", "5": "Sistemas lineares", "6": "Funções e gráficos", "7": "Análise combinatória",
        "8": "Progressões", "9": "Estruturas lógicas", "10": "Lógica de argumentação", "11": "Lógica proposicional",
        "12": "Lógica de primeira ordem (quantificadores)", "13": "Contagem e probabilidade",
        "14": "Operações com conjuntos (diagramas de Venn)", "15": "Problemas aritméticos, geométricos e matriciais; matrizes e determinantes",
    },
    "matematica": {
        "1": "Conjuntos numéricos e operações", "2": "Funções: afim, quadrática, exponencial, logarítmica", "3": "Progressões",
        "4": "Análise combinatória", "5": "Probabilidade", "6": "Sistemas lineares e equações",
    },
    "estatistica": {
        "1": "Estatística descritiva e análise exploratória (gráficos, medidas de posição e dispersão)",
        "2": "Probabilidade (axiomas, condicional, independência)",
        "3": "Amostragem e tamanho amostral",
    },
    "contabilidade-geral": {
        "1": "Conceitos e finalidades da contabilidade", "2": "Patrimônio e equação fundamental", "3": "Atos e fatos administrativos",
        "4": "Contas, débito e crédito", "5": "Plano de contas", "6": "Escrituração e lançamentos", "7": "Operações diversas (juros, descontos, tributos, aluguéis…)",
        "8": "Balancete de verificação", "9": "Balanço patrimonial", "10": "DRE", "11": "CPC / princípios contábeis",
    },
}

# códigos do mapa edital → material refeito em 2026-10-19 (build_edital_pcpe.py): substituem os antigos
DICAS["direito-constitucional"] = {
    "1.1": "Princípios fundamentais da CF/88 (arts. 1º a 4º)", "1.2": "Poder constituinte (originário, derivado e decorrente)",
    "2": "Aplicabilidade e eficácia das normas constitucionais",
    "3": "Direitos e garantias fundamentais (individuais, coletivos, sociais, nacionalidade, políticos); remédios constitucionais",
    "4": "Organização do Estado: federação, União, estados, DF, municípios, territórios; competências; intervenção",
    "5": "Administração pública (art. 37) e servidores públicos", "6": "Poder Executivo", "7": "Poder Legislativo; processo legislativo; CPI",
    "8": "Poder Judiciário", "9.1": "Ministério Público", "9.2": "Advocacia pública", "9.3": "Defensoria Pública",
    "10": "Defesa do Estado e das instituições democráticas; Segurança Pública (art. 144)",
    "11": "Constituição do Estado de Pernambuco – Segurança Pública",
}
DICAS["direito-administrativo"] = {
    "1": "Estado, governo e administração pública", "2": "Conceito, objeto e fontes do Direito Administrativo", "3": "Atos administrativos",
    "4.1": "Poderes: hierárquico, disciplinar, regulamentar e de polícia", "4.2": "Uso e abuso do poder",
    "5.1": "Regime jurídico-administrativo", "5.2": "Princípios expressos e implícitos da administração", "6": "Responsabilidade civil do Estado",
    "7": "Serviços públicos; concessão, permissão, autorização", "8.1": "Centralização, descentralização, concentração e desconcentração",
    "8.2": "Administração direta e indireta", "9.1": "Controle administrativo", "9.2": "Controle judicial", "9.3": "Controle legislativo",
    "9.4": "Improbidade administrativa (Lei 8.429/1992)", "10": "Processo administrativo (Lei 9.784/1999 e Lei estadual 11.781/2000)",
    "11": "Licitações e contratos (Lei 14.133/2021 e, para provas antigas, 8.666/1993)", "12.1": "Agentes públicos: legislação pertinente",
    "12.2": "Agentes públicos: disposições constitucionais", "13": "Cargo, emprego e função pública; provimento e vacância",
}
DICAS["lingua-portuguesa"] = {
    "1": "Compreensão e interpretação de textos", "2": "Tipologia e gêneros textuais", "3": "Ortografia oficial; acentuação",
    "4.1": "Coesão textual: referenciação, conectores, sequenciação", "4.2": "Tempos e modos verbais", "5.1": "Classes de palavras",
    "5.2": "Coordenação (orações e termos)", "5.3": "Subordinação (orações e termos)", "5.4": "Pontuação", "5.5": "Concordância verbal e nominal",
    "5.6": "Regência verbal e nominal", "5.7": "Crase", "5.8": "Colocação pronominal", "6.1": "Significação das palavras",
    "6.2": "Substituição de palavras ou trechos", "6.3": "Reorganização de orações e períodos", "6.4": "Reescrita e níveis de formalidade",
    "7.1": "Redação oficial: aspectos gerais", "7.2": "Redação oficial: finalidade dos expedientes", "7.3": "Redação oficial: adequação da linguagem",
    "7.4": "Redação oficial: formato do texto",
}
DICAS["informatica"] = {
    "1.1": "Windows: janelas, menus, barra de tarefas, área de trabalho", "1.2": "Windows: pastas e arquivos", "1.3": "Windows: configurações básicas",
    "1.4": "Windows Explorer", "2.1": "Word", "2.2": "Excel", "2.3": "PowerPoint",
    "3.1": "Internet, intranet, redes sociais, nuvem, deep web e dark web", "3.2": "Correio eletrônico", "3.3": "Navegadores e sítios de busca",
    "3.4": "Segurança: malwares, antivírus, criptografia", "3.5": "Backup e armazenamento na nuvem",
}
DICAS["raciocinio-logico"] = {
    "7": "Princípios de contagem (análise combinatória)", "9": "Estruturas lógicas", "10": "Lógica de argumentação",
    "11.1": "Proposições simples e compostas", "11.2": "Tabelas-verdade", "11.3": "Equivalências lógicas", "11.4": "Leis de De Morgan; negações",
    "11.5": "Diagramas lógicos", "12": "Lógica de primeira ordem (quantificadores)", "13": "Contagem e probabilidade",
    "14": "Operações com conjuntos (diagramas de Venn)", "15": "Problemas matriciais: matrizes e determinantes",
}
DICAS["matematica"] = {
    "1": "Conjuntos numéricos e operações", "2": "Sistema legal de medidas", "3": "Razões e proporções", "3.1": "Divisão proporcional",
    "3.2": "Regras de três simples e compostas", "3.3": "Porcentagem", "4": "Equações e inequações de 1º e 2º graus", "5": "Sistemas lineares",
    "6": "Funções e gráficos (afim e quadrática)", "8": "Progressões aritméticas e geométricas", "15": "Problemas aritméticos e geométricos (geometria plana)",
}
DICAS["estatistica"] = {
    "1": "Estatística descritiva: gráficos, medidas de posição e dispersão, assimetria e curtose",
    "2.1": "Probabilidade: definições e axiomas", "2.2": "Probabilidade condicional e independência",
    "3.1": "Amostragem: simples, estratificada, sistemática, conglomerados", "3.2": "Tamanho amostral",
}

ORDEM = [
    "legislacao-pcpe", "direito-constitucional", "direito-administrativo", "direito-penal", "legislacao-penal-especial",
    "direito-processual-penal", "lingua-portuguesa", "informatica", "raciocinio-logico", "matematica", "estatistica",
    "contabilidade-geral",
]
SIGLA = {
    "legislacao-pcpe": "LEGPCPE", "direito-constitucional": "DCONST", "direito-administrativo": "DADM", "direito-penal": "DPEN",
    "legislacao-penal-especial": "LPE", "direito-processual-penal": "DPP", "lingua-portuguesa": "PORT", "informatica": "INFO",
    "raciocinio-logico": "RLOG", "matematica": "MAT", "estatistica": "EST", "contabilidade-geral": "CONT",
}
PROVA = {  # questões da prova (60) por disciplina
    "legislacao-pcpe": 4, "direito-constitucional": 4, "direito-administrativo": 4, "direito-penal": 3,
    "legislacao-penal-especial": 2, "direito-processual-penal": 3, "lingua-portuguesa": 10, "informatica": 10,
    "contabilidade-geral": 10, "raciocinio-logico": 3, "matematica": 3, "estatistica": 4,
}


def main() -> None:
    imp = json.loads((C / "importance" / "segments.json").read_text(encoding="utf-8"))["segments"]
    appears = {s for s, v in imp.items() if v["contests"].get(K, {}).get("appears")}
    cadernos: list[dict] = []
    for sub in ORDEM:
        f = C / "edital" / "pcpe" / f"{sub}.json"
        if not f.exists():
            f = C / "edital" / f"{sub}.json"
        items = json.loads(f.read_text(encoding="utf-8"))["items"]
        rows = []
        vistos: set[str] = set()  # cada trecho conta uma vez por disciplina (itens vizinhos repartem os mesmos trechos)
        for it in items:
            segs = {sg for w in it.get("where", []) for sg in w.get("segments", []) if sg in appears} - vistos
            vistos |= segs
            n = len(segs)
            meta = min(320, max(12, n * 8))
            piso = min(200, max(8, n * 5))
            rows.append({"codigo": it["id"], "item": it["item"], "trechos": n, "meta": meta, "piso": piso,
                         "dica": DICAS[sub].get(it["id"], it["item"]), "status": it["status"]})
        cur: list[dict] = []
        tot = 0
        parts = []
        for r in rows:
            if cur and tot + r["meta"] > CAP_CADERNO:
                parts.append(cur)
                cur, tot = [], 0
            cur.append(r)
            tot += r["meta"]
        if cur:
            parts.append(cur)
        for i, p in enumerate(parts, 1):
            cadernos.append({"sub": sub, "nome": f"PCPE {SIGLA[sub]} {i}" if len(parts) > 1 else f"PCPE {SIGLA[sub]}", "itens": p,
                             "meta": sum(x["meta"] for x in p), "piso": sum(x["piso"] for x in p)})
    # CSV
    with open(ROOT / "PCPE-CADERNOS-TEC.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["Caderno", "Matéria no TEC", "Item do edital", "Assunto (dica de busca no TEC)", "Trechos do plano", "Piso", "Meta de questões"])
        for c in cadernos:
            for r in c["itens"]:
                w.writerow([c["nome"], MATERIA[c["sub"]][0], f'{r["codigo"]} – {r["item"]}', r["dica"], r["trechos"], r["piso"], r["meta"]])
    # Markdown
    out = ["# Cadernos do TecConcursos a montar — PCPE Agente de Polícia (Cebraspe)", "",
           "> Gerado por `pipeline/pcpe_tools/gen_cadernos_tec.py` a partir do edital do PCPE (`content/edital`) e dos trechos do plano (`importance/segments.json`). Planilha equivalente: `PCPE-CADERNOS-TEC.csv`.", "",
           "## Filtros comuns a todos os cadernos", "",
           "- **Banca:** CEBRASPE (aparece como *CESPE / CEBRASPE*, *Cebraspe* ou *Cespe/UnB*; marque todas as grafias que o TEC oferecer). O caderno das atividades e os simulados do PCPE usam **só** essa banca.",
           "- **Questões:** exclua *anuladas* e *desatualizadas*. Mantenha **Certo/Errado e múltipla escolha** (a prova do PCPE tem 60 itens e o sistema importa os dois tipos).",
           "- **Ano:** de 2015 em diante para as disciplinas de legislação (Direito Constitucional, Administrativo, Penal, Processual Penal, Legislação Penal Especial, Legislação do PCPE); de 2012 em diante nas demais. Se faltar volume, amplie o intervalo.",
           "- **Órgão/Cargo:** não restrinja (Polícia Civil, Polícia Federal, PRF, tribunais e MP servem); só na *Legislação do PCPE* filtre **Órgão = PC-PE**.",
           "- **Ordenação:** por **Assunto** (ajuda a importar e classificar). **Nome do caderno:** exatamente o da tabela (o importador usa o título do caderno para organizar o relatório).",
           "- **Exportar:** *Imprimir caderno* → PDF → salvar em `docs/questoes/`. Depois: `pipeline/.venv/Scripts/python pipeline/questoes/importar.py` (hoje o importador classifica só as matérias do CBMPE/PMPE; veja o aviso abaixo).",
           "- **Tamanho:** cada caderno tem até ~220 questões (o tamanho dos cadernos já importados). Se o TEC não achar a meta, o **piso** é o mínimo que mantém ~5 questões por trecho de Teoria (o caderno das atividades usa 25 questões a cada até 4 Teorias).", "",
           "## Resumo", "",
           "| Disciplina | Questões na prova | Trechos no plano | Cadernos | Meta de questões |", "| --- | ---: | ---: | ---: | ---: |"]
    tot_c = tot_m = tot_t = 0
    for sub in ORDEM:
        cs = [c for c in cadernos if c["sub"] == sub]
        t = sum(r["trechos"] for c in cs for r in c["itens"])
        m = sum(c["meta"] for c in cs)
        out.append(f"| {MATERIA[sub][0]} | {PROVA[sub]} | {t} | {len(cs)} | {m} |")
        tot_c += len(cs); tot_m += m; tot_t += t
    out.append(f"| **Total** | 60 | {tot_t} | {tot_c} | {tot_m} |")
    out += ["", "## Cadernos", ""]
    for c in cadernos:
        out.append(f"### {c['nome']} — {MATERIA[c['sub']][0]}  (meta {c['meta']} · piso {c['piso']})")
        if MATERIA[c["sub"]][1]:
            out += ["", f"_{MATERIA[c['sub']][1]}_"]
        out += ["", "| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |", "| --- | --- | ---: | ---: |"]
        for r in c["itens"]:
            nota = "" if r["status"] in ("covered",) else " ⚠ complemento/lacuna"
            out.append(f"| {r['codigo']} | {r['dica']}{nota} | {r['trechos']} | {r['meta']} |")
        out.append("")
    out += ["## Avisos", "",
            "1. **Contabilidade Geral:** o Cebraspe cobra pouca Contabilidade em provas de polícia; é provável que o TEC devolva menos que a meta. O plano e os simulados do PCPE só usam Cebraspe, então vale decidir antes se Contabilidade pode usar outras bancas (FCC, FGV, Vunesp…) no caderno das atividades. Monte também um caderno **sem filtro de banca** (nome `PCPE CONT extra`) para o treino livre.",
            "2. **Itens com ⚠:** têm material complementar ou lacuna no conteúdo; a classificação dessas questões depende de os complementos estarem no catálogo.",
            "3. **Matemática × Raciocínio Lógico:** o edital do PCPE reúne os dois no bloco \"Raciocínio Lógico\"; análise combinatória e probabilidade ficam nos cadernos de RL (itens 7 e 13). Cada trecho do plano é contado uma só vez por disciplina (itens vizinhos que dividem os mesmos trechos aparecem com meta mínima).",
            "4. **Importação:** `content/questoes/mapa-assuntos.json` ainda não tem as matérias do TEC de Direito Penal, Processo Penal, Contabilidade e Legislação PCPE, e o classificador só reconhece os cadernos do CBMPE/PMPE. Isso faz parte do **importador de questões por concurso** (sessão separada, ainda pendente): baixar os PDFs agora e importar depois é seguro."]
    (ROOT / "PCPE-CADERNOS-TEC.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(cadernos)} cadernos, meta total {tot_m}, trechos {tot_t}")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
