from heapq import *

class KthLargest:
    def __init__(self, k, nums):
        self.nums = nums[:k]
        self.k = k
        heapify(self.nums)
        for i in range(k, len(nums)):
            if nums[i] > self.nums[0]:
                # Push the smallest element out of the heap
                heappushpop(self.nums, nums[i])
        
    def add(self, val):
        # If the heap is not full, add the element
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        # If the heap is full, replace the smallest element
        elif val > self.nums[0]:
            heapreplace(self.nums, val)
        # Return the smallest element
        return self.nums[0]
