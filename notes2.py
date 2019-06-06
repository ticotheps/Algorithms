#  Fibonacci Sequence

#  Write a function that computes the nth Fibonacci number.

#----------Clarifying the Problem------------

#  n is a non-negative integer

#----------Understand the Problem------------

#  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...]
#  F(0) = 0
#  F(1) = 1
#  F(n) = F(n-1) + F(n-2)

#  F(8) = 21

#--------------Devise a Plan-----------------

def fib(n):
    # TODO make sure n is non-negative 
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)
  
for i in range(40):
    print(f'{i}: {fib(i)}')
    