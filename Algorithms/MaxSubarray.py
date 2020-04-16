'''
Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

from unittest import TestCase
from typing import List

def maxSubArray_fail(nums: List[int]) -> int:
    cur_max_start = 0
    cur_max_end = 0
    if len(nums) == 0:
        return 0
    cur_max = nums[0]
    ret = cur_max
    for i in range(len(nums)):
        if cur_max <= nums[i] <= 0:
            cur_max = nums[i]
            ret = cur_max
            continue
        if cur_max < cur_max + nums[i] > 0 :
            cur_max += nums[i]
            ret = cur_max
        elif cur_max + nums[i] > 0:
            continue
        elif cur_max + nums[i] <= 0:
            cur_max = 0

    return ret

def maxSubArray_work1(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    cur_max = nums[0]
    last_max = cur_max
    for i in nums[1:]:
        last_max = max(last_max, cur_max)
        if i > cur_max + i:
            cur_max = i
        else :
            cur_max = max(i + cur_max,i)

    return max(last_max, cur_max)

def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    
    cur_max = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i-1]+nums[i], nums[i])
        cur_max = max(cur_max, nums[i])
    
    return cur_max

if __name__ == "__main__":
    test_case = TestCase()
    test_case.assertEqual(6, maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    test_case.assertEqual(-1, maxSubArray([-2,-1,-2]))
    test_case.assertEqual(0, maxSubArray([]))
