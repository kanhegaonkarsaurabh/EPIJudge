from test_framework import generic_test
from test_framework.test_failure import TestFailure
import sys

class Stack:
    def __init__(self):
      self.arr = []
      self.max = - sys.maxsize - 1  # Smallest int value

    def empty(self):
      return len(self.arr) == 0

    def top(self):
      return self.arr[-1]

    def max(self):
        # TODO - you fill in here.
        return 0

    def pop(self):
      if (self.empty()):
        return -1 
      
      # calculate the new max if the curr max is popped off
      if (self.top() == self.max):
        val = self.arr.pop()
        if (self.empty()):
          self.max = - sys.maxsize - 1
        else:
          self.max = max(self.arr)
        return val

      return self.arr.pop()

    def push(self, x):
      # calculate the max value before insertion
      if (self.max < x):
        self.max = x
      
      # append the x to array
      self.arr.append(x)
      return

def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
