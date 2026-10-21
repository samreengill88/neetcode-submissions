class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # example: pos=[10,8,0,5,3] spd=[2,4,1,1,3]
        # get pairs of pos, speed
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        # pairs = [(10,2), (8,4), (0,1), (5,1), (3,3)]
        # sort by position -> largest pos first 
        pairs.sort(reverse=True)

        stack = []
        for p, s in pairs:
            # calculate time for pair to get to destination
            # push time to stack
            time = (target - p) / s
            stack.append(time)

            # check if time to reach dest on top of stack is less than second top on stack -> merge times so pop
            if len(stack)>= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
            # now at the end stack has times for each pos to reach destination that could not be merged  
        return len(stack) 

# TC: building pairs-> O(n)
#       sort pairs ->  O(n log n)
#       for loop -> O(n)
# total = O(n) + O(n log n) + O(n) = O(n log n)

# SC: n tuples -> O(n)
#     stack -> wc no merge so O(n)
# Total: O(n)