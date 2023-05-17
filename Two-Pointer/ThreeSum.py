def threeSum(nums: list[int]) -> list[list[int]]:

        triplets = []
        nums.sort()

        for i in range(len(nums)):

            left = i + 1
            right = len(nums)-1

            while left < right:

                if nums[left] + nums[right] + nums[i] == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    left += 1

        return triplets
    
print(threeSum([-1,0,1,2,-1,-4]))