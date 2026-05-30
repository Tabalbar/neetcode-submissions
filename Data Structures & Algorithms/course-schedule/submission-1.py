class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: set() for i in range(numCourses)}
        visiting = set()
        classes_taken = set()

        for cls, req in prerequisites:
            adj_list[cls].add(req) 

        def dfs(crs):
            if len(adj_list[crs]) == 0 and crs not in visiting:
                return True
            if crs in visiting:
                return False

            visiting.add(crs)
            for req in adj_list[crs]:
                if not dfs(req):
                    return False
            visiting.discard(crs)
            classes_taken.add(crs)
            return True

        for crs in range(numCourses):
            if crs not in classes_taken:
                if not dfs(crs):
                    return False

        return True
                



