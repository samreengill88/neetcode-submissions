class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build graph course -> pre_reqs
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        visit_set = set()

        def dfs(crs):
            # Cycle check: crs is already on the path we're currently walking.
            if crs in visit_set: 
                return False
            
            # crs has no prerequisites left to check.
            if pre_map[crs] == []:
                return True

            # Put crs on the current path ("visiting")
            visit_set.add(crs)


            # Check every prerequisite. If any of them leads to a cycle ->. return False
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            
             # All prerequisites are safe. Take crs off the current path
            visit_set.remove(crs)

             # Mark crs as "done": clearing its list
            pre_map[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True