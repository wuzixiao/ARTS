'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

from unittest import TestCase
from typing import List

def singleNumber(nums: List[int]) -> int:
    ret = 0
    for n in nums:
        ret ^= n
    
    return ret

if __name__ == "__main__":
    test_case = TestCase()
    test_case.assertEqual(23^23^8, 8)
    test_case.assertEqual(singleNumber([3,4,4,4,4]), 3)
    