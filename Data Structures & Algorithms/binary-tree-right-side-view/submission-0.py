# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = [[] for i in range(1001)]

        def dfs(node, level=0):
            if not node:
                return

            dfs(node.left, level + 1)
            levels[level].append(node.val)
            dfs(node.right, level + 1)
        dfs(root)
        res = []
        for level in levels:
            if len(level):
                res.append(level[-1])
      
        return res