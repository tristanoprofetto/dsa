"""
Kth Largest Element - Medium

Given an integer array nums and an integer k, return the kth largest element in the array.
** Note that it is the kth largest element in the sorted order, not the kth distinct element. **

Optimal time complexity: O(nlogK)
Optimal space complexity: O(k)
"""
from collections import heapq

def kth_largest(nums, k):
    h = nums[:k]
    heapq.heapify(h)
    for i in range(k, len(nums)):
        if nums[i] > h[0]:
            heapq.heappop(h)
            heapq.heappush(h, nums[i])
    return h[0]


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(kth_largest(nums, k))