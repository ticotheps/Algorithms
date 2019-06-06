#---------------Understanding the Problem---------------

#  Objective: Find the largest positive difference between two numbers in a
#             list of 'stock prices'.
#  Expected Input: a list of stock prices.
#      Example: [1050, 270, 1540, 3800, 2]
#  Expected Output: an integer representing the largest (positive) difference between two
#                   numbers in the list.
#      Example: 3530

#  Clarifying Questions:

#  Can we assume that the list will be sorted?
#  Can we ever have a list with 0 items in it?
#  Can we ever have a list with negative numbers in it?
#  Can we assume that items in the list cannot be repeated?
#  Can we assume that all items in the list are integers?
#  Can we assume that all items in the list are floats?


#-------------------Devising a Plan----------------------

#  Iterative Approach: 


#  - Create a new empty "profits_list" that will hold all the values of the
#    different possible profits.
#  - Use a for loop to find the "profits" (positive difference) between each 
#    current_number (older price) and each compared_number (newer price) to 
#    the right of it.
#  - Store each difference (compared_number - current_number = difference) inside
#    the new empty "profits_list".
#  - Traverse the profits_list to find the largest number.
#  - Return that number.

def iterative_profit(prices):
    current_max_profit = 0
    last_index = len(prices) - 1
    list_length = len(prices)
    for i in range(0, list_length):
        if i > last_index - 1:
            break
        for j in range(i+1, list_length):
            difference = prices[j] - prices[i]
            if j > list_length:
                break
            elif prices[j] == prices[i]:
                break
            else:
                if difference > current_max_profit:
                    current_max_profit = difference
                    j += 1
                else:
                    continue
                
    return current_max_profit

print(iterative_profit([1050, 270, 1540, 3800, 2]))

    # latest_price = len(prices) - 1
    # previous_price = len(prices) - 2
    # for i in range(stock_prices[latest_price], 0):
    #     current_max_profit = 0
    #     for j in range(stock_prices[previous_price], 0):
    #         difference = stock_prices[i] - stock_prices[j]
    #         if difference > 0:
    #             if current_max_profit < difference:
    #                 current_max_profit = difference
    #             elif current_max_profit >= difference:
    #                 j -= 1
    #         elif difference < 0:
    #             pass
    #     i -= 1
    #     return current_max_profit


#     count = len(prices) - 1
#     while count >= 0:
#         print(prices[count])
#         count -= 1

# iterative_profit([1050, 270, 1540, 3800, 2])
#     difference = 0
#     newer_price = len(prices) - 1
#     older_price = len(prices) -2
#     while newer_price >= 0 and older_price >= 0:
#         # print("newer_price: ", prices[newer_price])
#         # print("older_price: ", prices[older_price])
#         difference = prices[newer_price] - prices[older_price]
#         print(difference)
#         newer_price -= 1
#         older_price -= 1

# iterative_profit([1050, 270, 1540, 3800, 2])





#  Recursive Approach: 

# import argparse

# def find_max_profit(prices):
#   pass


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))