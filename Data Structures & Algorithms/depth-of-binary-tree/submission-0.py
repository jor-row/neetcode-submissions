# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_d = 0

        def dfs(node, depth):
            nonlocal max_d
            if node is None:
                max_d = max(depth, max_d)
                return

            depth += 1
            dfs(node.right, depth)
            dfs(node.left, depth)
        

        dfs(root, 0)

        return max_d
        