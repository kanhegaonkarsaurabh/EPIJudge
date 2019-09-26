from test_framework import generic_test
from stack_api import Stack

def shortest_equivalent_path(path):
  stack = Stack()

  # append '/' onto the stack
  stack.push('/')

  # split the path on the basis of '/'
  path_names = path.split('/')
  for name in path_names:
    if (len(name) != 0 and name != '.'):  # ignore '.' and ''
      if (name == '..'):                  # pop from the stack
        if (stack.top() == '/' or stack.top() == '..'): # if there's no dir push .. onto the stack
          stack.push(name)
        else:
          dir_ = stack.pop()
      else:
        stack.push(name)
  new_path = ''
  val = stack.pop()
  while (val != '/'):
    new_path = val + '/' + new_path
    val = stack.pop()

  # if initial path starts with '/' then push that onto the new_path
  if (path[0] == '/'):
    return val + new_path[:-1]

  return new_path[:-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
