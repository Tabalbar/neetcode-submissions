# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if not left or not right:
                return None

            root = TreeNode(val=left[0])
            mid = right.index(left[0])
            root.left = build(left[1: mid+1], right[:mid])
            root.right = build(left[mid+1:], right[mid + 1:])
            return root

        root = build(preorder, inorder)
        return root
