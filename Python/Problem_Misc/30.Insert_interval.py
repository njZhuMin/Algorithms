"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        results = []
        if intervals is None or len(intervals) == 0:
            if newInterval:
                results.append(newInterval)
            return results

        insertPos = 0
        for it in intervals:
            if newInterval.end < it.start:
                # case 1: [new], [old]
                results.append(it)
            elif it.end < newInterval.start:
                # case 2: [old], [new]
                results.append(it)
                insertPos += 1
            else:
                # case 3,4: [old, new] or [new, old]
                newInterval.start = min(newInterval.start, it.start)
                newInterval.end = max(newInterval.end, it.end)

        results.insert(insertPos, newInterval)
        return results

