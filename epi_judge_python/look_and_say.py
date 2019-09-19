from test_framework import generic_test

def calc_next(s):
  s_next = ""
  i = 0
  while i < len(s):
    curr = s[i]
    count = 1
    while i+1 < len(s) and s[i+1] == curr:
      count += 1
      i += 1

    s_next += chr(ord('0') + count)
    s_next += curr
    i += 1
  return s_next

def look_and_say(n):
  # Write the function that calculates i+1 in the sequence for the given input i
  value = calc_next("1211")
  start = "1"
  
  if (n == 1):
    return start

  for i in range(1, n):
    print ('i: ' + str(i))
    start = calc_next(start)
  
  return (start)
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
