# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Constraints:
#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104
#     k is in the range [1, the number of unique elements in the array].
#     It is guaranteed that the answer is unique.



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Keeps track of an element and its count.
        # Key: The number in the nums list, Value: Count(0-len(nums)).
        # Eg. {1: 3, 2: 2}
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        # Keeps track of the elements that have a particular count.
        # Each index acts as the count and we append a list of numbers that have the same count as the index to that particular position.
        # Start by initializing the array to be filled with empty lists.
        freq = [[] for i in range(len(nums)+1)]
        for num, count in count.items():
            freq[count].append(num)

        # Traverse the frequency list from the end since we want the K most frequent elements.
        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)

            if len(result) == k:
                return result
            


             

        
            

       


        


        

        

