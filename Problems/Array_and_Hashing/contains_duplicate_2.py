
#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if not nums or k<0:
            return False

        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if i >= k:
                window.remove(nums[i-k])
        
        return False

