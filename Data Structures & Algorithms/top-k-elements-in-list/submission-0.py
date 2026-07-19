class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # make list with len(nums) + 1 empty sublists 
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            # key-value pairs (number and frq)
        for num, frq in count.items():
            freq[frq].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if (len(res) == k):
                    return res
