# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, ps = 0):
            if not node:
                return

            if not node.right and not node.left:
                ps += node.val
                if ps == targetSum:
                    return True

            return dfs(node.left, ps + node.val) or dfs(node.right, ps + node.val)

        hasSum = dfs(root)


        return True if hasSum else False
        