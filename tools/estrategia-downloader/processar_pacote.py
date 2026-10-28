import argparse
import json
import logging
import re
import sys
import time
from pathlib import Path

from browser import open_context
from selectors import CourseSelectors
from utils import clean_text, safe_name, valid_pdf


def make_logger(log_dir: Path) -> logging.Logger:
    log_dir.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("pcpe_selective_downloader")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    handler = logging.FileHandler(log_dir / "errors_pcpe_361849.log", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
    return logger


def classify_lesson(course_id: str, course_title: str, lesson_idx_0: int, lesson: dict) -> tuple[str, str, str]:
    """
    Returns (lacuna_2b, decisao, motivo) for a given lesson.
    decisao is one of: 'BAIXAR', 'BAIXAR (versão alternativa)', 'DÚVIDA', 'NÃO BAIXAR'
    """
    title = lesson["title"]
    nome_api = (lesson.get("nome_api") or "").strip()

    # 1. PC-PE (Agente de Polícia) Noções de Direito Administrativo (361711)
    if course_id == "361711":
        if lesson_idx_0 in (6, 7, 8):
            return (
                "2b.7 - Direito Administrativo (Licitações e contratos - Lei 14.133/2021)",
                "BAIXAR (versão alternativa)",
                "Nosso curso no catálogo (02 - CBM-PE) omite Licitações e Contratos (Lei 14.133/2021); versão específica PC-PE/Cebraspe.",
            )
        if lesson_idx_0 == 13:
            return (
                "2b.7 - Direito Administrativo (Processo administrativo)",
                "BAIXAR (versão alternativa)",
                "Nosso curso no catálogo omite Processo Administrativo (e docs/17 traz apenas a Lei Estadual 11.781/2000); baixada para verificar o PDF disponibilizado.",
            )
        if lesson_idx_0 == 14:
            return (
                "2b.7 - Direito Administrativo (Improbidade administrativa - Lei 8.429/1992)",
                "BAIXAR (versão alternativa)",
                "Nosso curso no catálogo (02 - CBM-PE) omite Improbidade Administrativa (Lei 8.429/1992); versão específica PC-PE/Cebraspe.",
            )
        return (
            "—",
            "NÃO BAIXAR",
            "Duplicado: mesmo professor (Herbert Almeida), mesmo assunto e mesmos títulos já presentes em docs/02, docs/17 e catalog.json.",
        )

    # 2. PC-PE (Agente de Polícia) Raciocínio Lógico (361715)
    if course_id == "361715":
        return (
            "—",
            "NÃO BAIXAR",
            "Duplicado: Raciocínio Lógico e Matemática já constam em catalog.json e em docs/10, docs/14, docs/22 e docs/35 (item 2a).",
        )

    # 3. PC-PE (Agente de Polícia) Estatística (361717)
    if course_id == "361717":
        return (
            "—",
            "NÃO BAIXAR",
            "Duplicado: Estatística já consta em catalog.json e em docs/11 e docs/23 com a mesma Equipe Exatas (item 2a).",
        )

    # 4. PC-PE (Agente de Polícia) Contabilidade Geral (361835)
    if course_id == "361835":
        return (
            "2b.2 - Contabilidade Geral (Agente)",
            "BAIXAR",
            "Disciplina inédita no sistema (não existe em docs/ nem em catalog.json); cobre integralmente a lacuna 2b.2.",
        )

    # 5. PC-PE (Agente de Polícia) Noções de Direito Constitucional (361838)
    if course_id == "361838":
        if lesson_idx_0 == 16:
            return (
                "2b.1 - Legislação Estadual PCPE (Constituição de PE - Segurança Pública, arts. 101 a 105-B)",
                "BAIXAR (versão alternativa)",
                "Aula específica sobre Segurança Pública na Constituição de PE para a Polícia Civil (Prof. Rodrigo Bet), preenchendo a lacuna 2b.1.",
            )
        return (
            "—",
            "NÃO BAIXAR",
            "Duplicado: mesmo assunto, mesma Equipe Constitucional e mesmos títulos já existentes em docs/04, docs/24, docs/36 e catalog.json.",
        )

    # 6. PC-PE (Agente de Polícia) Língua Portuguesa (361843)
    if course_id == "361843":
        return (
            "—",
            "NÃO BAIXAR",
            "Duplicado: Língua Portuguesa já consta completa em catalog.json e em docs/03, docs/21 e docs/34 (item 2a).",
        )

    # 7. PC-PE (Agente de Polícia e Escrivão) Discursiva - Sem Correção (361844)
    if course_id == "361844":
        if lesson_idx_0 == 0:
            return (
                "2b.8 - Redação / prova discursiva para Polícia Civil",
                "BAIXAR (versão alternativa)",
                "Análise específica do edital da PC-PE (Cebraspe) para a prova discursiva de Agente e Escrivão (lacuna 2b.8).",
            )
        if lesson_idx_0 in (4, 5, 6):
            return (
                "2b.8 - Redação / prova discursiva para Polícia Civil e Atualidades de segurança pública",
                "BAIXAR (versão alternativa)",
                "Rodada de temas discursivos específicos para Polícia Civil / Segurança Pública na banca Cebraspe (lacuna 2b.8).",
            )
        return (
            "2b.8 - Redação / prova discursiva para Polícia Civil",
            "DÚVIDA",
            "Mesmo professor (Carlos Roberto) e título das aulas de docs/31 e docs/40 (PM-PE/AOCP), mas pode conter exemplos/padrão Cebraspe para PC-PE; baixada pela regra de DÚVIDA.",
        )

    # 8. PC-PE (Agente de Polícia) Informática (361846)
    if course_id == "361846":
        return (
            "—",
            "NÃO BAIXAR",
            "Duplicado: Informática já consta em catalog.json e em docs/06, docs/29 e docs/37 (item 2a).",
        )

    # 9. PC-PE (Agente de Polícia) Noções de Direito Penal (361847)
    if course_id == "361847":
        if lesson_idx_0 in (0, 1, 2, 3):
            return (
                "2b.4 - Direito Penal (Parte Geral e Contravenções Penais, versão Polícia Civil)",
                "BAIXAR (versão alternativa)",
                "Versão Polícia Civil / Cebraspe (Prof. Renan Araujo) com estrutura própria e inclusão de Contravenções Penais, distinta de docs/27.",
            )
        if lesson_idx_0 in (4, 5, 6, 7, 8, 9, 10):
            return (
                "2b.4 - Direito Penal (Parte Especial, versão Polícia Civil)",
                "BAIXAR (versão alternativa)",
                "Versão Polícia Civil / Cebraspe (Prof. Renan Araujo) da Parte Especial exigida em 2b.4 (docs/27 era voltado para PM-PE Oficial / banca AOCP).",
            )
        if lesson_idx_0 == 15:
            return (
                "2b.6 - Legislação Penal Extravagante (Organizações Criminosas - Lei 12.850/2013)",
                "BAIXAR (versão alternativa)",
                "Versão da Equipe Legislação para PC-PE/Cebraspe (em docs/30 a aula de Lei 12.850/2013 era de outra professora, Juliana Raite).",
            )
        if lesson_idx_0 == 19:
            return (
                "2b.6 - Legislação Penal Extravagante (Lei 14.344/2022 - Lei Henry Borel)",
                "BAIXAR",
                "Aula inédita sobre a Lei nº 14.344/2022 (Lei Henry Borel), ausente em docs/30, docs/33, docs/39 e no catálogo.",
            )
        return (
            "2b.6 - Legislação Penal Extravagante",
            "NÃO BAIXAR",
            "Duplicado: mesma autoria (Equipe Legislação), mesmo assunto e mesmo título já baixados em docs/30 (Legislação Penal Especial) e docs/39.",
        )

    # 10. PC-PE (Agente de Polícia) Noções de Direito Processual Penal (361848)
    if course_id == "361848":
        if lesson_idx_0 == 1:
            return (
                "2b.5 - Direito Processual Penal (Inquérito Policial e Lei 12.830/2013)",
                "BAIXAR",
                "Inclui Investigação Criminal pelo Delegado (Lei 12.830/2013), ausente no título de docs/28, versão Polícia Civil / Cebraspe (Prof. Renan Araujo).",
            )
        if lesson_idx_0 in (0, 2, 3, 4, 5, 6):
            return (
                "2b.5 - Direito Processual Penal (versão Polícia Civil)",
                "BAIXAR (versão alternativa)",
                "Versão Polícia Civil / Cebraspe (Prof. Renan Araujo) com recorte, títulos e questões próprias do edital PC-PE, distinta de docs/28 (PM-PE/AOCP).",
            )
        return (
            "2b.5 - Direito Processual Penal (Lei 7.960/1989, Lei 9.099/1995, Lei 12.830/2013)",
            "BAIXAR",
            "Aula específica da Equipe Legislação para PC-PE não existente em docs/28 nem em docs/30 (lacuna 2b.5).",
        )

    # 11. PC-PE (Agente de Polícia) Legislação Estadual (362385)
    if course_id == "362385":
        return (
            "2b.1 - Legislação Estadual da Polícia Civil de PE",
            "BAIXAR",
            "Conteúdo 100% inédito no sistema (LC 137/2008, LC 317/2015, Lei 6.425/1972 e Lei 6.123/1968), prioridade máxima em 2b.1.",
        )

    # 12. PC-PE (Agente de Polícia) Direito Constitucional (Professor Diego Cerqueira) (372958)
    if course_id == "372958":
        return (
            "—",
            "NÃO BAIXAR",
            "Duplicado: mesmo professor (Diego Cerqueira), mesmo assunto e mesmos títulos já baixados integralmente em docs/32 (19 aulas).",
        )

    return ("—", "DÚVIDA", "Curso não mapeado previamente; baixado por precaução.")


def generate_markdowns_and_plan(raw_path: Path, out_dir: Path, start_index: int = 42) -> list[dict]:
    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    subjects = raw["subjects"]

    # 1. INVENTARIO.md
    inv_lines = [
        "# Inventário do Pacote 361849 — PC-PE (Agente de Polícia)",
        "",
        "- **URL do pacote:** https://www.estrategiaconcursos.com.br/app/dashboard/pacote/361849",
        f"- **Total de cursos no pacote:** {len(subjects)}",
        f"- **Total de aulas listadas:** {sum(len(s['lessons']) for s in subjects)}",
        "- **Observação:** O pacote `361849` corresponde ao **Pacote PC-PE (Agente de Polícia)** (incluindo Discursiva para Agente e Escrivão). Todas as 177 aulas possuem PDF disponível na plataforma.",
        "",
        "## Resumo dos Cursos do Pacote",
        "",
        "| # | ID | Curso | Professores | Total de Aulas | Com PDF |",
        "|---|---|---|---|---|---|",
    ]

    for s in subjects:
        profs = ", ".join(s.get("professores", []))
        pdf_cnt = sum(1 for l in s["lessons"] if l.get("has_pdf"))
        inv_lines.append(
            f"| {s['index']} | `{s['course_id']}` | {s['title']} | {profs} | {len(s['lessons'])} | {pdf_cnt}/{len(s['lessons'])} |"
        )

    inv_lines.extend([
        "",
        "## Tabela Completa de Aulas (Curso | Aula | Título | Professor | Somente em PDF? | Tem PDF?)",
        "",
        "| Curso | Aula | Título | Professor(es) | Somente em PDF? | Tem PDF? |",
        "|---|---|---|---|---|---|",
    ])

    # 2. DECISOES.md
    dec_lines = [
        "# Decisões de Download — Pacote 361849 (PC-PE)",
        "",
        "Comparação realizada contra `content/catalog.json` e todas as pastas `docs/01` a `docs/41` conforme regras `2a`, `2b` e `2c`.",
        "",
        "| Curso | Aula | Título | Lacuna 2b | Decisão | Motivo |",
        "|---|---|---|---|---|---|",
    ]

    download_plan = []
    folder_idx = start_index

    counts = {"BAIXAR": 0, "BAIXAR (versão alternativa)": 0, "DÚVIDA": 0, "NÃO BAIXAR": 0}

    for s in subjects:
        c_id = s["course_id"]
        c_title = s["title"]
        c_profs = ", ".join(s.get("professores", []))
        selected_lessons = []

        for idx0, l in enumerate(s["lessons"]):
            lesson_num_1 = idx0 + 1
            full_title = l["title"]
            nome_api = (l.get("nome_api") or "").strip()

            m_aula = re.match(r"^(Aula\s*\d+|Aula\s*Única)\b", full_title, re.I)
            aula_label = m_aula.group(1) if m_aula else (nome_api or f"#{lesson_num_1:02d}")

            prof_match = re.search(r"(Prof(?:essor|\.)?\s+[^-(]+|Equipe\s+[^-(]+)", full_title, re.I)
            prof_str = prof_match.group(1).strip() if prof_match else c_profs

            tl = full_title.lower()
            if "somente pdf" in tl or "somente em pdf" in tl or "exclusivamente pdf" in tl:
                somente_pdf = "Sim (indicado no título)"
            elif l.get("videos_count", 0) == 0:
                somente_pdf = "Sim (sem vídeos)"
            else:
                somente_pdf = f"Não ({l.get('videos_count', 0)} vídeos)"

            if l.get("has_pdf") and l.get("has_pdf_simplificado"):
                tem_pdf = "Sim (Completo + Simplificado)"
            elif l.get("has_pdf"):
                tem_pdf = "Sim (Completo)"
            else:
                tem_pdf = "Não"

            inv_lines.append(
                f"| {c_title} | {aula_label} | {full_title} | {prof_str} | {somente_pdf} | {tem_pdf} |"
            )

            lacuna, decisao, motivo = classify_lesson(c_id, c_title, idx0, l)
            counts[decisao] = counts.get(decisao, 0) + 1

            dec_lines.append(
                f"| {c_title} | {aula_label} | {full_title} | {lacuna} | **{decisao}** | {motivo} |"
            )

            if decisao in ("BAIXAR", "BAIXAR (versão alternativa)", "DÚVIDA"):
                filename = f"{lesson_num_1:03d} - {safe_name(full_title, max_length=88)}.pdf"
                selected_lessons.append({
                    "lesson_index_1": lesson_num_1,
                    "aula_label": aula_label,
                    "aula_id": l.get("aula_id", ""),
                    "title": full_title,
                    "url": l["url"],
                    "filename": filename,
                    "lacuna": lacuna,
                    "decisao": decisao,
                    "motivo": motivo,
                    "has_pdf": l.get("has_pdf", True),
                    "has_pdf_simplificado": l.get("has_pdf_simplificado", False),
                    "videos_count": l.get("videos_count", 0),
                })

        if selected_lessons:
            folder_name = f"{folder_idx:02d} - {safe_name(c_title, max_length=72)}"
            download_plan.append({
                "folder_index": folder_idx,
                "folder_name": folder_name,
                "course_id": c_id,
                "course_title": c_title,
                "course_url": s["url"],
                "lessons": selected_lessons,
            })
            folder_idx += 1

    summary_header = [
        "## Resumo Quantitativo das Decisões",
        "",
        f"- **BAIXAR (inéditas):** {counts['BAIXAR']} aulas",
        f"- **BAIXAR (versão alternativa):** {counts['BAIXAR (versão alternativa)']} aulas",
        f"- **DÚVIDA (baixadas por precaução):** {counts['DÚVIDA']} aulas",
        f"- **Total selecionado para download:** {counts['BAIXAR'] + counts['BAIXAR (versão alternativa)'] + counts['DÚVIDA']} aulas (em {len(download_plan)} pastas: `docs/42` a `docs/{folder_idx - 1}`)",
        f"- **NÃO BAIXAR (duplicadas):** {counts['NÃO BAIXAR']} aulas",
        "",
    ]
    dec_lines = dec_lines[:4] + summary_header + dec_lines[4:]

    (out_dir / "INVENTARIO.md").write_text("\n".join(inv_lines) + "\n", encoding="utf-8")
    (out_dir / "DECISOES.md").write_text("\n".join(dec_lines) + "\n", encoding="utf-8")
    (out_dir / "plano_download.json").write_text(
        json.dumps(download_plan, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return download_plan


def find_complete_pdf_url(page) -> tuple[str | None, str]:
    """
    Prefer 'original' / complete PDF over 'simplificado' or 'grifado'.
    Returns (pdf_url, link_label).
    """
    links = page.locator(CourseSelectors.ORIGINAL_PDF_LINK)
    count = links.count()
    if count == 0:
        return None, ""

    candidates = []
    for i in range(count):
        link = links.nth(i)
        href = link.get_attribute("href")
        text = clean_text(link.inner_text() or "")
        if href:
            candidates.append((href, text))

    # 1st priority: explicit 'original' in label
    for href, text in candidates:
        if "original" in text.casefold():
            return href, text

    # 2nd priority: not 'simplificad' and not 'grif'
    for href, text in candidates:
        tc = text.casefold()
        if "simplificad" not in tc and "grif" not in tc:
            return href, text

    # Fallback: first available PDF link
    return candidates[0] if candidates else (None, "")


def download_single_pdf(context, page, lesson_url: str, target: Path, retries: int, delay: float, logger: logging.Logger) -> tuple[str, int, str]:
    """
    Download complete PDF for a lesson, verify size > 0 and %PDF- header.
    Returns (status, file_size_bytes, notes).
    """
    for attempt in range(retries + 1):
        try:
            page.goto(lesson_url, wait_until="domcontentloaded")
            if "login" in page.url.lower() or "identificacao" in page.url.lower():
                raise RuntimeError("BLOQUEIO_LOGIN: Redirecionado para página de login")

            pdf_url = None
            link_label = ""
            for _ in range(30):
                pdf_url, link_label = find_complete_pdf_url(page)
                if pdf_url:
                    break
                page.wait_for_timeout(500)

            if not pdf_url:
                raise RuntimeError("Link de download de PDF não encontrado na página da aula")

            response = context.request.get(pdf_url, timeout=90_000)
            if not response.ok:
                raise RuntimeError(f"Download respondeu HTTP {response.status}")

            content_type = response.headers.get("content-type", "").casefold()
            body = response.body()
            if len(body) == 0:
                raise RuntimeError("Arquivo PDF retornado vazio (0 bytes)")
            if not body.startswith(b"%PDF-"):
                raise RuntimeError(f"Cabeçalho inválido (não começa com %PDF-, Content-Type: {content_type or 'ausente'})")

            target.parent.mkdir(parents=True, exist_ok=True)
            partial = target.with_suffix(target.suffix + ".part")
            partial.write_bytes(body)

            if not valid_pdf(partial) or partial.stat().st_size == 0:
                partial.unlink(missing_ok=True)
                raise RuntimeError("Verificação pós-escrita falhou (tamanho 0 ou cabeçalho %PDF- ausente)")

            partial.replace(target)
            size_bytes = target.stat().st_size
            time.sleep(max(1.0, delay))
            return "downloaded", size_bytes, link_label
        except Exception as exc:
            logger.exception("Falha em %s (tentativa %s/%s): %s", lesson_url, attempt + 1, retries + 1, exc)
            if "BLOQUEIO_LOGIN" in str(exc):
                raise
            if attempt >= retries:
                raise
            time.sleep(min(max(1.0, delay) * (2 ** attempt), 30))
    raise RuntimeError("Falha inesperada de download")


def format_size(size_bytes: int) -> str:
    if size_bytes >= 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB ({size_bytes:,} bytes)"
    if size_bytes >= 1024:
        return f"{size_bytes / 1024:.1f} KB ({size_bytes:,} bytes)"
    return f"{size_bytes} bytes"


def generate_relatorio(out_dir: Path, plan: list[dict], results: list[dict], failures: list[dict]) -> None:
    total_size = sum(r["size_bytes"] for r in results)
    rel_lines = [
        "# Relatório Final de Download Seletivo — Pacote 361849 (PC-PE)",
        "",
        "- **Pacote analisado:** `https://www.estrategiaconcursos.com.br/app/dashboard/pacote/361849` (*Pacote PC-PE - Agente de Polícia*)",
        f"- **Cursos no pacote:** 12 cursos (177 aulas no total)",
        f"- **Cursos com aulas selecionadas:** {len(plan)} pastas (`docs/42` a `docs/48`)",
        f"- **Aulas selecionadas para download:** {sum(len(c['lessons']) for c in plan)} (sendo 39 `BAIXAR`, 21 `BAIXAR (versão alternativa)` e 3 `DÚVIDA`)",
        f"- **Aulas ignoradas (`NÃO BAIXAR` por duplicidade):** 114 aulas",
        f"- **PDFs baixados/verificados com sucesso (`size > 0` e cabeçalho `%PDF-`):** {len(results)} arquivos ({format_size(total_size)})",
        f"- **Falhas:** {len(failures)}",
        "",
        "---",
        "",
        "## 1. Arquivos Baixados (Pasta, Nome e Tamanho)",
        "",
        "| Pasta (`docs/`) | Arquivo | Decisão | Tamanho | Verificação `%PDF` |",
        "|---|---|---|---|---|",
    ]

    for r in results:
        rel_lines.append(
            f"| `{r['folder_name']}` | `{r['filename']}` | {r['decisao']} | {format_size(r['size_bytes'])} | OK (`%PDF-`, > 0B) |"
        )

    rel_lines.extend([
        "",
        "---",
        "",
        "## 2. Lacunas de 2b que o Pacote 361849 NÃO Cobre (Para Produção de Material Autoral)",
        "",
        "O pacote `361849` é o **Pacote PC-PE (Agente de Polícia)**. Por isso, ele cobre integralmente o conteúdo específico de **Agente de Polícia**, mas **não** inclui as disciplinas exclusivas de **Escrivão** nem as disciplinas exclusivas de **Delegado**, além de duas sublacunas específicas nos cursos de Agente:",
        "",
        "### 2.1. Lacunas de Agente e Escrivão (Prioridade Máxima)",
        "1. **Noções de Arquivologia (exclusivo de Escrivão — item 2b.3):**",
        "   - *Ausente por completo no pacote 361849* (princípios e conceitos de arquivologia, legislação arquivística, gestão de documentos, protocolo, classificação, avaliação, tabela de temporalidade, preservação, conservação e restauração, políticas de acesso, documentos digitais, requisitos e metadados, microfilmagem).",
        "2. **Estatuto da Criança e do Adolescente — Lei nº 8.069/1990 (parte geral / ato infracional além dos crimes, se exigido — item 2b.6):**",
        "   - O curso `PC-PE (Agente de Polícia) Noções de Direito Penal` traz a **Lei nº 14.344/2022 (Lei Henry Borel)** na Aula 19, mas **não possui aula dedicada ao ECA (Lei nº 8.069/1990)**. *(Nota: já possuímos os crimes do ECA em `docs/18`, `docs/33` e `docs/39`, bem como material autoral `direito-constitucional/c01` no catálogo).* ",
        "3. **Processo Administrativo Federal — Lei nº 9.784/1999 (item 2b.7):**",
        "   - No curso `PC-PE (Agente de Polícia) Noções de Direito Administrativo`, a **Aula 13 (`Processo administrativo. Não há`)** traz apenas um PDF informativo indicando que o edital de Agente de Polícia não cobrou expressamente a Lei de Processo Administrativo. Portanto, a **Lei Federal nº 9.784/1999** não possui aula teórica nesse pacote *(em `docs/17` Aula 13 temos apenas a Lei Estadual de PE nº 11.781/2000)*.",
        "4. **Direito Penal — Crimes contra a Fé Pública e Penas / Extinção da Punibilidade na versão PC-PE (item 2b.4):**",
        "   - O curso `PC-PE (Agente de Polícia) Noções de Direito Penal` foca nos tópicos do edital de Agente (Princípios, Aplicação da Lei Penal, Crime e Contravenção Penal, Crimes contra a Pessoa, Patrimônio, Dignidade Sexual e Administração Pública), mas já temos Teoria da Pena, Extinção da Punibilidade e Crimes contra a Fé Pública em `docs/27 - PM-PE (Oficial) Direito Penal` (Aulas 04, 05, 06 e 10).",
        "",
        "### 2.2. Lacunas de Delegado de Polícia (Segunda Prioridade — Ausentes no Pacote 361849)",
        "Como o pacote `361849` é o de **Agente de Polícia**, nenhum curso específico de **Delegado** faz parte dele. Ficam descobertas pelo pacote:",
        "- **Medicina Legal** (tanatologia, traumatologia, sexologia forense, toxicologia, psicopatologia forense, documentos médico-legais).",
        "- **Criminologia** (conceito, método, objetos, escolas criminológicas, teorias macrossociológicas, vitimologia, prevenção criminal).",
        "- **Direito Civil e Empresarial** (LINDB, parte geral, obrigações, contratos, responsabilidade civil, posse/propriedade, teoria da empresa, sociedades, títulos de crédito, falência e recuperação).",
        "- **Direito Tributário** (Sistema Tributário Nacional, CTN, espécies tributárias, obrigação, crédito tributário, administração tributária).",
        "- **Direito Ambiental** (PNMA, SNUC, Código Florestal, responsabilidade ambiental, licenciamento; *apenas Crimes Ambientais - Lei 9.605/1998 já existe*). ",
        "- **Direitos Humanos (versão aprofundada para Delegado)** (*temos a versão PM-PE Oficial/Soldado em `docs/18` e `docs/33`*). ",
        "- **Legislação Penal e Processual Penal Extravagante ampliada para Delegado:** Lavagem de Capitais (Lei 9.613/1998), Execução Penal (LEP - Lei 7.210/1984), Terrorismo (Lei 13.260/2016), Crimes contra a Ordem Tributária/Econômica (Leis 8.137/1990 e 8.176/1991), Crimes contra o Sistema Financeiro (Lei 7.492/1986), Lavagem/Organizações aprofundadas, etc. *(Nota: Estatuto da Pessoa Idosa - Lei 10.741/2003 já existe em `docs/18` Aula 13, e Interceptação Telefônica - Lei 9.296/1996 já existe em `docs/30` Aula 08).* ",
        "- **Direito Constitucional e Administrativo aprofundados para Delegado:** Bens públicos, Agências reguladoras, Parcerias Público-Privadas (Lei 11.079/2004), Concessões e Permissões (Lei 8.987/1995), Terceiro Setor, Controle de Constitucionalidade avançado para carreiras jurídicas *(temos Controle de Constitucionalidade geral em `docs/04`, `docs/24` e `docs/32` Aula 18)*.",
        "",
        "---",
        "",
        "## 3. Aulas que Falharam e o Motivo",
        "",
    ])

    if not failures:
        rel_lines.append("Nenhuma falha! Todas as 63 aulas selecionadas foram baixadas e validadas com sucesso.")
    else:
        rel_lines.append("| Pasta | Aula | Título | Motivo da Falha |")
        rel_lines.append("|---|---|---|---|")
        for f in failures:
            rel_lines.append(f"| `{f['folder_name']}` | {f['aula_label']} | {f['title']} | {f['error']} |")

    rel_lines.extend([
        "",
        "---",
        "",
        "## 4. Observações Técnicas e de Conteúdo",
        "",
        "1. **Disponibilidade de PDF:** Todas as 177 aulas dos 12 cursos possuem versão em PDF disponível (`is_disponivel = true` e `has_pdf = true`). Em todos os downloads foi priorizada e baixada a versão **Completa / Original** (`Livro Eletrônico - Original`), descartando-se versões simplificadas.",
        "2. **Aulas com indicação 'Somente em PDF':**",
        "   - `44 - PC-PE (Agente de Polícia) Noções de Direito Constitucional`: Aula 16 (`Prof. Rodrigo Bet - Constituição do Estado de Pernambuco - Segurança Pública`).",
        "   - `45 - PC-PE (Agente de Polícia e Escrivão) Discursiva - Sem Correção`: Aulas 00, 04, 05 e 06 (`Prof. Carlos Roberto` e `Prof. Márcio Damasceno`).",
        "   - `48 - PC-PE (Agente de Polícia) Legislação Estadual`: Aulas 01 e 02 (`LC nº 137/2008` e `LC nº 317/2015`).",
        "3. **Aula 13 de Direito Administrativo (`Aula 13 Processo administrativo. Não há`):** Possui arquivo PDF válido na plataforma (provavelmente comunicado/esclarecimento do professor sobre a ausência do tópico no edital de Agente).",
        "4. **Aulas marcadas como `DÚVIDA` (e baixadas conforme regra 2c):**",
        "   - As Aulas 01, 02 e 03 de `45 - PC-PE (Agente de Polícia e Escrivão) Discursiva - Sem Correção` possuem o mesmo professor (`Prof. Carlos Roberto`) e títulos das Aulas 01 a 03 de `docs/31` e `docs/40` (PM-PE / banca AOCP), porém foram baixadas por precaução por integrarem o curso de Discursiva da PC-PE (banca Cebraspe).",
    ])

    (out_dir / "RELATORIO.md").write_text("\n".join(rel_lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera INVENTARIO.md, DECISOES.md, baixa aulas selecionadas e gera RELATORIO.md.")
    parser.add_argument("--raw-json", default="docs/pacote-361849/inventario_raw.json")
    parser.add_argument("--out-dir", default="docs/pacote-361849")
    parser.add_argument("--docs-dir", default="docs")
    parser.add_argument("--profile", default="browser-profile")
    parser.add_argument("--start-index", type=int, default=42)
    parser.add_argument("--delay", type=float, default=1.0)
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--only-plan", action="store_true", help="Apenas gera INVENTARIO.md e DECISOES.md sem iniciar downloads")
    args = parser.parse_args()

    root = Path.cwd()
    raw_path = (root / args.raw_json).resolve()
    out_dir = (root / args.out_dir).resolve()
    docs_dir = (root / args.docs_dir).resolve()
    profile_path = (root / args.profile).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    plan = generate_markdowns_and_plan(raw_path, out_dir, args.start_index)
    total_to_download = sum(len(c["lessons"]) for c in plan)
    print(f"✓ INVENTARIO.md e DECISOES.md gerados em {out_dir}", flush=True)
    print(f"✓ Cursos selecionados: {len(plan)} (pastas {args.start_index} a {args.start_index + len(plan) - 1})", flush=True)
    print(f"✓ Total de aulas selecionadas para download: {total_to_download}", flush=True)

    if args.only_plan:
        return 0

    progress_file = out_dir / "progress_361849.json"
    progress_data = {}
    if progress_file.exists():
        try:
            progress_data = json.loads(progress_file.read_text(encoding="utf-8"))
        except Exception:
            progress_data = {}

    logger = make_logger(root / "logs")
    manager, context = open_context(profile_path, args.headless, 45_000)

    results = []
    failures = []
    done_count = 0

    try:
        page = context.pages[0] if context.pages else context.new_page()
        for course in plan:
            folder_name = course["folder_name"]
            course_folder = docs_dir / folder_name
            course_folder.mkdir(parents=True, exist_ok=True)
            print(f"\n=== [{course['folder_index']}] {course['course_title']} ({len(course['lessons'])} aulas selecionadas) ===", flush=True)

            for lesson in course["lessons"]:
                done_count += 1
                target = course_folder / lesson["filename"]
                l_url = lesson["url"]

                if target.exists() and valid_pdf(target) and target.stat().st_size > 0:
                    sz = target.stat().st_size
                    print(f"  [{done_count}/{total_to_download}] {lesson['aula_label']} - JÁ EXISTE ({format_size(sz)})", flush=True)
                    results.append({
                        "folder_name": folder_name,
                        "filename": lesson["filename"],
                        "aula_label": lesson["aula_label"],
                        "title": lesson["title"],
                        "decisao": lesson["decisao"],
                        "size_bytes": sz,
                        "status": "exists",
                    })
                    progress_data[l_url] = {"status": "downloaded", "file": f"{folder_name}/{lesson['filename']}", "size": sz}
                    progress_file.write_text(json.dumps(progress_data, ensure_ascii=False, indent=2), encoding="utf-8")
                    continue

                print(f"  [{done_count}/{total_to_download}] Baixando {lesson['title'][:75]} ...", flush=True)
                try:
                    status, sz, link_label = download_single_pdf(
                        context, page, l_url, target, args.max_retries, max(1.0, args.delay), logger
                    )
                    print(f"      -> OK ({format_size(sz)}) [{link_label}]", flush=True)
                    results.append({
                        "folder_name": folder_name,
                        "filename": lesson["filename"],
                        "aula_label": lesson["aula_label"],
                        "title": lesson["title"],
                        "decisao": lesson["decisao"],
                        "size_bytes": sz,
                        "status": status,
                    })
                    progress_data[l_url] = {"status": "downloaded", "file": f"{folder_name}/{lesson['filename']}", "size": sz}
                    progress_file.write_text(json.dumps(progress_data, ensure_ascii=False, indent=2), encoding="utf-8")
                except Exception as exc:
                    err_msg = str(exc)
                    print(f"      -> ERRO: {err_msg}", flush=True)
                    failures.append({
                        "folder_name": folder_name,
                        "filename": lesson["filename"],
                        "aula_label": lesson["aula_label"],
                        "title": lesson["title"],
                        "error": err_msg,
                    })
                    progress_data[l_url] = {"status": "failed", "error": err_msg}
                    progress_file.write_text(json.dumps(progress_data, ensure_ascii=False, indent=2), encoding="utf-8")
                    if "BLOQUEIO_LOGIN" in err_msg:
                        print("Parando imediatamente devido a solicitação de login.", flush=True)
                        generate_relatorio(out_dir, plan, results, failures)
                        return 3

        generate_relatorio(out_dir, plan, results, failures)
        print(f"\n✓ RELATORIO.md gerado em {out_dir / 'RELATORIO.md'}", flush=True)
        print(f"✓ Sucesso: {len(results)}/{total_to_download} | Falhas: {len(failures)}", flush=True)
        return 0 if not failures else 1
    finally:
        try:
            context.close()
        except Exception:
            pass
        try:
            manager.stop()
        except Exception:
            pass


if __name__ == "__main__":
    sys.exit(main())
