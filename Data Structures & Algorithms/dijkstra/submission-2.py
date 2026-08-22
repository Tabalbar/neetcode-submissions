class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for s, d, w in edges:
            adj[s].append((w,d))

        shortestPaths = {}
        minHeap = [[0, src]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortestPaths:
                continue
            shortestPaths[n1] = w1
            for w2, n2 in adj[n1]:
                if n2 not in shortestPaths:
                    heapq.heappush(minHeap,[w1 + w2,n2])
        
        for i in range(n):
            if i not in shortestPaths:
                shortestPaths[i] = -1
        return shortestPaths
            