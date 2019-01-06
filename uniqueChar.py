
def uniqueChar(str):

    emptySet = set()

    for letters in str:
        if letters in emptySet:
            return False
        else:
            emptySet.add(letters)

    return True


print(uniqueChar('abcc'))
