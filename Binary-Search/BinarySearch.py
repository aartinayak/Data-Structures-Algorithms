def searchInsert(nums: list[int], target: int) -> int:

        # Initialize the start and end points for the traversal
        left, right = 0, len(nums)-1

        while left < right:
            # Compute the mid point of the section to be traversed
            mid = (left + right)//2  # Avoid the integer overflow
            
            if nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return left + 1
    
print(searchInsert([1,3,5,6], 7))    
