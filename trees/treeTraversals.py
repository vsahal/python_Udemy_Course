# vists root first then recursively vists the left sub tree
# then recursively the right sub tree


def preOrder(tree):  # recursive implementation
  if tree:
    print(tree.getRootVal())
    preorder(tree.getLeftChild())
    preorder(tree.getRightChild())


def preOrder(self):  # Method implementation
  print(self.key)
  if self.leftChild:
    self.leftChild.preOrder()
  if self.rightChild:
    self.rightChild.preOrder()


# vists the left subtree recursively then the right subtree
# recursively then in the end vists the root


def postOrder(tree):
  if tree != None:
    postOrder(tree.getLeftChild())
    postOrder(tree.getRightChild())
    print(tree.getRootVal())


# vists the left subtree recursively then the root and then
# vists the right subtree recursively


def inOrder(tree):
  if tree != None:
    inOrder(tree.getLeftChild())
    print(tree.getRootVal())
    inOrder(tree.getRightChild())
