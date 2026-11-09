class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_stack = []

        for i, temp in enumerate(temperatures):
            while temp_stack and temp > temp_stack[-1][0]:
                s_temp, s_index = temp_stack.pop()
                res[s_index] = i - s_index
            temp_stack.append((temp, i))
        return res
