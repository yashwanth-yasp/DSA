class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # for i in range(len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        merged, duplicates = self.merge_sort(nums)
        if len(duplicates) < len(nums):
            return True
        else:
            return False
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr, arr
        mid = len(arr) // 2
        left, left_duplicates = self.merge_sort(arr[:mid])
        right, right_duplicates = self.merge_sort(arr[mid:])
        merged, duplicates = self.merge(left, right)

        duplicates.update(left_duplicates)
        duplicates.update(right_duplicates)

        return merged, duplicates

    def merge(self, left, right):
        merged = []
        duplicates = set()

        i = j = 0
        while i < len(left) and  j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            elif left[i] > right[j]:
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                merged.append(right[i])
                duplicates.add(left[i])
                i += 1
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged , duplicates
        