class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        ranks = [1] * (len(edges) + 1)

        def find_and_assign_parent(node):
            if node == parents[node]:
                return parents[node]
            else:
                parents[node] = find_and_assign_parent(parents[node])
                return parents[node]

        def union(i, j):
            i_parent, j_parent = find_and_assign_parent(i), find_and_assign_parent(j)
            if i_parent == j_parent:
                return False

            if ranks[i_parent] > ranks[j_parent]:
                parents[j_parent] = i
            elif ranks[i_parent] < ranks[j_parent]:
                parents[i_parent] = j
            else:
                parents[i_parent] = j
                ranks[j_parent]+=1

            return True

        for i, j in edges:
            if not union(i, j):
                return [i,j]




        