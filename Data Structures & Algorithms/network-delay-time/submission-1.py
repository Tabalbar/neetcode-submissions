class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # BFS
        # k
        # Check if connected, if not, return -1
        ## {1: [(2, 1), (4, 4)] }
        # {2: [(3,2)]}
        # {}
        # {3: [4, 3]}

        # {1: 0, 2: 1, 4: min(3,4), 3: 2, }

        visited = set()
        queue = deque()
        timer = {}

        adjList = defaultdict(list)
        for edge in times:
            src = edge[0]
            des = edge[1]
            time = edge[2]
            adjList[src].append((src, des, time))
        # {1: 0, 2: 1}
        # (1,2,1) (1,4,4)

        def bfs(start):
            queue.append((adjList[start], 0))
            
            timer[(start)] = 0
            while len(queue) > 0:
                curr = queue.popleft()
                for edge in curr[0]:
                    src = edge[0]
                    des = edge[1]
                    time = edge[2]
                    d = curr[1]
                    if des in timer:
                        if time + d < timer[des]:
                            timer[des] = time + d
                            queue.append((adjList[des], min(time + d, timer[des])))
                    else:
                        timer[des] = time + d
                        queue.append((adjList[des], time + d))

            if len(timer) == n:
                return max(timer.values())
            else: 
                return -1

        return bfs(k)