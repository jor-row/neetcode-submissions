class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for num in nums:
            if num in freqMap.keys():
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        
        heap = []

        for key in freqMap.keys():
            heapq.heappush(heap, (freqMap[key], key))
            if len(heap) > k:
                 heapq.heappop(heap)
        
        return [n[1] for n in heap]

        