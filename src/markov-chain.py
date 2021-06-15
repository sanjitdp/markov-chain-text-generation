def read_file(filepath):
    return open(filepath, "r", encoding="utf8")


def get_distinct_words(file):
    distinct_words = []
    for line in file:
        words = line.split()
        for word in words:
            if word not in distinct_words:
                distinct_words.append(word)

    return distinct_words


if __name__ == "__main__":
    f = read_file("../tests/input-text/metamorphosis-kafka.txt")
    print(get_distinct_words(f))
