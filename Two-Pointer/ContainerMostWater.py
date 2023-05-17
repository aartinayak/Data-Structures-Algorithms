def maxArea(height: list[int]) -> int:

        maxArea = 0
        left, right = 0, len(height)-1

        while left < right:
            
            currArea = (right-left) * (min(height[left], height[right]))

            if currArea > maxArea:
                maxArea = currArea

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return maxArea
    
    
print(maxArea([1,8,6,2,5,4,8,3,7]))