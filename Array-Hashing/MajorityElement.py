# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Constraints:
#     n == nums.length
#     1 <= n <= 5 * 104
#     -109 <= nums[i] <= 109

 
# Follow-up: Could you solve the problem in linear time and in O(1) space?

# Used the Moore Voting algorithm.
# Uses the candidate voting concept - if a particular number has a count of N/2, the others have to have a count that is less than N/2

def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0   # Tracks the current candidate

        for i in range(len(nums)):
            if count == 0: candidate = nums[i]   # Implies that the current candidate has been crossed out by the other elements
            if nums[i] != candidate: count -= 1   # There is some other number whos count has increased
            else: count += 1
        
        return candidate   # The one remaining in the end will be the one that has a count greater than N/2
