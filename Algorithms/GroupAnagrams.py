'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

from unittest import TestCase
from typing import List

def groupAnagrames(strs: List[str]) -> List[List[str]]:
    dict_group = {}
    for s in strs:
        sort_str = ''.join(sorted(s))
        if dict_group.get(sort_str) is None:
            dict_group[sort_str] = [s]
        else:
            dict_group[sort_str].append(s)
    
    return list(dict_group.values())

if __name__ == "__main__":
    test_case = TestCase()
    result = groupAnagrames(["eat", "tea", "tan", "ate", "nat", "bat"])
    test_case.assertEqual(3, len(result))
    print(result)