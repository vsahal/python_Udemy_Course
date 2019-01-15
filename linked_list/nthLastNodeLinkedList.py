
class Node(object):

  def __init(self, value):
    self.value = value
    self.nextNode = None


def nthToLastNode(n, head):

  leftPointer = head
  rightPointer = head

  for i in range(n - 1):

    if not rightPointer.nextNode:
      raise LookupError('Error: n is larger than the linked list.')
    else:
      rightPointer = rightPointer.nextNode

  while rightPointer.nextNode:
    leftPointer = leftPointer.nextNode
    rightPointer = rightPointer.nextNode

  return leftPointer
