class Solution:
    def reorganizeString(self, s: str) -> str:
        # hashmap with char -> charCount
        # make maxHeap
        # pop max freq char 
        count = Counter(s)
        maxHeap = []
        for char, cnt in count.items():
            maxHeap.append([-1 * cnt, char])
        
        heapq.heapify(maxHeap) # by default make maxHeap by first index i.e, count
        
        # pop the most freq char and check if its not the same as prev
        #       if so add to res
        prev = None
        res = ""

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            # most freq but not prev

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            
            if prev is not None:
                heapq.heappush(maxHeap, prev)
                prev = None 

            if cnt != 0:
                prev = [cnt, char]
        
        return res