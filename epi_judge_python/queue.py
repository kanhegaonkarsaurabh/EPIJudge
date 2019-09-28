'''
  Queue implementation in python3 using deque in collections
'''

class Queue:
  def __init__(self):
    arr = collections.deque()

  # O(1)
  def enqueue(self, x):
    return self.arr.append(x)

  # O(1)
  def dequeue():
    return self.arr.popleft()

  # O(1)
  def empty():
    return len(arr) == 0
