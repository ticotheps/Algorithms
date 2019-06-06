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
    cache = {}

    def fib_inner(n):  #  O(2^n)
        nonlocal cache
        # TODO make sure n is non-negative 
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n not in cache:
            cache[n] = fib_inner(n-1) + fib_inner(n-2)
            
        return cache[n]

    return fib_inner(n)
      
    #  This for loop is REALLY slow because we are doing redundant
    #  calculations. For example, if we want the 10th Fib number, we
    #  first have to get the 9th Fib number, which requires us to get
    #  the 8th Fib number, and so forth, until we get the 0th Fib number. 
    #  HOW DO WE MAKE IT FASTER?
    #    MAKE A CACHE!
for i in range(40):
    print(f'{i}: {fib(i)}')

    