class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort by start time
        intervals.sort(key=lambda i:i[0])

        # put first interval
        output = [intervals[0]]

        for start, end in intervals[1:]:

            # end of last interval in output
            lastEnd = output[-1][1]

            if start <= output[-1][1]:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output
            