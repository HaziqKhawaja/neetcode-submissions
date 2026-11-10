class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_count = defaultdict(int)
        for num in nums:
            int_count[num] += 1
        freq_array = [[] for i in range(len(nums) + 1)]
        for num, frequency in int_count.items():
            freq_array[frequency].append(num)
        res = []
        for num_group in reversed(freq_array):
            for num in num_group:
                res.append(num)
                if len(res) == k:
                    return res