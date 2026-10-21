class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        h = []

        for x, y in points:
            dist = math.sqrt(x**2 + y**2) # dist of x, y from origin
            h.append([dist, x, y])
        
        heapq.heapify(h) # O(n) -> min heap with minimum at the top 
        
        res =[]
        while len(res) != k:
            dist, x, y = heapq.heappop(h)
            res.append([x, y])
        return res

# TC:
#   heapify: O(n)
#   while loop does heappop that is O(log n) and it does this k times so O(k log n)
#   total ->  O(n) + O(k log n) = O(n + k log n)
#  WC when k = len(points) - you have to return every point so k = n so O(n + n log n) === O(n log n)

# SC:
#   h stores all points so O(n)