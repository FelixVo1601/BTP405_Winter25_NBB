# Write a Python function called getFibonacciNumbers(n) that generates a list of all Fibonacci numbers less than or equal to n. 
# Fibonacci numbers are defined as:
# F_0 = 0
# F_1 = 1
# F_n = F_{n-1} + F_{n-2} for n \geq 2

def getFibonacciNumbers(n):
  if n < 0:
   return []
  fib_numbers = [0,1]
  while True:
   next_fib = fib_numbers[-1] + fib_numbers[-2]
   if next_fib > n:
    break
   fib_numbers.append(next_fib)
  return fib_numbers if n >= 1 else [0]
print(getFibonacciNumbers(10))

 


