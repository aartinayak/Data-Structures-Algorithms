"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:
1 <= nums.length <= 105
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        # Initialze a hashmap to keep a record of all the elements seen so far
        hash_map = {}

        # Iterate through all the elements
        for i in range(len(nums)):

            # If a particular number is found in the hash map, means that it must be a duplicate
            if nums[i] in hash_map:
                return True

            # Add the number to the hash map to keep a record
            else:
                hash_map[nums[i]] = 1

        return False
    
    
def main():
    
    obj = Solution()
    print(obj.containsDuplicate([1,2,3,1]))
    print(obj.containsDuplicate([1,2,3,4]))
    print(obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    
    
main()