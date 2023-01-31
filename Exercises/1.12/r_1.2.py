"""
Write a short Python function, is_even(k), that takes an integer
value and returns True if k is even, and False otherwise. However, 
your function cannot use the multiplication, modulo, or division operators. 
"""

def is_even(k):
  return(k & 1)

k = 4
if (is_even(k) == 0):
  print("Even")
else: 
  print("Odd")