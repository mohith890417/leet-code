class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        start = 0
        max_len = 0
        
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome
            return right - left - 1
            
        for i in range(len(s)):
            len1 = expand_around_center(i, i)       # Odd length palindrome (center is i)
            len2 = expand_around_center(i, i + 1)   # Even length palindrome (center is between i and i+1)
            
            current_max = max(len1, len2)
            
            if current_max > max_len:
                max_len = current_max
                # Update the start index of the longest palindrome
                start = i - (current_max - 1) // 2
                
        return s[start:start + max_len]