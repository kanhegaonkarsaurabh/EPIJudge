from test_framework import generic_test
from list_node import ListNode

def even_odd_merge(L):
  # Trivial edge cases
  if not L:
    return None
  
  if not L.next:
    return L

  even_dummy = ListNode(0)
  odd_dummy = ListNode(0)

  heads, count = [even_dummy, odd_dummy], 0

  while L:
    heads[count].next = L
    L = L.next
    heads[count] = heads[count].next
    count = count ^ 1
  heads[1].next = None
  heads[0].next = odd_dummy.next
  return even_dummy.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
