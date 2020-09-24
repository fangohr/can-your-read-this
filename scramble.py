def pword(word):
    """Process WORD"""
    if len(word) < 4:
        return word
    else:
        raise NotImplementedError


def scramble(input):
    resulting_words = map(pword, input.split())
    result = " ".join(resulting_words)
    return result
