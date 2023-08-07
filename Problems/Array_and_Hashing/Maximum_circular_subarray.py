
def maxSubarraySumCircular( nums) -> int:
    def kadane(nums):
        max_sum = curr_sum = nums[0]
        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
    
    n = len(nums)
    
    max_kadane = kadane(nums)
    total_sum = sum(nums)
    
    for i in range(n):
        nums[i] *= -1
        
    min_kadane = kadane(nums)
    max_circular = total_sum + min_kadane
    
    return max(max_kadane, max_circular) if max_kadane > 0 else max_kadane

def main():
    nums = [5,-3,5]
    print(maxSubarraySumCircular(nums))

main()