class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # preMap -> map courses to thier preReqs
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for [crs, pre] in prerequisites:
            preMap[crs].append(pre)
        
        res = []
        visitSet = set()
        processed = set()


        def dfs(crs):
            # stop when crs in visit - cycle exists
            if crs in visitSet:
                return False
            
            if crs in processed: # crs is already processed, just skip it
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visitSet.remove(crs) 
            processed.add(crs)  
            res.append(crs)
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res