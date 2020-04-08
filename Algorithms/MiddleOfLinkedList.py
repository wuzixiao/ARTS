'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
''' 

from unittest import TestCase

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head : ListNode) -> ListNode:
    pSlow = pFast = head
    while pFast.next is not None and pFast.next.next is not None:
        pSlow = pSlow.next
        pFast = pFast.next.next
    
    if pFast.next is None:
        return pSlow

    return pSlow.next

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6

    test = TestCase()
    test.assertEqual(4, middleNode(l1).val)