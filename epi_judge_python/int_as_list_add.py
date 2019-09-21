from test_framework import generic_test
from list_node import ListNode

    # Function to reverse the linked list 
def reverse(head): 
  prev = None
  current = head 
  while(current is not None): 
    next = current.next
    current.next = prev 
    prev = current 
    current = next
  return prev 

def print_list(head):
  print ("pass")
  iter = head
  while (iter):
    print (str(iter.data) + " -> ")
    iter = iter.next
 
def add_two_numbers(l0, l1):
  # Trivial case of both being null
  if (not l0 and not l1):
    return None

  # trivial case for when one of them is null 
  if (not l0):
    return l1

  if (not l1):
    return l0

  carry = 0  # Carry over for each addition

  sum_list = ListNode(0) 

  # iterate theough the two lists and calculate the sum and update the carry over
  while (l0 and l1):
    sum = l0.data + l1.data
    nodeVal = (sum + carry) % 10
    
    node = ListNode(nodeVal)
    node.next = sum_list.next
    sum_list.next = node
    
    carry = (sum + carry) // 10
    l0 = l0.next
    l1 = l1.next

  # find out which list is left to be iterated upon
  longer = None
  if (l0):
    longer = l0
  else:
    longer = l1

  while longer:
    sum = longer.data
    nodeVal = (sum + carry) % 10
    node = ListNode(nodeVal)
    node.next = sum_list.next
    sum_list.next = node
    carry = (sum + carry) // 10
    longer = longer.next
  
  # add the carry over value at the end of the list if not considered
  if (carry != 0):
    node = ListNode(carry)
    node.next = sum_list.next
    sum_list.next = node 

  return reverse(sum_list.next)
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
