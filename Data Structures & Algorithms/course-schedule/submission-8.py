class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # preMap - map each course to preReq List
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for [crs, pre] in prerequisites:
            preMap[crs].append(pre)
        
        # visitSet = all courses along curr DFS path
        visitSet = set()
        def dfs(crs):
            # stop if crs in visit or if crs has no prereq
            if crs in visitSet:
                return False
            
            # crs has no preReq
            if preMap[crs] == []: 
                return True
            
            visitSet.add(crs)
            # run dfs on all of its prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []  # clear preReqs after runnign
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True