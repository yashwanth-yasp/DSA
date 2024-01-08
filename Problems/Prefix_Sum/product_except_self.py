
def productExceptSelf( nums):
    
    prefix_product = []
    postfix_product = []
    temp1, temp2 = 1, 1

    for i in range(len(nums)):
        temp1 *= nums[i]
        temp2 *= nums[len(nums) - i - 1]
        # print(temp2)
        prefix_product.append(temp1)
        postfix_product.append(temp2)

    print(prefix_product)
    print(postfix_product)
    
    for i in range(len(nums)):
        if i > 0 and i < len(nums) - 1:
            nums[i] = prefix_product[i - 1] * postfix_product[i + 1]
            print(nums[i])
        elif i == 0:
            nums[i] = postfix_product[i + 1]
        elif i == len(nums) - 1:
            nums[i] = prefix_product[i - 1]
        
    return nums

nums = [1,2,3,4]
print(nums)
print(productExceptSelf(nums))