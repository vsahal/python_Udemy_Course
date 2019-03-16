def permute (a, lo, hi):
  if (lo == hi):
    print (a)
  else:
    for i in range (lo, hi):
      a[i], a[lo] = a[lo], a[i]
      permute (a, lo + 1, hi)
      a[i], a[lo] = a[lo], a[i]

def sub_sets (a, b, idx):
  if (idx == len(a)):
    print (b)
    return
  else:
    c = b[:]
    b.append (a[idx])
    sub_sets (a, b, idx + 1)
    sub_sets (a, c, idx + 1)
