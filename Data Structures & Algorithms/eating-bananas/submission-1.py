class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_num = max(piles)
        start = 1
        res = max_num
        while start <= max_num:
            mid = (start + max_num ) // 2
            temp_res = 0
            for n in piles:
                temp_res += math.ceil(float(n) / mid)
            if temp_res <= h:
                res = mid
                max_num = mid - 1
            elif temp_res > h:
                start = mid + 1
        return res
