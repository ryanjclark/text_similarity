# text_similarity

## Scoring
### Levenshtein
I am using Levenshtein's Distance algorithm to calculate text similarity. The algorithm returns an integer that represents how many modifications (inserts, deletions, substitutions) is necessary to change one string into another string. The higher the integer from Levenshtein, the more different the strings are.

In my application, Levenshtein's Distance has O(nm) time and O(nm) space. It can be further optimized to only store part of the matrix, which can lower the space complexity to O(min(n, m)).
