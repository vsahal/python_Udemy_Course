def BinaryTree(r):
  return [r, [], []]


def insertLeft(root, newBranch):
  t = root.pop(1)

  if len(t) > 1:
    root.insert(1, [newBranch, t, []])
  else:
    root.insert(1, [newBranch, [], []])

  return root


def insertRight(root, newBranch):
  t = root.pop(2)

  if len(t) > 1:
    root.insert(2, [newBranch, [], t])
  else:
    root.insert(2, [newBranch, [], []])

  return root


def getRootVal(root):
  return root[0]

def setRootVal(root, new):
