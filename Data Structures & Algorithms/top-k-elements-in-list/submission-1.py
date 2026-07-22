class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            if num in freqs:
                freqs[num].append(num)
            else:
                freqs[num] = [num]
        
        arr = []
        for key, value in freqs.items():
            arr.append(value)

        sorted_arr = sorted(arr, key=len, reverse=True)
        
        result = []
        count = k
        for a in sorted_arr:
            if count - 1 == 0:
                result.append(a[0])
                return result
            else:
                result.append(a[0])
                count -= 1