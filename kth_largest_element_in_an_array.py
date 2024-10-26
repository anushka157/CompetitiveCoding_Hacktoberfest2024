class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
 
        k_numbers_min_heap = []

    
        for i in range(k):
            k_numbers_min_heap.append(nums[i])

  
        heapq.heapify(k_numbers_min_heap)

      
        for i in range(k, len(nums)):
       
            if nums[i] > k_numbers_min_heap[0]:
          
                heapq.heappop(k_numbers_min_heap)
               
                heapq.heappush(k_numbers_min_heap, nums[i])

        return k_numbers_min_heap[0]
