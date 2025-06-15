class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort()

        start_prev, end_prev = intervals[0]

        for i in range(1, len(intervals)):
            s, e = intervals[i]

            if end_prev < s:
                answer.append([start_prev, end_prev])
                start_prev = s
                end_prev = e
            else:
                end_prev = max(e, end_prev)
        
        answer.append([start_prev, end_prev])
        
        return answer