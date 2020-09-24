import random


def random_reordering(sequence):
    # if sequence is only one character, we'll never get a different order
    assert len(sequence) > 1
    new_order = sequence[:]
    while sequence == new_order:
        new_order = random.sample(sequence, len(sequence))
    return "".join(new_order)


def pword(word):
    """Process WORD"""
    if len(word) < 4:
        return word
    else:
        return word[0] + random_reordering(word[1:-1]) + word[-1]


def scramble(input):
    resulting_words = map(pword, input.split())
    print("resulting words = ", list(resulting_words))
    result = " ".join(list(resulting_words))
    return result


if __name__ == "__main__":
    print(scramble("Can you read this?"))
