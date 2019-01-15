def reverseStr(s):
  if len(s) == 1:
    return s[-1]
  else:
    return s[-1] + reverseStr(s[:-1])
