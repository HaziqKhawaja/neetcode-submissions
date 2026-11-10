class Solution:
    def trap(self, height: List[int]) -> int:
        l = max_l = max_r = res = 0
        r = len(height) - 1
        while l <= r:
            if max_l <= max_r:
                res += 0 if max_l - height[l] < 0 else max_l - height[l]
                max_l = max(max_l, height[l])
                l += 1
            else:
                res += 0 if max_r - height[r] < 0 else max_r - height[r]
                max_r = max(max_r, height[r])
                r -= 1
        return res