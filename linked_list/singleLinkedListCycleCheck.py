
class Node(object):

  def __init__(self, value):
    self.value = value
    self.nextNode = None


def cycleCheck(node):

  m1 = node
  m2 = node

  while m2 != None and m2.nextNode != None:

    m1 = m1.nextNode
    m2 = m2.nextNode.nextNode

    if m2 == m1:
      return True

  return False
