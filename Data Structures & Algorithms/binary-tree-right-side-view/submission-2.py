# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes_by_level = defaultdict(list)
        result = []
        def dfs(node, level):
            if node == None:
                return
            nodes_by_level[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        

        dfs(root, 0)
        for level in sorted(nodes_by_level.keys()):
            result.append(nodes_by_level[level][-1])
        return result