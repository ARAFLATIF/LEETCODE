class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] store = new int[26];

        for (int i = 0; i < s.length(); i++) {
            store[s.charAt(i) - 'a']++;
            store[t.charAt(i) - 'a']--;
        }

        for (int n : store) if (n != 0) return false;

        return true;
    }
}

//EXPLANATION :

// Length Check:
// We first check if the lengths of strings s and t are equal.
// If they're not equal, they can't be anagrams, so we immediately return false.
// Initialize Count Array:
// We create an integer array store of size 26 (assuming lowercase English letters only).
// Each index in this array will correspond to a letter (0 for 'a', 1 for 'b', etc.).
// Process Both Strings:
// We iterate through both strings simultaneously.
// For each character in s, we increment the count at its corresponding index in store.
// For each character in t, we decrement the count at its corresponding index.
// s.charAt(i) - 'a' converts the characte r to its array index (e.g., 'a' becomes 0, 'b' becomes 1).
// Check Counts:
// After processing both strings, we iterate through the store array.
// If any count is not zero, it means the strings have different character frequencies, so we return false.
// Final Check:
// If we've made it through the entire store array without finding any non-zero counts, the strings must be anagrams.
// We return true.
// Key Insights:
// This solution is very efficient, with a time complexity of O(n) where n is the length of the strings.
// The space complexity is O(1) because we use a fixed-size array of 26 elements, regardless of the input size.
// By incrementing for s and decrementing for t, we effectively compare the character frequencies in one pass.
// This method assumes the input strings contain only lowercase English letters. If this assumption doesn't hold, the method would need to be modified.
// This solution is particularly elegant because it processes both strings in a single loop and uses a clever counting method to determine if they are anagrams.
