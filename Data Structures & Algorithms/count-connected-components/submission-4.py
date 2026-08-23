class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [1 for i in range(n)]

        def findPar(n):
            p = parents[n]

            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(n1, n2):
            p1, p2 = findPar(n1), findPar(n2)

            if ranks[p1] > ranks[p2]:
                parents[p2] = p1
                for idx,p in enumerate(parents):
                    if p == p2:
                        parents[idx] = p1
                ranks[p1] += 1
            else:
                parents[p1] = p2
                for idx,p in enumerate(parents):
                    if p == p1:
                        parents[idx] = p2
                ranks[p2] += 1

        for n1, n2 in edges:
            union(n1, n2)
        uniqueSet = set(parents)
        return len(uniqueSet)
