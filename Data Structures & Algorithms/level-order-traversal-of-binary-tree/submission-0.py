# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_to_node = defaultdict(list)
        result = []

        def traversal(node, level):
            nonlocal level_to_node
            if node == None:
                return

            level_to_node[level].append(node.val)
            traversal(node.left, level + 1)
            traversal(node.right, level + 1)

        traversal(root, 0)
    
        for level in level_to_node:
            result.append(level_to_node[level])

        return result