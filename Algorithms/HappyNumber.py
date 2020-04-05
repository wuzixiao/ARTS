'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
from unittest import TestCase
from typing import List
from functools import reduce

def isHappy(n: int) -> bool:
    path = {}

    lst = split_num(n)

    while True:
        product = reduce((lambda x, y: x+y), [ x*x for x in lst])
        if product == 1:
            return True

        if path.get(product) is None:
            path[product] = True
        else :
            return False
        lst = split_num(product)

def split_num2(n:int) -> List[int]:
    return [int(i) for i in str(n)]

def split_num(n:int) -> List[int]:
    ret = []
    while n >= 1:
        ret.insert(0, n%10)
        n = int(n/10)

    return ret

if __name__ == "__main__":
    test_case = TestCase()
    test_case.assertTrue(isHappy(7))
    test_case.assertFalse(isHappy(8))
    test_case.assertTrue(isHappy(19))
    test_case.assertListEqual(split_num(76), [7,6])
    test_case.assertListEqual(split_num2(76), [7,6])


    
