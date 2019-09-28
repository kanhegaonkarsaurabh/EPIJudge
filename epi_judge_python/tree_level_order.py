from test_framework import generic_test


def binary_tree_depth_order(tree):
  # initialize the deoths of the nodes
  depths = []

  # queues that store nodes in a depth level
  q1 = [tree]

  while len(q1) > 0:
    depths.append([curr.data for curr in q1])

    new_nodes = []
    for nodes in q1:
      if (not nodes.left):
        new_nodes.append(nodes.left)
      if (not nodes.right):
        new_nodes.append(nodes.right)

    q1 = new_nodes

  return depths

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
