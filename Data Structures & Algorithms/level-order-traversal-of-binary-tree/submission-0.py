# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        dic = {i:[] for i in range(2001)}

        if not root:
            return res

        def dfs(node, height):
            if not node:
                return

            dic[height].append(node.val)

            dfs(node.left, height + 1)
            dfs(node.right, height + 1)

        dfs(root, 0)

        for key in dic:
            val = dic[key]
            if len(val) > 0:
                res.append(val)

        return res   
        