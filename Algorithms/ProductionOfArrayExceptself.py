'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

from typing import List
from unittest import TestCase
from functools import reduce


def productExceptSelf2(nums: List[int]) -> List[int]:
    p = 1
    n = len(nums)
    output = []
    for i in range(0,n):
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n-1, -1, -1):
        output[i] = p * output[i]
        p = p * nums[i]

    return output

def productExceptSelf(nums: List[int]) -> List[int]:
    product = 1
    zeros = []
    for i,n in enumerate(nums):
        if n == 0:
            zeros.append(i)
        else:
            product *= n

    if len(zeros) == 0:
        for i in range(len(nums)):
            nums[i] = int(product / nums[i])
    elif len(zeros) == 1:
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] = 0
            else:
                nums[i] = product
    else:
        nums = [0 for i in nums]
    
    return nums

if __name__ == '__main__':
    test = TestCase()
    test.assertListEqual(productExceptSelf([1,2,3,4]), [24,12,8,6])
    test.assertListEqual(productExceptSelf([]), [])
    test.assertListEqual(productExceptSelf([0,1,2]), [2,0,0])
    test.assertListEqual(productExceptSelf([0,0]), [0,0])

    test.assertListEqual(productExceptSelf2([1,2,3,4]), [24,12,8,6])
    test.assertListEqual(productExceptSelf2([]), [])
    test.assertListEqual(productExceptSelf2([0,1,2]), [2,0,0])
    test.assertListEqual(productExceptSelf2([0,0]), [0,0])

    
    
