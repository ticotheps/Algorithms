#!/usr/bin/python

#---------------Understanding the Problem---------------

#  Objective: Find the largest positive difference between two numbers in a
#             list of 'stock prices'.
#  Expected Input: a list of stock prices.
#      Example: [1050, 270, 1540, 3800, 2]
#  Expected Output: an integer representing the largest (positive) difference between two
#                   numbers in the list.
#      Example: 3530

#  Clarifying Questions:
#  Can we ever have a list with 0 items in it?
#  Can we ever have a list with negative numbers in it?
#  Can we assume that all items in the list are integers?
#  Can we assume that all items in the list are floats?


#-------------------Devising a Plan----------------------

#  Iterative Approach: 
#  
#  Recursive Approach: 

import argparse

def find_max_profit(prices):
  pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))