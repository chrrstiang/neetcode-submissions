import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #

        # go left -> right and store prods of prefixes
        prefixes = []
        suffixes = []
        for i in range(len(nums)):
            if i == 0:
                prefixes.append(1)
                suffixes.append(math.prod(nums[1:]))
            elif i == len(nums) - 1:
                prefixes.append(math.prod(nums[0:i]))
                suffixes.append(1)
            else:
                prefixes.append(math.prod(nums[0:i])) 
                suffixes.append(math.prod(nums[i+1:]))
            print(f'prefixes for {i}: {prefixes[i]}')
            print(f'suffixes for {i}: {suffixes[i]}')

        # loop through nums, storing prods of prefixes and suffixes
        output=[]
        for i in range(len(nums)):
            output.append(prefixes[i] * suffixes[i])
        return output
