# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        array1 = []
        array2 = []

        def pre_order(node, arr):
            if node == None:
                arr.append(None)
                return

            arr.append(node.val)
            left = pre_order(node.left, arr)
            right = pre_order(node.right, arr)
            
        pre_order(p, array1)
        pre_order(q, array2)

        return array1 == array2