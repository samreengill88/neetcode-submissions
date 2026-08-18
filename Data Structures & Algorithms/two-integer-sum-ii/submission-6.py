class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers) - 1

        while i < j:
            currSum = numbers[i] + numbers[j] # 5
            if currSum > target:
                j -= 1
            elif currSum < target:
                i += 1
            else:
                return [i + 1, j + 1]

        return []