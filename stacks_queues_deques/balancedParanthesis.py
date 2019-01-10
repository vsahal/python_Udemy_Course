
def balanceCheck(s):

  if len(s) % 2 != 0:
    return False

  openingBrackets = set('([{')

  matches = set([('(', ')'), ('[', ']'), ('{', '}')])

  stack = []

  for paren in s:
    if paren in openingBrackets:
      stack.append(paren)

    else:
      if len(stack) == 0:
        return False

      lastOpen = stack.pop()

      if (lastOpen, paren) not in matches:
        return False

  return len(stack) == 0
