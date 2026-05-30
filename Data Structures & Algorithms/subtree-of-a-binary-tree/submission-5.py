# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        p1 = 0

        def pre_order(node, arr):
            if node == None:
                arr.append(None)
                return

            arr.append(node.val)
            pre_order(node.left, arr)
            pre_order(node.right, arr)

        pre_order(root, arr1)
        pre_order(subRoot, arr2)
        print(arr1, arr2)
        for l in range(0, len(arr1)):
            print(arr1[l: l + len(arr2)], len(arr2))
            if arr1[l: l + len(arr2)] == arr2:
                return True

        return False