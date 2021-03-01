def normalize(doc_1: str, doc_2: str, score: int) -> float:
    """Takes two strings and their Levenshtein score and
    returns the complement of the ratio."""
    max_distance = max(len(doc_1), len(doc_2))
    return 1 - (score / max_distance)

