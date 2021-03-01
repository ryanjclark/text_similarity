from typing import Optional

from dataclasses import dataclass
from dataclasses_json import dataclass_json

from src.utils.matrix import create_matrix


@dataclass_json
@dataclass
class StringPair:
    doc_1: str
    doc_2: str
    distance: Optional[str] = None
    score: Optional[int] = None

    def _levenshtein(self) -> None:
        """Applies Levenshtein's distance algorithm to the string pair.
        Sets distance attribute asan int that represents how many additions,
        modifications, and deletions one string would require to become another
        string.
        """
        # create empty matrix
        matrix = create_matrix(len(self.doc_1) + 1, len(self.doc_2) + 1)

        # assign the first row and column with default values
        for i in range(len(self.doc_1) + 1):
            matrix[i][0] = i
        for j in range(len(self.doc_2) + 1):
            matrix[0][j] = j

        # loop through each position
        for i in range(1, len(self.doc_1) + 1):
            for j in range(1, len(self.doc_2) + 1):
                # if the comparing letters are the same,
                # assign the same value as the previous corner
                if self.doc_2[j - 1] == self.doc_1[i - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                # else assign the minimum of the 3 surrounding neighbors plus 1
                else:
                    matrix[i][j] = (
                        min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j])
                        + 1
                    )

        # return the bottom corner of the matrix
        self.distance = matrix[-1][-1]

    def _normalize(self) -> None:
        """Normalizes the Levenshtein score and returns
        the complement of the normalized ratio."""
        max_distance = max(len(self.doc_1), len(self.doc_2))
        self.score = round(1 - (self.distance / max_distance), 4)

    def get_similarity(self) -> int:
        self._levenshtein()
        self._normalize()
        return self.score
