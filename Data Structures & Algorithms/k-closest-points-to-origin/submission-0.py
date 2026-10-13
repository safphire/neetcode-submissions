class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x, y = points[i]
            dis = math.sqrt(pow(x, 2) + pow(y, 2))
            heapq.heappush(heap, (-dis, points[i]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            dis, pts = heapq.heappop(heap)
            res.append(pts)
        return res