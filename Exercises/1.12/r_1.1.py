'''
Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some 
integer i, and False otherwise. 
'''

def is_multiple(n, m):
  if m % n == 0:
    return True
  return False

print(is_multiple(2, 8))