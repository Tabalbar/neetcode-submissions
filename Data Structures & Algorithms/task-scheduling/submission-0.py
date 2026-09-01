class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        freq = Counter(tasks)
        timestep = -1
        max_heap = [(-freq[key], key) for key in freq]
        heapq.heapify(max_heap)

        while max_heap or queue:
            timestep += 1
            if queue and queue[0][0] == timestep:
                _, val, letter = queue.popleft()
                heapq.heappush(max_heap, (val, letter))
            if not max_heap:
                continue
            val, letter = heapq.heappop(max_heap)
            val += 1
            if val < 0:
                queue.append((timestep+n+1, val, letter))
            else:
                continue
        timestep+=1
        return timestep