class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i in range(k):
            heapq.heappush(max_heap, (-self.distance_from_origin(points[i]), points[i]))
        for i in range(k, len(points)):
            distance = self.distance_from_origin(points[i])
            if distance < -max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-distance, points[i]))
        res = []
        for i in range(k):
            res.append(max_heap[0][1])
            heapq.heappop(max_heap)
        return res

    def distance_from_origin(self, point):
        return (point[0] - 0) ** 2 + (point[1] - 0) ** 2