'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

from unittest import TestCase
from typing import List


# what a sily answer it is
def maxProfit_sily(prices: List[int]) -> int:
    buy_point = 0
    sell_point = 0
    profit = 0

    status = 0 # not holding

    new_prices = []
    for i in range(len(prices)-1):
        if prices[i] != prices[i+1]:
            new_prices.append(prices[i])

    new_prices.append(prices[-1])
    prices = new_prices
    for i in range(len(prices)):
        if status == 0 and i < len(prices)-1:
            if (prices[i] <= prices[i+1] and i == 0) or prices[i-1] >= prices[i] < prices[i+1]:
                buy_point = i
                status = 1
                continue
        if status == 1:
            if (prices[i] > prices[i-1] and i == len(prices)-1) or prices[i-1] < prices[i] >= prices[i+1]:
                sell_point = i
                status = 0
                profit = prices[sell_point] - prices[buy_point] + profit
                continue
    
    return profit

def maxProfit(prices: List[int]) -> int:
    profit = 0
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            profit += prices[i+1] - prices[i]

    return profit

if __name__ == "__main__":
    test_case = TestCase()

    test_case.assertEqual(7, maxProfit([7,1,5,3,6,4]))
    test_case.assertEqual(4, maxProfit([1,2,3,4,5]))
    test_case.assertEqual(0, maxProfit([5,4,3,2,1]))
    test_case.assertEqual(3, maxProfit([2,3,3,5]))
    test_case.assertEqual(2, maxProfit([3,3,3,5]))
