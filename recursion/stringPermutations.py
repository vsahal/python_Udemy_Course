
def stringPermutations(s):

  if len(s) == 0:
    return []
  if len(s) == 1:
    return [s]

  output = []

  for i in range(len(s)):
    start = s[i]

    remainderStr = s[:i] + s[i + 1:]

    for p in stringPermutations(remainderStr):
      output.append([start] + p)

  return output
