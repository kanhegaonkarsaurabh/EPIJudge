import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def list_length(head):
  iter = head
  length = 0
  while iter:
    length += 1
    iter = iter.next
  return length

def overlapping_no_cycle_lists(l0, l1):
  # trivial edge case to be solved first
  if ((not l0) or (not l1)):
    return None

  # Find tail of both the lists and compare them to see if they match
  i0, i1 = l0, l1
  while i0.next:
    i0 = i0.next

  while i1.next:
    i1 = i1.next

  if (i0 != i1):
    return None     # The two lists don't overlap

  # get the length of both the lists
  len0, len1 = list_length(l0), list_length(l1)

  diff, longer, shorter = 0, None, None
  if (len0 >= len1):
    diff = len0 - len1
    longer = l0
    shorter = l1
  else:
    diff = len1 - len0
    longer = l1
    shorter = l0

  # Iterate and move the longer pointer by the difference of length in the longer list
  for _ in range(diff):
    longer = longer.next

  # Run through the two lists in tandem with longer one ahead by diff. The lists will eventually overlap at common node
  while longer and shorter:
    if longer == shorter:
      return shorter
    longer = longer.next
    shorter = shorter.next

  return None

@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
