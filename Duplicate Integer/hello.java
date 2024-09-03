class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> uniques = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (uniques.contains(nums[i])) {
                return true;
            }
            uniques.add(nums[i]);
        }
        return false;
    }
}


// CODE EXPLANATION : 

// class Solution: This defines a class named Solution.
// public boolean hasDuplicate(int[] nums): This is a method named hasDuplicate that takes an integer array nums as input and returns a boolean value.
// Set<Integer> uniques = new HashSet<>();:
// Creates a new HashSet called uniques.
// A Set is a collection that cannot contain duplicate elements.
// HashSet is an implementation of Set that uses a hash table for storage.
// for (int i = 0; i < nums.length; i++): This is a for loop that iterates through each element in the nums array.
// if (uniques.contains(nums[i])):
// Checks if the current number (nums[i]) is already in the uniques set.
// If it is, it means we've found a duplicate.
// return true;: If a duplicate is found, the method immediately returns true.
// uniques.add(nums[i]);: If the number is not in the set, we add it to uniques.
// return false;: If we've gone through the entire array without finding any duplicates, we return false.
// The logic of this code is:
// We use a Set to keep track of unique numbers we've seen.
// As we iterate through the array, for each number:
// If it's already in the Set, we've found a duplicate, so we return true.
// If it's not in the Set, we add it to the Set and continue.
// If we finish the loop without finding any duplicates, we return false.
// This solution has a time complexity of O(n) where n is the length of the input array, as we potentially need to check each element once. The space complexity is also O(n) in the worst case, 
// where all elements are unique and we store them all in the Set.
