# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        bins = []

        def dfs(node, b = ""):
            if not node:
                return

            b += f'{node.val}'

            if not node.left and not node.right:
                bins.append(b)
            else:
                dfs(node.left, b)
                dfs(node.right, b)

        dfs(root)
        print(bins)    

        res = 0

        for binary_num in bins:
            res += int(binary_num)

        return res
        