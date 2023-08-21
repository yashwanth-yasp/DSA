
def trap( height) -> int:
        def calc(left , right, height):
            return min(height[left - 1], height[right])*(right - left ) - sum(height[left :right]) 
        
        left , right = 0, 1
        trap = 0
        while right < len(height) - 1:
            while right < len(height) and height[right] >= height[left]:
                right += 1
            if left == 0:
                left = right
            while right < len(height) and height[right] <= height[left]:
                right += 1
            if right < len(height) and height[right] <= height[left]:
                left = left + 1
                right = left + 1
                continue 
            elif right >= len(height):
                break
            trap += calc(left, right, height)
        
        return trap

height = [4,2,0,3,2,5]
print(trap(height))