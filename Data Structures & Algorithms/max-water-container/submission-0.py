class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            total = min(heights[l], heights[r]) * (r - l)
            res = max(total, res)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
            
        return res
