# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        # dfs function
        def dfs(r, curr):
            curr = (curr * 10) + r.val
            # base case
            if r.left is None and r.right is None:
                self.total += curr
            if r.left:
                dfs(r.left, curr)
            if r.right:
                dfs(r.right, curr)
        
        dfs(root, 0)
        return self.total

# T.C = O(n), as we are going through all nodes
# S.C = O(n), due to recursive call stack