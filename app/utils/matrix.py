from typing import List


def create_matrix(rows: int, cols: int) -> List[List[float]]:
    """Takes two integers that define the dimensions of a matrix.
    Returns a matrix of 0s."""
    matrix = []
    for i in range(rows):
        arr = []
        for i in range(cols):
            arr.append(float(0))
        matrix.append(arr)
    return matrix
