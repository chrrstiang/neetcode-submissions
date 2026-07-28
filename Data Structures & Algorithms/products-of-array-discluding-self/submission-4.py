class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev, fol = [1 for num in nums], [1 for num in nums]

        for i in range (len(nums)):
            if i == 0:
                continue
            else:
                prev[i] = prev[i-1] * nums[i-1]

        for i in range (len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            else:
                fol[i] = fol[i+1] * nums[i+1]

        print(f'{prev}, {fol}')
        res = [1 for num in nums]
        for i in range (len(nums)):
            res[i] = prev[i] * fol[i]
        
        return res
