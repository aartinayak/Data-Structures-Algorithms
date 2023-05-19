"""
Problem:

Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
 
Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Initialize a hash map to map the string letters.
        hash_map = {}

        # Iterate through the letters of both the strings simultaneously.
        for (i, j) in zip(s, t):

            # Map the letters from the s string as the key and the ones from string t as values.
            
            # If a key does not exist already in the hash map.
            if i not in hash_map:
                
                # We check if the value is not already mapped to some other key.
                if j not in hash_map.values():
                    hash_map[i] = j
                else:
                    return False

            else:               
                # If the key already exists in the map, we check if another value than the
                # one already mapped to key.
                if j != hash_map[i]:
                    return False

        return True
                    
def main():
    obj = Solution()
    print(obj.isIsomorphic("egg", "add"))
    print(obj.isIsomorphic("foo", "bar"))
    print(obj.isIsomorphic("paper", "title"))
    
main()