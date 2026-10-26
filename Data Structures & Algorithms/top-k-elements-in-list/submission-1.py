class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        # Step 2: Initialize a min-heap
        min_heap = []
        
        # Step 3: Push (frequency, number) pairs into the heap and keep its size at k
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Pops the smallest frequency
                
        # Step 4: Extract just the numbers from the heap
        return [num for freq, num in min_heap]
        