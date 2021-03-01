from src.score.levenshtein import levenshtein
from src.score.normalize import normalize

def main():
    distance = levenshtein("bria", "brian")
    score = normalize("bria", "brian", distance)
    print(score)

if __name__ == "__main__":
    main()

