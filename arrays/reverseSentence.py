def reversedSentence1(str):

    words = []

    i = 0

    while i < len(str):
        if str[i] != ' ':
            word_start = i

            while i < len(str) and str[i] != ' ':
                i += 1

            words.append(str[word_start:i])
        i += 1

    return ' '.join(reversed(words))


def reversedSentence2(str):
    return ' '.join(x[::-1] for x in str.split())
