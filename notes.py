#  Factorial Example
#--------------Understand the Problem Phase--------------------

#  n!, n must be non-negative
#  n < 1000

#--------------------------------------------------------------

#  0! == 1
#  7! == 7 * 6 * 5 * 4 * 3 * 2 * 1

#  n! == n * (n-1)!

#  4! == 4 * (4-1)!
#  4! == 4 * 3!
#            3 * 2 * 1

#----------------------Planning Phase---------------------------

#  Recursive Definition:

#  0! == 1
#  n! == n * (n-1)!

#  Add range checking 0...1000
#  Make sure it's an integer

#-----------------------Implementing Phase-----------------------
#  Recursive-version of algorithm

# def factorial(n):
#     #  Todo: add range checking
#     #  Todo: make sure it's an integer

#     if n == 0:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(40))

#-----------------------Implementing Phase (Part 2)--------------
#  Non-Recursive-version of algorithm

# def factorial2(n):
#     a = 1
#     for i in range(n, 0, -1):
#         a *= i
    
#     return a 

# print(factorial2(40))








#----------------------------------------------------------------
#  Power/Exponents Example
#--------------Understand the Problem Phase----------------------

#  Write algorithm to compute a^b

#  What is the range of input?
    #  a can range from 0 to infinity
    #  b can range from 0 to infinity
#  What about fractional numbers?
    #  integer only
#  What about negative numbers?
    #  non-negative only
#  What about raising to the power of 0?
    #  n^0 == 1
#  How much memory do we have?
    #  Enough

#--------------Iterative Solution-----------------
#  2^0 == 1
#  2^4 == 2 * 2 * 2 * 2       <-- made up of 2 * 2^3
#         |----2^4----|
#         2 * |--2^3--|

#--------------Recursive Solution-----------------
#  a^0 == 1
#  a^b == a * a^(b-1)

#----------------------Planning Phase----------------------------
#  Iterative approach:

    #  O(n) time complexity
    #  O(1) space complexity

def power_iter(a, b):
    if b == 0:
        return 1

    x = a

    for i in range(b):
        x *= a

    return x

print(power_iter(2, 8))


#  Recursive approach:

    #  O(n) time complexity
    #  O(n) space complexity

def power_recursive(a, b):
    if b == 0:
        return 1

    return a * power_recursive(a, b - 1) 

print(power_recursive(10, 80))

#-----------------------Implementing Phase-----------------------