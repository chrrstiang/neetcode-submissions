class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = {}
        if not nums:
            return 0

        for num in nums:
            if num - 1 in set(nums):
                continue
            seqs[num] = 1
            curr = num + 1
            while curr in set(nums):
                seqs[num] += 1
                curr += 1
        
        return max(seqs.values())
            
