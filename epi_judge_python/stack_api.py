class Stack:
    def __init__(self):
      self.arr = []

    def empty(self):
      return len(self.arr) == 0

    def top(self):
      return self.arr[-1]

    def pop(self):
      if (self.empty()):
        return -1 
      
      # calculate the new max if the curr max is popped off
      return self.arr.pop()

    def push(self, x):
      # append the x to array
      self.arr.append(x)
      return