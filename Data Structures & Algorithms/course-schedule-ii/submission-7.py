class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # build graph
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        
        res = []
        visit_set = set()
        processed =set()

        def dfs(crs):
            # crs already in path for current course
            if crs in visit_set:
                return False 
            
            # crs is fully processed
            if crs in processed:
                return True
            
            visit_set.add(crs)

            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            
            visit_set.remove(crs)
            processed.add(crs)
            res.append(crs)
            return True





        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res