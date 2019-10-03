from test_framework import generic_test
from test_framework.test_failure import TestFailure

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        # declare the initial size
        self.size = 0
        self.max_size = k
        self.l = [0] * k
        self.front = -1
        self.rear = -1
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # check that the queue is not full
        if (self.size == self.max_size): return False
    
        # set the front to be zero on first item insertion
        if (self.rear == -1):
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
            
        self.l[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if (self.size == 0): return False
        
        
        if (self.front == self.rear): 
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size    
    
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        print ('front: ' + str(self.front))
        if (self.front == -1): return self.front
        return self.l[self.front]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if (self.rear == -1): return self.rear
        return self.l[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

class Queue:
    def __init__(self, capacity):
        # TODO - you fill in here.
        return

    def enqueue(self, x):
        # TODO - you fill in here.
        return

    def dequeue(self):
        # TODO - you fill in here.
        return 0

    def size(self):
        # TODO - you fill in here.
        return 0


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
