class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack:
                if temp > temperatures[stack[-1]]:
                    diff = i - stack[-1]
                    res[stack[-1]] = diff
                    stack.pop()
                else:
                    break
            stack.append(i)
        return res

