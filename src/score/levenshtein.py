from src.utils.matrix import create_matrix


def levenshtein(doc_1: str, doc_2: str) -> int:
    """Takes two strings and applies Levenshtein's distance algorithm.
    Returns an int that represents how many additions, modifications,
    and deletions one string would require to become another string.
    """
    # create empty matrix
    matrix = create_matrix(len(doc_1) + 1, len(doc_2) + 1)

    # assign the first row and column with default values
    for i in range(len(doc_1) + 1):
        matrix[i][0] = i
    for j in range(len(doc_2) + 1):
        matrix[0][j] = j

    # loop through each position
    for i in range(1, len(doc_1) + 1):
        for j in range(1, len(doc_2) + 1):
            # if the comparing letters are the same,
            # assign the same value as the previous corner
            if doc_2[j - 1] == doc_1[i - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            # else assign the minimum of the 3 surrounding neighbors plus 1
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]) + 1

    # return the bottom corner of the matrix
    return matrix[-1][-1]

