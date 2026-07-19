class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        starts = set(nums)
        elements = set(nums)
        for i in elements:
            print(set(nums))
            if i - 1 in elements:
                starts.remove(i)
        print(starts)
        
        max_length = 1
        for start in starts:
            sequence_length = 1
            valid = True
            while valid:
                if start + 1 in set(nums):
                    print(f"{start} + 1 is here, adding to length")
                    sequence_length += 1
                    start += 1
                    max_length = max(sequence_length, max_length)
                else:
                    valid = False
        return max_length