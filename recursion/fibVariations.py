
def fib1(n):
  if n == 0 or n == 1:
    return 1

  else:

    return fib1(n - 1) + fib1(n - 2)

  
  def fib2(n):

  a = 0
  b = 1
  for i in range(n):
    a, b = b, b + a

  return a
