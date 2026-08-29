class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for idx in range(len(intervals)):
            if newInterval[1] < intervals[idx][0]:
                result.append(newInterval)
                return result + intervals[idx:]
            elif newInterval[0] > intervals[idx][1]:
                result.append(intervals[idx])
            else:
                newInterval = [
                    min(newInterval[0],intervals[idx][0]),
                    max(newInterval[1],intervals[idx][1]),
                ]
        result.append(newInterval)
        return result