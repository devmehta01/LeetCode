class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        start, end = newInterval

        for i in range(len(intervals)):
            s, e = intervals[i]

            if start == -1:
                answer.append([s,e])
            elif s<start and e<start:
                answer.append([s,e])
            elif s>end:
                answer.append([start,end])
                start = end = -1
                answer.append([s,e])
            else:
                start = min(start, s)
                end = max(end, e)
        
        if start != -1:
            answer.append([start,end])
        
        return answer