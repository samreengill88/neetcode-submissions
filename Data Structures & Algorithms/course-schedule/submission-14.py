class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build graph
        adj_lst = defaultdict(list)
        for crs, pre in prerequisites:
            adj_lst[crs].append(pre)
        
        visit = set()

        def dfs(crs):
            #  stop if crs in visit -> means it is a cycle
            if crs in visit:
                return False 
            
            if adj_lst[crs] == []: # crs has no preReq left 
                return True 
            
            visit.add(crs)
        
            for pre in adj_lst[crs]:
                if not dfs(pre):
                    return False 
            
            # mark crs as done
            visit.remove(crs)
            adj_lst[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


