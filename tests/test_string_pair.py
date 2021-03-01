import os
import pytest

from src.model.string_pair import StringPair

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
    pair = StringPair(doc_1, doc_2)
    pair._levenshtein()
    assert pair.distance == expected


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
    pair = StringPair(doc_1, doc_2)
    pair._levenshtein()
    pair._normalize()
    assert pair.score == expected


@pytest.mark.parametrize(
    "doc_1,doc_2,expected",
    [
        ("hey", "hi", 0.3333),
        (samples[0], samples[1], 0.2988),
        (samples[0], samples[2], 0.2819),
        (samples[1], samples[2], 0.8136),
    ],
)
def test_get_similarity(doc_1, doc_2, expected):
    pair = StringPair(doc_1, doc_2)
    pair.get_similarity()
    assert pair.score == expected
