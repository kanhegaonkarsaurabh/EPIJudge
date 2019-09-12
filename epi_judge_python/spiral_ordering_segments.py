from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    # Initialize the starting and ending row, col indices
    a = 0
    c = 0
    b = len(square_matrix[0])
    d = len(square_matrix)

    spiral = []

    while (a < b and c < d):
      # Loop to print starting row
      for i in range(a, b):
          spiral.append(square_matrix[c][i])
      # increase the starting row pointer to print cols next
      c += 1

      # Loop to print the last column in a straight manner
      for i in range(c, d):
          spiral.append(square_matrix[i][b-1])
      b -= 1

      # Loop to print the last row in a reverse manner
      for i in range(b-1, a-1, -1):
          spiral.append(square_matrix[d-1][i])
      d -= 1

      # Loop to print the first col in a reverse manner
      for i in range(d-1, c-1, -1):
          spiral.append(square_matrix[i][a])
      a += 1

      for i in range(a, b):
          spiral.append(square_matrix[c][i])
    
    print (spiral)
    return spiral


if __name__ == '__main__':
    exit(
      generic_test.generic_test_main("spiral_ordering_segments.py",
                                      "spiral_ordering_segments.tsv",
                                      matrix_in_spiral_order))
