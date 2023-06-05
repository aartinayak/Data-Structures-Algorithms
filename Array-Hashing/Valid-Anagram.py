"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
 
Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Initialze a hashmap to keep a record of all the letters per string
        hash_map = {}

        # Iterate through element of the first string
        for i in range(len(s)):

            # If the letter is seen before in the string update the count
            if s[i] in hash_map:
                hash_map[s[i]] += 1

            # Initialize the count of the letter
            else:
                hash_map[s[i]] = 1


        # Iterate through every letter of the second string
        for i in range(len(t)):

            # If the letter is seen after the first time decrement the count
            if t[i] in hash_map:
                hash_map[t[i]] -= 1

            # If a letter is observed that is not a part of the hashmap, 
            # implies that it is a totally different letter that is not present in the first string
            else:
                return False

        # Check for all the values as to check if the count is 0,
        # implying that the number of letters match with the first string
        for i in hash_map.values():

            if i > 0:
                return False

        return True
    
    
def main():
    obj = Solution()
    print(obj.isAnagram("anagram", "nagaram"))
    print(obj.isAnagram("rat", "car"))
    
main()