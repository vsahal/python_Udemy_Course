def anagramCheck2(str1, str2):

    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    dictStr1 = {}
    dictStr2 = {}

    for letters in str1:

        if letters not in dictStr1:
            dictStr1[letters] = 1
        else:
            dictStr1[letters] += 1

    for letters in str2:

        if letters not in dictStr2:
            dictStr2[letters] = 1
        else:
            dictStr2[letters] += 1

    return (dictStr1 == dictStr2)

