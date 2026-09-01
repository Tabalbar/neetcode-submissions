class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        res = [intervals[0]]
        curr = intervals[0]

        removeCount= 0
        for i in range(1,len(intervals)):
            if intervals[i][0] < curr[1]:
                removeCount += 1
            else:
                res.append(intervals[i]) 
                curr = intervals[i]
        return removeCount