class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        min_jumps = 0
        while right < len(nums) - 1:
            max_num = 0
            for i in range(left, right + 1):
                max_num = max(max_num, i + nums[i])
            left = right + 1
            right = max_num
            min_jumps += 1
        return min_jumps
            