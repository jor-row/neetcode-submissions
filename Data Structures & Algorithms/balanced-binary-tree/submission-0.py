# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0


        max_height = 0


        def dfs(node, height):
            nonlocal max_height
            if not node:
                max_height = max(height, max_height)
                return


            dfs(node.left, height + 1)
            dfs(node.right, height + 1)

        dfs(root, 0)

        return max_height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        found_imbalance = False


        def dfs(node):
            nonlocal found_imbalance
            if not node:
                return

            max_left_height = self.maxHeight(node.left)
            max_right_height = self.maxHeight(node.right)

            if abs(max_left_height - max_right_height) > 1:
                found_imbalance = True
                return


            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return not found_imbalance