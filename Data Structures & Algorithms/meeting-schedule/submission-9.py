"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 0:
            return True

        intervals.sort(key = lambda i: i.start)
        res_intervals = [intervals[0]]

        for interval in intervals[1:]:
            last_end = res_intervals[-1].end
            print(interval.start,  last_end)

            if interval.start < last_end:
                return False
            else:
                res_intervals.append(Interval(interval.start, interval.end))

        return True