class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        res = 0
        starting_seqs = []
        for n in nums:
            temp_max = 1
            if n-1 not in hs:
                i = n
                while i + 1 in hs:
                    temp_max += 1
                    i += 1
                res = max(res, temp_max)
        return res
