from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
  is_neg = False
  if x < 0:
    is_neg = True
    x = -x

  s = ""
  if (x == 0):
    return '0'

  while x > 0:
    val = x % 10
    x = x // 10
    char = chr(ord('0') + val)
    s += char
  
  if is_neg:
    return '-' + s[::-1]

  return s[::-1]

def string_to_int(s):
  is_neg = False
  if (s.startswith('-')):
    is_neg = True
    s = s[1:]
  
  if (s == '0'):
    return 0
  pow = 0
  num = 0
  while len(s) > 0:
    char = s[len(s) - 1] 
    print (char)
    sum = (ord(char) - ord('0')) * (10 ** pow)
    num += sum
    s = s[:-1]
    pow += 1
  if (is_neg):
    return -num
  return num

def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
  exit(generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                      wrapper))
