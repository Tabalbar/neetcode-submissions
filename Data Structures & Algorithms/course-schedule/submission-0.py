class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        parents = [i for i in range(numCourses)]
        ranks = [1 for i in range(numCourses)]
        adj_list = {i: set() for i in range(numCourses)}
        classes_taken = []
        prev = -1

        for cls, req in prerequisites:
            adj_list[cls].add(req) 

        {0: [1], 1: [0]}

        def remove_classes(classes, cls_to_remove):
            for cls in classes:
                classes[cls].discard(cls_to_remove)
            return

        while prev != len(classes_taken):
            prev = len(classes_taken)
            for cls in range(numCourses):
                if len(adj_list[cls]) == 0 and cls not in classes_taken:
                    classes_taken.append(cls)
                    remove_classes(adj_list, cls)

        if len(classes_taken) == numCourses:
            return True
        else:
            return False


