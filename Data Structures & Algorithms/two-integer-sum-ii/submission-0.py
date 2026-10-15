class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # -2 -> -1 -> 1 -> 2      target = 3
        #        l         r
        l, r = 0, len(numbers) - 1
        while l < r:
            res = numbers[l] + numbers[r]
            if res < target:
                l += 1
            elif res > target:
                r -= 1
            else:
                return [l + 1, r + 1]