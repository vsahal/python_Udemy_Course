def sumNum(n):
  if len(str(n)) == 1:
    return n
  else:
    return n % 10 + sumNum(n // 10)
