import os

import pytest
from src.models.similarity_score import SimilarityScore
from src.models.string_pair import StringPair
from src.services.levenshtein_service import LevenshteinService

samples = []
files = [os.path.join("samples", f) for f in os.listdir("samples")]

for file in files:
    f = open(file)
    sample = f.read()
    samples.append(sample)


@pytest.mark.parametrize(
    "doc_1,doc_2,expected",
    [
        ("hey", "hi", 2),
        (samples[0], samples[1], 291),
        (samples[0], samples[2], 298),
        (samples[1], samples[2], 66),
    ],
)
def test_levenshtein(doc_1, doc_2, expected):
    pair = StringPair(doc_1=doc_1, doc_2=doc_2)
    service = LevenshteinService(pair)
    distance = service._levenshtein()
    assert distance == expected


@pytest.mark.parametrize(
    "doc_1,doc_2,expected",
    [
        ("hey", "hi", 0.3333),
        (samples[0], samples[1], 0.2988),
        (samples[0], samples[2], 0.2819),
        (samples[1], samples[2], 0.8136),
    ],
)
def test_normalize(doc_1, doc_2, expected):
    pair = StringPair(doc_1=doc_1, doc_2=doc_2)
    service = LevenshteinService(pair)
    distance = service._levenshtein()
    score = service._normalize(distance)
    assert score == expected


@pytest.mark.parametrize(
    "doc_1,doc_2,expected",
    [
        ("hey", "hi", SimilarityScore(score=0.3333)),
        (samples[0], samples[1], SimilarityScore(score=0.2988)),
        (samples[0], samples[2], SimilarityScore(score=0.2819)),
        (samples[1], samples[2], SimilarityScore(score=0.8136)),
    ],
)
def test_get_similarity(doc_1, doc_2, expected):
    pair = StringPair(doc_1=doc_1, doc_2=doc_2)
    service = LevenshteinService(pair)
    similarity_score = service.get_similarity_score()
    assert similarity_score == expected
