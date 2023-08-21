
def pivotIndex(nums) -> int:
        total_sum = 0
        prefix_sum = []
        for i in range(len(nums)):
            total_sum += nums[i]
            prefix_sum.append(total_sum)
        
        print(nums)
        print(prefix_sum)
        
        if total_sum - prefix_sum[0] == 0:
              return 0
        
        for i in range(1 , len(nums) - 1):
              if total_sum - prefix_sum[i]  == prefix_sum[i - 1]:
                    return i
        
        if prefix_sum[len(nums) - 2] == 0:
              return len(nums) - 1
        
        return -1


nums = [-1,-1,1,1,0,0]
print(pivotIndex(nums))