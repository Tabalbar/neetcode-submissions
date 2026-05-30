class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                new_intervals.append(newInterval)
                return new_intervals + intervals[i:]
            elif newInterval[0] > interval[1]:
                new_intervals.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        new_intervals.append(newInterval)

        return new_intervals
        

#Input: [[1,2],[3,5],[9,10]] newInterval = [6,7]
#Result: [[1,2], [3,5], [6,7], ]