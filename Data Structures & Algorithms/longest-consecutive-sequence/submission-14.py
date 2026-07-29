class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = {}
        if not nums:
            return 0

        for num in nums:
            if num - 1 in set(nums):
                continue
            seqs[num] = [num]
            curr = num + 1
            while curr in set(nums):
                seqs[num].append(curr)
                curr += 1
        
        return len(max(seqs.values(), key=len))
            
