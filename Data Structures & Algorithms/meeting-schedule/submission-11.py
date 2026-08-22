"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True

        sortedIntervals = sorted(intervals, key=lambda i: i.start)
        curr = sortedIntervals[0]
        for idx in range(1, len(sortedIntervals)):
            if curr.end > sortedIntervals[idx].start:
                return False
            curr = sortedIntervals[idx]
        return True