# Two Integer Sum
# Solved 
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]
# Example 3:

# Input: nums = [5,5], target = 10

# Output: [0,1]
# Constraints:

# 2 <= nums.length <= 1000
# -10,000,000 <= nums[i] <= 10,000,000
# -10,000,000 <= target <= 10,000,000


## SOLUTION : 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


## EXPLANATION : 

# Here's a detailed explanation:
# Function Definition:
# python
# def twoSum(self, nums: List[int], target: int) -> List[int]:

# This defines a method twoSum that takes two parameters:
# nums: A list of integers
# target: An integer
# The method is expected to return a list of integers (the indices of the two numbers that add up to the target).
# Initialize the Hash Map:
# python
# prevMap = {}  # val -> index

# We create an empty dictionary called prevMap.
# This will store the numbers we've seen so far as keys and their indices as values.
# Iterate Through the List:
# python
# for i, n in enumerate(nums):

# We use enumerate() to loop through the list, giving us both the index (i) and the value (n) of each element.
# Calculate the Difference:
# python
# diff = target - n

# For each number n, we calculate the difference between the target and n.
# This difference is the number we need to find to solve the problem.
# Check if the Difference Exists:
# python
# if diff in prevMap:
#     return [prevMap[diff], i]

# We check if the difference is already in our prevMap.
# If it is, we've found our solution! We return a list containing:
# The index of the difference (which we stored earlier)
# The current index i
# Update the Map:
# python
# prevMap[n] = i

# If we haven't found a solution yet, we add the current number and its index to prevMap.
# This allows us to check for it in future iterations.
# Key Insights:
# This solution uses a hash map (dictionary in Python) for O(1) lookup time.
# It solves the problem in a single pass through the list, giving it a time complexity of O(n).
# The space complexity is O(n) in the worst case, where we might need to store nearly all numbers in the hash map.
# This method is more efficient than the brute force approach of checking every pair of numbers.
# Example Walkthrough:
# Let's say nums = [2, 7, 11, 15] and target = 9:
# First iteration: n = 2, diff = 7. 7 is not in prevMap, so we add {2: 0} to prevMap.
# Second iteration: n = 7, diff = 2. 2 is in prevMap, so we return [0, 1].
# This solution efficiently finds the two numbers that add up to the target sum, returning their indices in a single pass through the list.
