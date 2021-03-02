from ..models.similarity_score import SimilarityScore
from ..models.string_pair import StringPair
from ..services.similarity import SimilarityService
from ..utils.matrix import create_matrix


class LevenshteinService(SimilarityService):
    def __init__(self, pair: StringPair):
        self.pair = pair

    def _levenshtein(self) -> int:
        """Applies Levenshtein's distance algorithm to the string pair.
        Sets distance attribute asan int that represents how many additions,
        modifications, and deletions one string would require to become another
        string.
        """
        # create empty matrix
        matrix = create_matrix(len(self.pair.doc_1) + 1, len(self.pair.doc_2) + 1)

        # assign the first row and column with default values

        for i in range(len(self.pair.doc_1) + 1):
            matrix[i][0] = i

        for j in range(len(self.pair.doc_2) + 1):
            matrix[0][j] = j

        # loop through each position

        for i in range(1, len(self.pair.doc_1) + 1):
            for j in range(1, len(self.pair.doc_2) + 1):
                # if the comparing letters are the same,
                # assign the same value as the previous corner

                if self.pair.doc_2[j - 1] == self.pair.doc_1[i - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                # else assign the minimum of the 3 surrounding neighbors plus 1
                else:
                    matrix[i][j] = (
                        min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j])
                        + 1
                    )

        # return the bottom corner of the matrix

        return matrix[-1][-1]

    def _normalize(self, distance: int) -> float:
        """Normalizes the Levenshtein score and returns
        the complement of the normalized ratio, rounded
        to four decimals."""
        max_distance = max(len(self.pair.doc_1), len(self.pair.doc_2))

        return round(1 - (distance / max_distance), 4)

    def get_similarity_score(self) -> SimilarityScore:
        distance = self._levenshtein()
        score = self._normalize(distance)

        return SimilarityScore(score=score)
