class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # when inserting newInterval, comparing each interval to nI - 3 cases :
        # 1. new int ends before interval starts  
        #       nI.end < int.start ---- append(nI), return res + intervals[i:]
        # 2. new int starts after interval ends   
        #       nI.start > int.end  ---- append(intervals[i])
        # 3. interval overlaps 
        #    - early_start = starts at whichever one starts first -> take min
        #    - max_end = ends at whichever one ends last -> take max
        #    - newIn = [early_start, max_end]
        # after res.append(newIn) 

        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                early_start = min(newInterval[0], intervals[i][0])
                max_end =   max(newInterval[1], intervals[i][1])
                newInterval = [early_start, max_end]
        
        res.append(newInterval)
        return res  
    
    # TC: O(n)
    # SC: O(n)