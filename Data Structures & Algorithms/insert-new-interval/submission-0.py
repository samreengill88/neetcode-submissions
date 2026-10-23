class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # when inserting newInterval - 3 cases:
        # 1. new int ends before interval starts  
        #       nI.end < int.start ---- nI , int
        # 2. new int starts after interval ends   
        #       nI.start > int.end  ---- int, nI
        # 3. interval overlaps 

        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                early_start = min(newInterval[0], intervals[i][0])
                early_end =   max(newInterval[1], intervals[i][1])
                newInterval = [early_start, early_end]
        
        res.append(newInterval)
        return res  