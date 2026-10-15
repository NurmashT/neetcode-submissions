class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for c in s.lower():
            if c.isalnum():
                result += c
        return result == result[::-1]