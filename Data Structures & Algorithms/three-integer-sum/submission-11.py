class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        snums = sorted(nums)
        triplets = []

        for i in range (len(nums) - 1):
            left, right = 0, len(nums) - 1
            while not (left == i or right == i):
                tripletSum = snums[left] + snums[i] + snums[right]
                if tripletSum == 0:
                    triplets.append([snums[left], snums[i], snums[right]])
                    left += 1
                    right -= 1
                elif tripletSum > 0:
                    right -= 1
                else:
                    left += 1
        print(triplets)
        return [list(t) for t in {tuple(trip) for trip in triplets}]