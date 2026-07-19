class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = ''.join(x for x in s.lower() if x.isalnum())
        reversed_str = ''.join(x for x in s[::-1].lower() if x.isalnum())
        print(filtered_str, reversed_str)
        return filtered_str == reversed_str