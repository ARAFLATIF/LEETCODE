class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prevMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;

            if (prevMap.containsKey(diff)) {
                return new int[] { prevMap.get(diff), i };
            }

            prevMap.put(num, i);
        }

        return new int[] {};
    }
}



//DETAILED EXPLANATION : 

// Explanation:
// Class and Method Definition:
// java
// class Solution {
//     public int[] twoSum(int[] nums, int target) {

// We define a class named Solution.
// Inside this class, we have a method twoSum that takes two parameters:
// nums: An array of integers.
// target: An integer representing the target sum.
// The method returns an array of integers, which are the indices of the two numbers that add up to the target.
// Initialize the HashMap:
// java
// HashMap<Integer, Integer> prevMap = new HashMap<>();

// We create a HashMap named prevMap.
// This map will store numbers from the nums array as keys and their corresponding indices as values.
// Iterate Through the Array:
// java
// for (int i = 0; i < nums.length; i++) {
//     int num = nums[i];
//     int diff = target - num;

// We loop through the nums array using a standard for loop.
// i is the current index, and num is the current number at that index.
// We calculate diff, which is the difference between the target and the current number num. This diff represents the number we need to find in the map to complete the sum.
// Check for the Complement:
// java
// if (prevMap.containsKey(diff)) {
//     return new int[] { prevMap.get(diff), i };
// }

// We check if diff is already a key in prevMap.
// If it is, it means we've already encountered the number needed to complete the sum with the current number num.
// We return an array containing the index of diff (retrieved with prevMap.get(diff)) and the current index i.
// Update the HashMap:
// java
// prevMap.put(num, i);

// If the diff is not found in the map, we add the current num and its index i to prevMap.
// This allows us to check for this number in future iterations.
// Return Statement:
// java
// return new int[] {};

// If the loop completes without finding a solution, we return an empty array.
// In a typical interview setting, it's assumed that there will always be exactly one solution, so this return statement is just a safeguard.
// Key Insights:
// Efficiency: The use of a HashMap allows for O(1) average-time complexity for both insertions and lookups, making the overall time complexity of this solution O(n),
//   where n is the number of elements in nums.
// Space Complexity: The space complexity is O(n) because, in the worst case, we might store all elements of the array in the map.
// Logic: The solution efficiently checks for the complement of each number as we iterate through the array, ensuring that we find the two indices in a single pass.
// Example Walkthrough:
// Suppose nums = [2, 7, 11, 15] and target = 9:
// First iteration (i = 0): num = 2, diff = 7. 7 is not in prevMap, so we add {2: 0}.
// Second iteration (i = 1): num = 7, diff = 2. 2 is in prevMap, so we return [0, 1].
// This solution efficiently finds the indices of the two numbers that add up to the target sum.
