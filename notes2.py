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

#---------Top Down/Memoization Dynamic Programming----------
#  It's called "top down" because our target value starts at the top
#  of the array when searching for that target value.

import sys

sys.setrecursionlimit(40000)

def fib(n):
    #  "memoization" => adding a cache to an algorithm
    cache = {}

    def fib_inner(n):  #  O(2^n) without cache
        nonlocal cache  #  tells python that fib_inner() wants a cache 
        #                  variable outside of the it's own scope
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
#    MAKE A CACHE! => this will improve Big O to O(n)! :)
for i in range(40):
    print(f'{i}: {fib(i)}')
    
#---------Bottom-Up Dynamic Programming----------

def fib_bottom_up(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    pprev = 0
    prev = 1
    
    i = 2
    while i < n:
        pprev, prev = prev, prev + pprev
        i += 1
    
    return prev
        
#  This is the OPTIMUM Fib sequence algorithm
for i in range(8):
    print(f'{i}: {fib_bottom_up(i)}')


#-----------------ANAGRAM EXAMPLE------------------
#  anagram = a word that, when the letters are re-arranged, forms another word.

#  example: "actors" and "costar"  <== 2 anagrams
#  example_2: "gallery", "regally", "largely", "allergy"  <== 4 anagrams
#  example_3: "abets", "baste", "betas", "beast", "beats"  <== 5 anagrams

#  Find the largest number of anagrams in a given list.

#  For all the words: 
#      -Compute the alphabetical form, make all lower-case
#      -If two words have the same alphabetical form, add 
#       those words to the set keyed on that new alphabetical form.

def anagrams_func(words):
    anagrams = {}  
      
    for word in words:
        alphabetized_form = "".join(sorted(word.lower()))
        # print(f'Word: {word}; Alphabetized_Form: {alphabetized_form}')
        
        if alphabetized_form not in anagrams:
            anagrams[alphabetized_form] = []
        
        anagrams[alphabetized_form].append(word)

f = open('words.text', 'r')
words = f.read().split("\n")
f.close()

anagrams_func(words)


    