from typing import List


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        len_intervals = len(intervals)
        if len_intervals < 2:
            return intervals

        merged_intervals = []
        intervals.sort(key=lambda x: (x.start, x.end))

        for interval in intervals:
            if not merged_intervals or merged_intervals[-1].end < interval.start:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1].end = max(interval.end, merged_intervals[-1].end)

        return merged_intervals
