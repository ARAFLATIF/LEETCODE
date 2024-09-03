# Is Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.


# THE SOLUTION : 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths are different
        if len(s) != len(t):
            return False
        
        # Create dictionaries to store character counts
        count_s = {}
        count_t = {}
        
        # Count occurrences of each character in both strings
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        # Compare the character counts
        return count_s == count_t


## THE CODE IT SELF IS SELF EXPLANATORY
