'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
'''

from typing import List
from unittest import TestCase

def findMaxLength_wrong(nums: List[int]) -> int:
    curMax = 0
    cur1 = 0
    cur0 = 0
    for n in nums:
        if n == 0:
            cur0 += 1
        else:
            cur1 += 1
        curMax = max(min(cur0, cur1) * 2, curMax)

    return curMax

def findMaxLength_outoftime(nums: List[int]) -> int:
    curMax = 0

    for i in range(len(nums) -1 ):
        zero_count = 0
        one_count = 0
        if nums[i] == 0:
            zero_count = 1
        else:
            one_count = 1

        for j in range(i+1, len(nums)):
            if nums[j] == 0:
                zero_count += 1
            else:
                one_count += 1
            if zero_count == one_count:
                curMax = max(curMax, zero_count*2)
    
    return curMax

if __name__ == '__main__':
    test = TestCase()
    test.assertEqual(4, findMaxLength([1,0,0,1,1,1]))
    test.assertEqual(12, findMaxLength([0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0]))
    test.assertEqual(0, findMaxLength([0,0]))
    test.assertEqual(0, findMaxLength([]))
    test.assertEqual(4, findMaxLength([0,0,1,0,0,1,0,0]))
