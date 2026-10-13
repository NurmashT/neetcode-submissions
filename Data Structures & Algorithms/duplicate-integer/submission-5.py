class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            if n in count:
                return True
            count[n] = 1 + count.get(n, 0)
        return False