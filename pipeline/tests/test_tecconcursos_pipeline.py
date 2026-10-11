"""Suíte de testes automatizados para o Extrator, Classificador e Pipeline TecConcursos."""
import unittest
from pathlib import Path

from pipeline.tec_extractor import (
    extract_questions_from_pdf,
    extract_all_questions_from_dir,
    TecOption,
    TecQuestion,
    _compute_hash,
)
from pipeline.edital_classifier import (
    EditalClassifier,
    ClassificationResult,
    SUBJECT_MAP,
)

ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_QUESTOES = ROOT / "docs" / "questoes"


class TestTecExtractor(unittest.TestCase):
    def test_extract_all_pdfs_not_empty(self):
        pdf_files = list(DOCS_QUESTOES.glob("*.pdf"))
        self.assertGreaterEqual(len(pdf_files), 5, "Deveria haver pelo menos 5 PDFs em docs/questoes")

    def test_pdf_extraction_integrity(self):
        # Testar com o primeiro PDF
        pdf = sorted(DOCS_QUESTOES.glob("*.pdf"))[0]
        qs = extract_questions_from_pdf(pdf)
        self.assertGreaterEqual(len(qs), 190, f"O arquivo {pdf.name} deve conter cerca de 200 questões")

        # Verificar se todas têm ID, enunciado e gabarito
        for q in qs:
            self.assertTrue(q.tec_id.isdigit(), f"ID deve ser numérico: {q.tec_id}")
            self.assertGreater(q.seq_num, 0, f"Número sequencial deve ser > 0: {q.seq_num}")
            self.assertTrue(len(q.statement) > 5, f"Enunciado muito curto na questão {q.tec_id}")
            self.assertTrue(len(q.options) >= 2, f"Questão {q.tec_id} deve ter no mínimo 2 alternativas")
            self.assertIn(q.gabarito, ["A", "B", "C", "D", "E", "Certo", "Errado", "Anulada", "C", "E"])

    def test_deduplication_and_hash(self):
        opts = [TecOption("A", "Opção 1"), TecOption("B", "Opção 2")]
        h1 = _compute_hash("Enunciado de teste", opts)
        h2 = _compute_hash("Enunciado de teste", opts)
        h3 = _compute_hash("Outro enunciado", opts)
        self.assertEqual(h1, h2, "Hashes de conteúdos idênticos devem ser iguais")
        self.assertNotEqual(h1, h3, "Hashes de conteúdos distintos devem ser diferentes")

    def test_anulada_detection(self):
        all_qs = extract_all_questions_from_dir(DOCS_QUESTOES)
        anuladas = [q for q in all_qs if q.is_anulada]
        self.assertGreater(len(anuladas), 0, "Deve haver questões anuladas identificadas no acervo")
        for q in anuladas:
            self.assertEqual(q.gabarito.lower(), "anulada")


class TestEditalClassifier(unittest.TestCase):
    def setUp(self):
        self.classifier = EditalClassifier()

    def test_subject_resolution(self):
        self.assertEqual(self.classifier.resolve_subject("Informática"), "informatica")
        self.assertEqual(self.classifier.resolve_subject("Língua Portuguesa (Português)"), "lingua-portuguesa")
        self.assertEqual(self.classifier.resolve_subject("Biologia e Biomedicina"), "biologia")
        self.assertEqual(self.classifier.resolve_subject("Direito Constitucional (CF/1988 e Doutrina)"), "direito-constitucional")
        self.assertEqual(self.classifier.resolve_subject("Direito Administrativo (Doutrina e Leis Federais)"), "direito-administrativo")

    def test_classification_result_validity(self):
        q = TecQuestion(
            tec_id="999999",
            seq_num=1,
            banca="Instituto AOCP",
            concurso="PM ES",
            cargo="Combatente",
            ano=2018,
            raw_subject="Informática",
            raw_topic="Windows 11 e Gerenciamento de Arquivos",
            statement="Considerando o Windows, assinale a alternativa sobre pastas e arquivos.",
            options=[TecOption("A", "Alt 1"), TecOption("B", "Alt 2")],
            gabarito="A",
            is_certo_errado=False,
            is_anulada=False,
            source_pdf="test.pdf",
            content_hash="mock",
        )
        res = self.classifier.classify_question(q)
        self.assertEqual(res.subject_id, "informatica")
        self.assertTrue(res.aula_id.startswith("informatica/"))
        self.assertTrue(res.segment_id.startswith("informatica/"))
        self.assertGreater(res.confidence, 0.0)


if __name__ == "__main__":
    unittest.main()
