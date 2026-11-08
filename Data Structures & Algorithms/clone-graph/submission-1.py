"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return node
        
        adjList = {}
        queue = deque([])
        # {1: N1[2], 2: N2[1, 3], 3: N3[]}
        def bfs(node):
            head = Node(node.val, []) 
            queue.append(node)
            adjList[node.val] = head
            while len(queue) > 0:
                curr = queue.popleft()
                currNode = adjList[curr.val]
                for neighbor in curr.neighbors:
                    if neighbor.val not in adjList:
                        newNeighbor = Node(neighbor.val, [])
                        adjList[newNeighbor.val] = newNeighbor
                        queue.append(neighbor)
                        currNode.neighbors.append(newNeighbor)
                    else:
                        currNode.neighbors.append(adjList[neighbor.val])

            return head


        head = bfs(node)
        return head