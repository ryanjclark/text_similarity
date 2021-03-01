from src.model.string_pair import StringPair


def main():
    example_pair = StringPair("brian", "ryan")
    score = example_pair.get_similarity()
    print(score)


if __name__ == "__main__":
    main()
