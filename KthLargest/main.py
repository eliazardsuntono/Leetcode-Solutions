from heapq import *

class KthLargest:
    def __init__(self, k, nums):
        self.nums = nums[:k]
        self.k = k
        # Convert the list into a minheap
        heapify(self.nums)
        # This iterates thru the rest of nums and essentially keeps track of the largest kth elements
        for i in range(k, len(nums)):
            if nums[i] > self.nums[0]:
                heappushpop(self.nums, nums[i])
        
    def add(self, val):
        # The heap needs to be filled to the largest kth elements first before checking
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        # If the heap is full check and replace if necessary
        elif val > self.nums[0]:
            heapreplace(self.nums, val)
        # Returns the smallest element as that is the sorted order from nums
        return self.nums[0]
