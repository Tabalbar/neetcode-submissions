class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        sortedIntervals = sorted(intervals, key=lambda i: i[0])
        curr = sortedIntervals[0]
        for idx in range(1,len(sortedIntervals)):
            if curr[1] < sortedIntervals[idx][0]:
                res.append(curr)
                curr = sortedIntervals[idx]
            # elif curr[0] > intervals[idx][1]: 
            #     res.append(intervals[idx])
            else:
                newInterval = [
                    min(curr[0], sortedIntervals[idx][0]),
                    max(curr[1], sortedIntervals[idx][1]),
                ]
                # res.append(newInterval)
                curr = newInterval

        res.append(curr)
        return res