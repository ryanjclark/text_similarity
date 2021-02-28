import os
import pytest

from src.score.levenshtein import levenshtein

samples = []
files = [os.path.join("samples", f) for f in os.listdir("samples")]

for file in files:
    f = open(file)
    sample = f.read()
    samples.append(sample)

@pytest.mark.parametrize(
        "doc_1,doc_2,expected",
        [
            (
                "hey",
                "hi",
                2
            ),
            (
                samples[0],
                samples[1],
                291
            ),
            (
                samples[0],
                samples[2],
                298
            ),
            (
                samples[1],
                samples[2],
                66
            )
        ]
)
def test_levenshtein(doc_1, doc_2, expected):
    assert levenshtein(doc_1, doc_2) == expected

