class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_length = 1
        substring = ""
        for ch in s:
            if not ch in substring:
                substring += ch
            else:
                index = substring.index(ch)
                substring = substring[index+1:] + ch
            max_length = max(max_length, len(substring))
        return max_length