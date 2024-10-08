##Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:
# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


## EXPLANATION :

# Check each number in the list.
# If it finds a number that's already in seen, it returns True (we've found a duplicate).
# If it doesn't find any duplicates after checking all numbers, it returns False.
#always remeber to check the name that it is using, like "has duplicate" and "contains duplicate"
