
class Queue2Stacks(object):

  def __init__(self):
    self.instack = []
    self.outstack = []

  def enque(self, item):
    self.instack.append(item)

  def deque(self):
    if not self.outstack:
      while self.instack:
        self.outstack.append(self.instack.pop())
    return self.outstack.pop()
