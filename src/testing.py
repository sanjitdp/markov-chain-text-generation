from markov_chain import *

if __name__ == "__main__":
    f = read_file("../tests/metamorphosis-kafka.txt")
    m = get_transition_matrix(f, 3)

    prev_word = "The"
    print(prev_word, end=" ")
    for i in range(0, 100):
        next_words = select_word(m, prev_word)
        prev_word = next_words.split()[-1]
        print(next_words, end="")
