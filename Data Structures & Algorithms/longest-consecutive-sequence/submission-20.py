class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique = set(nums)
        maxCount = 1
        for num in nums:
            if num - 1 in unique:
                continue
            else:
                count = 1
                curr = num
                while curr + 1 in unique:
                    count += 1
                    maxCount = max(maxCount, count)
                    curr += 1
        return maxCount

