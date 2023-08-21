def rob( nums) -> int:
    mmax = 0
    while nums:
        potentials = []
        for i, n in enumerate(nums):
            if i == 0:
                if len(nums) == 1:
                    potentials.append(n)
                else:
                    potentials.append(n - nums[i+1])
            elif i == len(nums) - 1:
                potentials.append(n - nums[i-1])
            else:
                potentials.append(n - nums[i-1] -nums[i+1])
        print(potentials)
        print(nums)
        mx = float('-inf') 
        mxi = 0
        for i, p in enumerate(potentials):
            if p > mx: 
                mx = p
                mxi = i
        print(mxi)
        mmax += nums[mxi]
        nums = nums[:max(mxi-1, 0)] + nums[mxi+2:]
    return mmax

nums = [2,7,9,3,1]
print(rob(nums))