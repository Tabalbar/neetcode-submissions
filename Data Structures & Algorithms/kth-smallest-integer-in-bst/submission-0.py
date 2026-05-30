# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def merge(node):
            if node == None:
                return []

            left = merge(node.left)
            right = merge(node.right)

            return left + [node.val] + right

        sorted_array = merge(root)
        return sorted_array[k-1]