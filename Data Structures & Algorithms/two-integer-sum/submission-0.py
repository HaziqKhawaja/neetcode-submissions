class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hshmp = {}
        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in hshmp:
                hshmp[nums[i]] = i
            else:
                res.append(hshmp[diff])
                res.append(i)
        return res