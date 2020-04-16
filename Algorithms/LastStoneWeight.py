'''
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
'''

from unittest import TestCase

from typing import List

def lastStoneWeight_slow(stones: List[int]) -> int:
    stones = sorted(stones)
    while len(stones) >= 2:
        p1 = stoens.pop()
        p2 = stones.pop()
        if p1 != p2:
            stones.append(abs(p1 - p2))
            stones = sorted(stones)
    
    if len(stones) == 1:
        return stones[0]
    
    return 0

def lastStoneWeight_fail2(stones: List[int]) -> int:
    left = 0
    right = 0
    last_left = 0
    last_right = 0

    sort_arr = sorted(stones, reverse=True)
    for s in sort_arr:
        if left + s > right + s:
            if abs(right - last_right + last_left + s - (left - last_left + last_right)) < abs(right + s - left):
                # move last left to right and add s to left
                left -= last_left
                left += last_right
                right += last_left
                right -= last_right
                last_left= last_right
            right += s
            last_right = s
        else:
            if abs(left -last_left + last_right +s - (right - last_right + last_left)) < abs(left+s - right):
                # move last right to left and add s to right
                right -= last_right
                right += last_left
                left -= last_left
                left += last_right
                last_right = last_left
            left += s
            last_left = s

    return abs(left-right)


def lastStoneWeight_failed(stones: List[int]) -> int: # not wokring for [9,7,7,6,6]
    left = 0
    right = 0
    sort_arr = sorted(stones, reverse=True)
    for s in sort_arr:
        if left + s > right + s:
            right += s
        else:
            left += s

    return abs(left-right)

def lastStoneWeight(stones: List[int]) -> int:
    left = 0
    right = 0
    last_left = 0
    last_right = 0

    sort_arr = sorted(stones, reverse=True)
    for s in sort_arr:
        # not exchange last_right and last_left
        diff_not_exchange = min(abs(left+s-right),abs(right+s-left))
        diff_exchange = min(abs(left-last_left+last_right+s-(right-last_right+last_left))
                           ,abs(right-last_right+last_left+s-(left-last_left+last_right)))
        if diff_not_exchange <= diff_exchange :
            if left + s > right + s:
                right += s
                last_right = s
            else:
                left += s
                last_left = s
        else :
            left = left + last_right - last_left
            right = right + last_left - last_right
            if left + s > right + s:
                right += s
                last_right = s
            else:
                left += s
                last_left = s

    return abs(left - right)

if __name__ == "__main__":
    test = TestCase()
    test.assertEqual(1, lastStoneWeight([2,7,4,8,1,1]))
    test.assertEqual(3, lastStoneWeight([7,6,7,6,9]))
    test.assertEqual(0, lastStoneWeight([10,7,4,5,1,9]))
    test.assertEqual(0, lastStoneWeight([9,6,6,6,4,4,3]))

