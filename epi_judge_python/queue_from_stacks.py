from test_framework import generic_test

class AQueue:
    def __init__(self):
      self._s1 = []
      self._s2 = []

    '''
      Time: O(1)
    '''
    def enqueue(self, x):
      self._s1.append(x)
      return

    '''
      Time: O(m) where m is the number of el in the queue as of now
    '''
    def dequeue(self):
      if len(self._s2) == 0:
        while (len(self._s1) > 1):
          v = self._s1.pop()
          self._s2.append(v)
        return self._s1.pop()
      else:
        return self._s2.pop()

def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = AQueue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = AQueue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
