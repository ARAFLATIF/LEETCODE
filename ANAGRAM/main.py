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

# BETTER EXPLANATION : 

# This solution works as follows:
# First, we check if the lengths of the two strings are different. If they are, they can't be anagrams, so we return False.
# We create two dictionaries, count_s and count_t, to store the count of each character in strings s and t respectively.
# We iterate through each character in string s:
# For each character, we increment its count in count_s.
# The get(char, 0) method returns the current count of the character if it exists, or 0 if it doesn't.
# We do the same for string t, counting characters in count_t.
# Finally, we compare the two dictionaries. If they are equal, it means both strings have the same characters with the same frequencies, so they are anagrams.
# This solution has a time complexity of O(n), where n is the length of the input strings, as we iterate through each string once. The space complexity is O(k),
# where k is the number of unique characters in the strings (which is bounded by the size of the character set, typically 26 for lowercase English letters).
