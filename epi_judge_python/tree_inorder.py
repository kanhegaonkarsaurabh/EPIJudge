from test_framework import generic_test

def inorder_traversal_helper(tree, order):
  if (not tree):
    return order

  return inorder_traversal_helper(tree.left, order) + [tree.data] + inorder_traversal_helper(tree.right, order)

def inorder_traversal(tree):
  return inorder_traversal_helper(tree, [])

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))
