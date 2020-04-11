'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.currentMax = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None :
            return 0
        
        self.edge(root)
        return self.currentMax
        
    def edge(self, root:TreeNode) -> int:
        if root is None:
            return 0
        
        left = self.edge(root.left)
        right = self.edge(root.right)
        self.currentMax = max(self.currentMax, left+right)
        return 1 + max(left, right)

# It is wrong to recurse dismeterOfBinaryTree(), I should recurse the edge calculation
def diameterOfBinaryTree_wrong2(root: TreeNode) -> int:
    if root is None :
        return 0
    ret = 0
    if root.left is not None:
        ret += diameterOfBinaryTree_wrong2(root.left) + 1
    if root.right is not None:
        ret += diameterOfBinaryTree_wrong2(root.right) + 1

    return ret

def diameterOfBinaryTree_wrong(root: TreeNode) -> int:
    if root.left is None and root.right is None:
        return 0
    extra = 0
    if root.left is not None:
        if root.left.left is None or root.left.right is None:
            extra += 1
    if root.right is not None:
        if root.right.left is None or root.right.right is None:
            extra += 1
    return extra + diameterOfBinaryTree_wrong(root.left) + diameterOfBinaryTree_wrong(root.right)

