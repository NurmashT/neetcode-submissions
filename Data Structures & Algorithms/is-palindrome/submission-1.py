class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            print(s[start], s[end])
            if not s[start].isalnum():
                print(f"is not alnum: {s[start]}")
                start += 1
                continue
            if not s[end].isalnum():
                print(f"is not alnum: {s[end]}")
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                print(f"Comparing: {s[start]} and {s[end]}")
                return False
                
            start += 1
            end -= 1
        
        return True