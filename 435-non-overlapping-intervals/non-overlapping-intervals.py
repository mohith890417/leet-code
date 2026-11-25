from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals by end time ascending
        intervals.sort(key=lambda x: x[1])

        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # Overlap detected: remove the current interval (it ends at or after prev_end)
                removals += 1
            else:
                # Non-overlapping: keep this interval and advance prev_end
                prev_end = end

        return removals
        