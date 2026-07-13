# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_equal = 1

        def dfs(nodeA, nodeB):
            nonlocal is_equal
            if nodeA is None and nodeB is not None:
                is_equal = 0
                return

            if nodeA is not None and nodeB is None:
                is_equal = 0
                return

            if nodeA is None and nodeB is None:
                return

            if nodeA.val != nodeB.val:
                print("hello")
                is_equal = 0
                print(is_equal)
                return

            dfs(nodeA.right, nodeB.right)
            dfs(nodeA.left, nodeB.left)


        dfs(p,q)
        print(is_equal)

        return True if is_equal == 1 else False
        