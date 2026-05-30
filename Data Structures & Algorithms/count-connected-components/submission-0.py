class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1] * n
        num_components = n

        # Union Find
        def get_parent_and_assign(node):
            if node == parents[node]:
                return parents[node]
            else:
                parents[node] = get_parent_and_assign(parents[node])
                return parents[node]

        def union_find(curr_edge):
            p1, p2 = get_parent_and_assign(curr_edge[0]), get_parent_and_assign(curr_edge[1])
            print(p1, p2, curr_edge)
            if p1 == p2:
                return 0
            
            # Union by rank
            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
            elif ranks[p1] < ranks[p2]:
                parents[p1] = p2
            else:
                parents[p2] = p1
                ranks[p1] += 1  # Only increment rank when merging equal-rank trees

            return 1
        
        for edge in edges:
            num_components -= union_find(edge)

        return num_components