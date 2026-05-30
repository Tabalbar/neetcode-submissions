class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)
        result_dict = defaultdict(list)
        result = []


        for point in points:
            distance = math.sqrt(pow(point[0], 2)+ pow(point[1], 2))
            heapq.heappush(distances, distance)
            result_dict[distance].append(point)
            print(point)


        print(result_dict, '!!!')
        while len(result) < k:
            curr_max_distance = heapq.heappop(distances)
            result.append(result_dict[curr_max_distance][len(result_dict[curr_max_distance]) - 1])
            result_dict[curr_max_distance].pop()

        return result
