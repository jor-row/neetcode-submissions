# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
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

            
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 1 + height_left + height_right, but the max of that for every node as a "root"
        longest_diam = 0

        def dfs(node):
            nonlocal longest_diam

            if not node:
                return

            # print(self.height(node.left))
            # print(self.height(node.right))

            longest_diam = max(longest_diam, self.height(node.left) + self.height(node.right))

            dfs(node.left)
            dfs(node.right)


        dfs(root)
        return longest_diam

        