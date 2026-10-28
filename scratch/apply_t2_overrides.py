import json
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
OVERRIDES_DIR = ROOT / "content/overrides"

def update_file(filename, updates):
    path = OVERRIDES_DIR / filename
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"aulas": {}}
    aulas = data.get("aulas", {})
    for aula_id, info in updates.items():
        aula = aulas.setdefault(aula_id, {})
        if "headings_update" in info:
            # list of (page, new_title)
            existing_headings = aula.get("headings", [])
            for p, new_title in info["headings_update"]:
                found = False
                for h in existing_headings:
                    if h["page"] == p:
                        h["title"] = new_title
                        found = True
                        break
                if not found:
                    existing_headings.append({"page": p, "title": new_title, "level": 1})
            aula["headings"] = existing_headings
        if "dropHeadings_add" in info:
            existing_drops = aula.get("dropHeadings", [])
            for d in info["dropHeadings_add"]:
                if d not in existing_drops:
                    existing_drops.append(d)
            aula["dropHeadings"] = existing_drops
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Atualizado {filename}")

# 1. contabilidade-geral.json
update_file("contabilidade-geral.json", {
    "contabilidade-geral/a00": {"headings_update": [(3, "Apresentação do Curso e Metodologia de Contabilidade")]},
    "contabilidade-geral/a03": {"headings_update": [(31, "Tipos de Fatos Contábeis e Atos Administrativos")]},
    "contabilidade-geral/a06": {"headings_update": [(30, "Perdas estimadas com créditos de liquidação duvidosa (PECLD)")]},
    "contabilidade-geral/a08": {"headings_update": [(19, "Critério de avaliação do ativo imobilizado e custo atribuído")]},
    "contabilidade-geral/a10": {"headings_update": [(12, "Investimentos: mais-valia e goodwill")]},
    "contabilidade-geral/a13": {"headings_update": [(19, "Debêntures: conceito, características básicas e aspectos contábeis")]},
    "contabilidade-geral/a17": {"headings_update": [(12, "Critérios de avaliação de ativos e passivos: valor realizável")]},
    "contabilidade-geral/a19": {
        "headings_update": [
            (18, "Demonstrações contábeis: considerações gerais, estrutura e conteúdo"),
            (33, "Passivo circulante e não circulante no balanço patrimonial"),
            (46, "Demonstração do resultado do período e formas de apresentação das despesas")
        ]
    }
})

# 2. direito-administrativo.json
update_file("direito-administrativo.json", {
    "direito-administrativo/a20": {"headings_update": [(103, "Julgamento por melhor técnica ou técnica e preço: quesitos técnicos")]},
    "direito-administrativo/a21": {
        "headings_update": [
            (100, "Propostas inexequíveis e critérios de desempate e preferência"),
            (145, "Termo de referência e projeto básico na licitação")
        ]
    },
    "direito-administrativo/a22": {
        "headings_update": [
            (16, "Serviços contínuos e contratos de fornecimento"),
            (160, "Procedimento de apuração e aplicação de sanções"),
            (175, "Do recurso e pedido de reconsideração")
        ]
    }
})

# 3. direito-penal.json
update_file("direito-penal.json", {
    "direito-penal/a00": {"headings_update": [(30, "Súmulas pertinentes do STJ sobre Direito Penal")]},
    "direito-penal/a01": {"headings_update": [(33, "Aplicação da Lei penal em relação às pessoas: Sujeito ativo e passivo")]},
    "direito-penal/a02": {"headings_update": [(19, "Tipicidade penal: tipicidade formal, material e conglobante")]},
    "direito-penal/a04": {
        "headings_update": [
            (22, "Homicídio qualificado-privilegiado e majorantes"),
            (37, "Art. 121-B, vicaricídio e induzimento ao suicídio")
        ]
    },
    "direito-penal/a05": {"headings_update": [(139, "Da receptação: aspectos gerais e tipo penal")]},
    "direito-penal/a06": {"headings_update": [(35, "Favorecimento da prostituição de vulnerável (art. 218-B)")]},
    "direito-penal/a07": {"headings_update": [(21, "Facilitação de contrabando ou descaminho e prevaricação")]},
    "direito-penal/a09": {"headings_update": [(18, "Comunicação falsa de crime e autoacusação")]}
})

# 4. direito-processual-penal.json
update_file("direito-processual-penal.json", {
    "direito-processual-penal/a00": {"headings_update": [(8, "Princípio do devido processo legal, contraditório e ampla defesa")]},
    "direito-processual-penal/a01": {"headings_update": [(46, "Disposições legais do CPP sobre o Inquérito Policial")]},
    "direito-processual-penal/a03": {"headings_update": [(45, "Da confissão: conceito, requisitos e aspectos gerais")]},
    "direito-processual-penal/a06": {"headings_update": [(2, "Juizados Especiais Criminais: Considerações gerais e rito sumaríssimo")]}
})

# 5. legislacao-pcpe.json
update_file("legislacao-pcpe.json", {
    "legislacao-pcpe/a03": {
        "headings_update": [
            (2, "Sumário e Apresentação: Lei nº 6.425/1972"),
            (10, "Regime jurídico e Da Nomeação")
        ]
    },
    "legislacao-pcpe/a05": {
        "headings_update": [
            (3, "Apresentação do Curso: Lei Estadual nº 6.123/1968"),
            (12, "Da remoção, estágio probatório e promoção")
        ]
    },
    "legislacao-pcpe/a07": {"headings_update": [(3, "Apresentação e Estatuto dos Servidores: Regime disciplinar")]}
})

# 6. legislacao-penal-especial.json
update_file("legislacao-penal-especial.json", {
    "legislacao-penal-especial/a11": {"headings_update": [(24, "Crimes hediondos no Estatuto da Criança e do Adolescente (ECA)")]},
    "legislacao-penal-especial/a13": {"headings_update": [(3, "Lei nº 13.869/2019: Crimes de abuso de autoridade")]},
    "legislacao-penal-especial/a18": {"headings_update": [(35, "Do tráfico privilegiado de drogas")]},
    "legislacao-penal-especial/a20": {"headings_update": [(38, "Crimes contra a flora em florestas de preservação permanente")]},
    "legislacao-penal-especial/a21": {"headings_update": [(15, "Porte de arma de fogo: agentes e guardas prisionais")]}
})

# 7. direito-constitucional.json
update_file("direito-constitucional.json", {
    "direito-constitucional/a03": {"headings_update": [(24, "Crimes inafiançáveis e individualização da pena (art. 5º, XLIII a XLVI)")]}
})

# 8. estatistica.json
update_file("estatistica.json", {
    "estatistica/a01": {
        "dropHeadings_add": [{"page": 3, "title": "Noções Iniciais sobre Médias"}],
        "headings_update": [(3, "Introdução às Médias e Medidas de Posição")]
    }
})

# 9. informatica.json
update_file("informatica.json", {
    "informatica/a04": {
        "dropHeadings_add": [{"page": 60, "title": "IREWALL"}],
        "headings_update": [(60, "Firewall")]
    }
})

# 10. raciocinio-logico.json
update_file("raciocinio-logico.json", {
    "raciocinio-logico/a00": {"headings_update": [(1, "Apresentação do Curso e Raciocínio Lógico")]},
    "raciocinio-logico/a01": {"headings_update": [(1, "Raciocínio Lógico: Conversão de Linguagem")]},
    "raciocinio-logico/a03": {"headings_update": [(1, "Raciocínio Lógico: Proposições Quantificadas")]}
})
print("Todos os overrides T2 aplicados!")
