from test_framework import generic_test
from stack_api import Stack

'''
  T: O(n)
  S: O(1)

  Things to remember from question: Remember lambda syntax and the comma between the parameters i.e. lambda a, b: a + b.
  Further, remember to convert the string to int and remember the order in which the operation is calculated.
'''

def evaluate(expression):
    # trivial cases
    if not expression:
      return 0
    
    operands = {
      '+': (lambda x, y: x + y),
      '-': (lambda x, y: x - y),
      '*': (lambda x, y: x * y),
      '/': (lambda x, y: x // y)
    }

    stack = Stack()

    # convert the incoming string to an array
    exp = expression.split(',')
    
    # iterate through each exp
    for e in exp:
      if e in operands:   # if operand, pop two numbers and calculate a b .
        p1 = stack.pop()
        p2 = stack.pop()
        res = operands[e](p2, p1)
        stack.push(res)
      else:               # else push the number onto stack
        val = int(e)
        stack.push(val)
    
    final_res = stack.pop()
    return final_res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
