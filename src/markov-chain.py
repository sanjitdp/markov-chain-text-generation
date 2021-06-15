from random import choices


class ProbabilityList:
    def __init__(self, word):
        self.next_word_probability[word] = 1
        self.total = 1

    next_word_probability = {}
    total = 0


def read_file(filepath):
    return open(filepath, "r", encoding="utf8").read()


def get_transition_matrix(file):
    transition_matrix = {}

    words = file.split()
    for index, word in enumerate(words):
        if index == len(words) - 1:
            break
        if word not in transition_matrix:
            transition_matrix[word] = ProbabilityList(words[index + 1])
        else:
            if words[index + 1] not in transition_matrix[word].next_word_probability:
                transition_matrix[word].next_word_probability[words[index + 1]] = 1
            else:
                transition_matrix[word].next_word_probability[words[index + 1]] += 1
            transition_matrix[word].total += 1

    return transition_matrix


def select_word(transition_matrix, starting_sequence):
    prob_dist = transition_matrix[starting_sequence].next_word_probability
    words = []
    vals = []
    for k in prob_dist:
        words.append(k)
        vals.append(prob_dist[k] / transition_matrix[starting_sequence].total)
    return choices(words, vals)


if __name__ == "__main__":
    f = read_file("../tests/input-text/metamorphosis-kafka.txt")
    m = get_transition_matrix(f)
    print(m)
    for i in range(0, 10):
        print(select_word(m, "email"))
