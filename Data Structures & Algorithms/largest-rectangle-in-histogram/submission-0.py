class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            new_index = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                index_diff = i - index
                max_area = max(max_area, height * index_diff)  
                new_index = index     
            stack.append((new_index, h))
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area