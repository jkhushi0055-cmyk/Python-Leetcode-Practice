class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Stores {character: last_seen_index}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # If the character is a duplicate within the current active window,
            # jump the left pointer just past the previous occurrence.
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            # Update the latest index of the character
            char_index[char] = right
            
            # Calculate current window length and update max_len
            max_len = max(max_len, right - left + 1)
            
        return max_len