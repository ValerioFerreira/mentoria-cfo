import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from segment import MAX_PAGES, MIN_PAGES, classify_pages, partition_run, runs_of  # noqa: E402


def test_partition_respects_max_pages_and_covers_everything():
    m = 100
    segs = partition_run([1.0] * m, [30.0] * m)
    assert segs[0][0] == 0 and segs[-1][1] == m
    assert all(j - i <= MAX_PAGES for i, j in segs)
    assert all(segs[k][1] == segs[k + 1][0] for k in range(len(segs) - 1))


def test_partition_prefers_topic_boundaries():
    m = 40
    pen = [30.0] * m
    for k in (13, 26):  # inícios de tópico nas páginas 13 e 26
        pen[k] = 0.0
    segs = partition_run([1.0] * m, pen)
    cuts = {i for i, _ in segs[1:]}
    assert {13, 26} <= cuts


def test_short_run_is_single_segment():
    segs = partition_run([1.0] * 4, [30.0] * 4)
    assert segs == [(0, 4)]
    assert 4 < MIN_PAGES


def test_dense_pages_get_fewer_pages_per_segment():
    light = partition_run([0.6] * 60, [30.0] * 60)
    dense = partition_run([1.3] * 60, [30.0] * 60)
    avg = lambda s: sum(j - i for i, j in s) / len(s)  # noqa: E731
    assert avg(dense) < avg(light)


def test_classify_pages_state_machine():
    pages = [{"text": ""} for _ in range(30)]
    topics = [
        {"title": "Conceitos", "kind": "heading", "pdfPage": 3, "level": 1},
        {"title": "Resumo", "kind": "marker", "pdfPage": 20, "level": 1},
        {"title": "Questões Comentadas", "kind": "marker", "pdfPage": 22, "level": 1},
        {"title": "Lista de Questões", "kind": "marker", "pdfPage": 28, "level": 1},
    ]
    types, _ = classify_pages(topics, pages, toc_max=2)
    assert types[0:2] == ["FRONT", "FRONT"]
    assert types[2] == "THEORY" and types[18] == "THEORY"
    assert types[19] == "SUMMARY"
    assert types[21] == "COMMENTED" and types[26] == "COMMENTED"
    assert types[27] == "LIST"
    assert runs_of(types, "THEORY") == [(3, 19)]
    assert runs_of(types, "COMMENTED") == [(22, 27)]
