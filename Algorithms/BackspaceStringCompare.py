'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
'''

from unittest import TestCase

def cleaner(S: str) -> str:
    lst = []
    for c in S:
        if c != '#':
            lst.append(c)
        elif len(lst) > 0:
            lst.pop()
    return ''.join(lst)

def cleaner_unfinish(S: str) -> str:
    ret_len = 0
    for i in range(len(S)):
        if S[i] != '#':
            ret_len += 1
        else:
            ret_len = max(1, ret_len-1)

        S[ret_len-1] = S[i]

    return S[:ret_len]

def backspaceCompare(S: str, T: str) -> bool:
    return cleaner(S) == cleaner(T)

if __name__ == "__main__":
    test = TestCase()

    test.assertTrue(backspaceCompare("a#c", "c"))
    test.assertTrue(backspaceCompare("a###c", "c#c"))
    test.assertTrue(backspaceCompare("a####", "c#c#"))
