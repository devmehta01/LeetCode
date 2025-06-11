class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)

        for course, p in prerequisites:
            prereqs[course].append(p)
        
        taken = set()

        def check_pre(course):
            if not prereqs[course]:
                return True
            
            if course in taken:
                return False
            
            taken.add(course)

            for p in prereqs[course]:
                if not check_pre(p):
                    return False
            
            prereqs[course] = []
            return True

        for course in range(numCourses):
            if not check_pre(course):
                return False
        
        return True