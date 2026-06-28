class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # preMap -> map courses to thier preReqs
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for [crs, pre] in prerequisites:
            preMap[crs].append(pre)
        
        res = []
        visitSet = set() # crs in current path
        processed = set()   # crs already processed, avoid duplicacy


        def dfs(crs):

            if crs in visitSet:
                return False
            
            if crs in processed:
                return True

            visitSet.add(crs)
            
            for c in preMap[crs]:
                if not dfs(c):
                    return False
            
            visitSet.remove(crs)
            processed.add(crs)
            res.append(crs)
            return True


        for c in range(numCourses):
            if not dfs(c):
                return []
        return res

