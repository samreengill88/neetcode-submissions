class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        d = {}

        for i, num in enumerate(numbers):
            x = target - numbers[i]

            if x not in d:
                # add num to d
                d[num] = i
            else:
                # x in d
                return [d[x] + 1, i + 1]