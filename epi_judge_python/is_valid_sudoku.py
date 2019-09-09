from test_framework import generic_test
from typing import List

# generate three by three regions of a sudoku to validate them
def generate_regions(input: List[List]) -> List[List]:
  region_size = 3
  regions = []
  for i in range(len(input)):
    for j in range(len(input)):
      region = []
      for (a, b) in zip(range(region_size * i, region_size * (i+1)), range(region_size * j, region_size * (j+1))):
        region.append(input[a][b])
      regions.append(region)
  return regions

def has_dup(input: List[int]) -> bool:
  # filter out all the empty places in the row
  filled = []
  for i in input:
    if i != 0:
      filled.append(i)

  # Check if there are any duplicates b/w 1,2...9
  return len(filled) != len(set(filled))

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
  # check the row and column constraints for a sudoku
  if any([has_dup(row) for row in partial_assignment]) or any([has_dup(list(col)) for col in zip(*partial_assignment)]):
    return False

  if any([has_dup(region) for region in generate_regions(partial_assignment)]):
    return False

  return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
