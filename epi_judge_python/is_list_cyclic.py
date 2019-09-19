import functools
import pdb;
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def cycle_length(start_cyc):
  cyc_len = 0
  iter = start_cyc
  while True:
    cyc_len += 1
    iter = iter.next
    if iter == start_cyc:
      return cyc_len


def has_cycle(head):
  slow, fast = head, head
  # Up until fast reaches the end of the list
  while fast and fast.next and fast.next.next:
    slow, fast = slow.next, fast.next.next
    if slow is fast:
      cycle_len = cycle_length(slow)
      # Advance a pointer from the head to length C i.e. cycle length
      cycle_iter = head
      for _ in range(cycle_len):
        cycle_iter = cycle_iter.next

      # Now run two pointers: it and it + cycle_length together until they meet
      new_iter = head
      while new_iter != cycle_iter:
        new_iter = new_iter.next
        cycle_iter = cycle_iter.next

      return new_iter
  return None
@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError("Can't cycle empty list")
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError("Can't find a cycle start")
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure("Found a non-existing cycle")
    else:
        if result is None:
            raise TestFailure("Existing cycle was not found")
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    "Returned node does not belong to the cycle or is not the closest node to the head"
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            "Returned node does not belong to the cycle or is not the closest node to the head"
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_list_cyclic.py", 'is_list_cyclic.tsv', has_cycle_wrapper))
