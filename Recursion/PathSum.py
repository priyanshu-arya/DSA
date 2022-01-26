# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum, 0)

    def helper(self, root, targetSum, csum):
        if root is None:
            return

        csum += root.val

        if not root.left and not root.right:
            if csum == targetSum:
                return True

        return self.helper(root.left, targetSum, csum) or self.helper(root.right, targetSum, csum)