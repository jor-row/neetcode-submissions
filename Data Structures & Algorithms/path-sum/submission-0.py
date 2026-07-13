# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, sum = 0):
            if not node:
                return False

            sum += node.val
            if node.left is None and node.right is None:
                if sum == targetSum:
                    return True

            return dfs(node.left, sum) or dfs(node.right, sum)


        return dfs(root)
        