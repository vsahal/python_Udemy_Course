def reverseStr(s):
  if len(s) == 1:
    return s[-1]
  else:
    return s[-1] + reverseStr(s[:-1])

  #another way to do this
  
 def reverseStr1(s):
  if len(s) == 1:
    return s[0]
  else:
    return reverseStr1(s[1:]) + s[0]
