class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1] * n
        num_components = n

        def get_and_assign_parent(node):
            if node == parents[node]:
                return parents[node]
            else:
                parents[node] = get_and_assign_parent(parents[node])
                return parents[node]

        def union(edge1, edge2):
            p1 = get_and_assign_parent(edge1)
            p2 = get_and_assign_parent(edge2)
            if p1 == p2:
                return False

            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
            elif ranks[p2] < ranks[p1]:
                parents[p1] = p2
            else:
                parents[p1] = parents[p2]
                ranks[p1] += 1

            return True

        for edge1, edge2 in edges:
            if union(edge1, edge2):
                num_components -= 1
            
        return num_components