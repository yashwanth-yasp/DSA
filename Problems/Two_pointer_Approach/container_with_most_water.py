

def maxArea(self ,height) -> int:
    if not height:
        return 0
    
    left = 0
    right = len(height) - 1
    area = 1
    max_area = 0

    while left < right:

        min_l = min(height[left], height[right])
        area = min_l * (right - left)
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

def main():
     arr = [1,8,6,2,5,4,8,3,7]
     print(maxArea(arr))

main()