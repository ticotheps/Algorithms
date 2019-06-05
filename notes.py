#  Factorial

#  Understand the Problem
#----------------------------------------------------------------------

#  n!, n must be non-negative
#  n < 1000

#----------------------------------------------------------------------

#  0! == 1
#  7! == 7 * 6 * 5 * 4 * 3 * 2 * 1

#  n! == n * (n-1)!

#  4! == 4 * (4-1)!
#  4! == 4 * 3!
#            3 * 2 * 1

#----------------------------------------------------------------------
#  Plan
#----------------------------------------------------------------------

#  Recursive Definition:

#  0! == 1
#  n! == n * (n-1)!

#  Add range checking 0...1000
#  Make sure it's an integer

#----------------------------------------------------------------------

def factorial(n):
    #  Todo: add range checking
    #  Todo: make sure it's an integer

    if n == 0:
        return 1
    
    return n * factorial(n-1)

print(factorial(40))