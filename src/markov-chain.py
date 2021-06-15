from random import choices

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


def create_transition_matrix():
    transition_matrix = {}
    return transition_matrix


def select_word(transition_matrix, starting_sequence):
    prob_dist = transition_matrix.get(starting_sequence).getTransitionMatrix()
    words = []
    vals = []
    for k, v in prob_dist:
        words.append(k)
        vals.append(v/prob_dist.getTotal())
    return choices(words,vals)






if __name__ == "__main__":
    f = read_file("../tests/input-text/metamorphosis-kafka.txt")
    print(get_distinct_words(f))
