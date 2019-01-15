def cumulativeSum(n):
  if n == 0:
    return 0
   else:
    return n + cumulativeSum(n-1)
