def removeDuplicates( nums ) -> int:
        left , right = 1, 2 

        while right < len(nums):
            if nums[left] == nums[left - 1] and nums[right] == nums[right - 1] == nums[right - 2]:
                while right < len(nums) and nums[right] == nums[right - 1]:
                    right += 1
                if right == len(nums):
                    break
            left += 1
            nums[left] = nums[right]
            right += 1
        
        return left + 1 

def main():
     nums = [0,0,1,1,1,1,2,3,3]
     print(removeDuplicates(nums))

main()