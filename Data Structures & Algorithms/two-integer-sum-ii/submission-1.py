class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1
         
        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum  > target:
                r -= 1
            elif curr_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]

        
        # d = {}

        # for i, num in enumerate(numbers):
        #     x = target - numbers[i]

        #     if x not in d:
        #         # add num to d
        #         d[num] = i
        #     else:
        #         # x in d
        #         return [d[x] + 1, i + 1] 
