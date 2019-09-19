import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

def reverse_substring(s, start, end):
  while start < end:
    s[start], s[end] = s[end], s[start]
    start += 1
    end -= 1

  return s

# Assume s is a string encoded as bytearray.
def reverse_words(s):
  # Reverse the whole string first
  reverse_substring(s, 0, len(s) - 1)
 
  # Find each word now and reverse that particular word
  start, finish = 0,0
  while True:
    finish = start
    while finish < len(s) and chr(s[finish]) != ' ':
      finish += 1
   
    if (finish == len(s)):
      break

    reverse_substring(s, start, finish - 1)
    start = finish + 1
  
  reverse_substring(s, start, len(s) - 1)
  return

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
