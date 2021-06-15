from random import choices


def read_file(filepath):
    return open(filepath, "r", encoding="utf8").read()


def get_transition_matrix(file, k):
    transition_matrix = {}

    words = file.split()

    for index, word in enumerate(words):
        if index == len(words) - k:
            break

        k_word_list = []
        for x in range(1, k + 1):
            k_word_list.append(words[index + x])
        next_k_words = ""
        for w in k_word_list:
            next_k_words += w + " "

        if word not in transition_matrix:
            transition_matrix[word] = [{next_k_words: 1}, 1]
        else:
            if words[index + 1] not in transition_matrix[word][0]:
                transition_matrix[word][0][next_k_words] = 1
            else:
                transition_matrix[word][0][next_k_words] += 1
            transition_matrix[word][1] += 1

    return transition_matrix


def select_word(transition_matrix, starting_word):
    prob_dist = transition_matrix[starting_word][0]

    words = []
    values = []
    for next_word in prob_dist:
        words.append(next_word)
        values.append(prob_dist[next_word] / transition_matrix[starting_word][1])
    return choices(words, values)[0]
