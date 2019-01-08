
class Queue(object):

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    self.items.pop()

  def size(self):
    return len(self.items)


q = Queue()
q.size()
print(q.enqueue(1))
print(q.enqueue(2))
print(q.isEmpty())
print(q.dequeue())
print(q.size())
print(q())
