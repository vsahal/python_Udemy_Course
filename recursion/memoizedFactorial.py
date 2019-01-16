
def memFactorial(n):

  factorialDict = {}

  if k == 0:
    return 1

  if k == 1:
    return 1

  if k not in factorialDict:
    factorialDict[k] = k * memFactorial(k - 1)

  return factorialDict[k]
