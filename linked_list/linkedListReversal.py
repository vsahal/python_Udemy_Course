
class Node(object):

  def __init__(self, value):
    self.value = value
    self.nextValue = None


def reverse(head):

  curent = head
  prevNode = None
  nextNode = None

  while current:

    # copy current node first before overwriting previous node
    nextNode = current.nextNode

    current.nextNode = prevNode

    prevNode = current
    current = nextNode

  return prevNode
