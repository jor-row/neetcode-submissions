# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, level):
            if not node:
                return

            if len(res) <= level:
                res.append([])

            res[level].append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)

        dfs(root, 0)

        for i, row in enumerate(res):
            if i % 2 == 0:
                res[i] = res[i][::-1]
                print(res[i][::-1])

        return res