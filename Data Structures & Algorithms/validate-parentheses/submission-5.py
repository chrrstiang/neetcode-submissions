from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        openings = set(['(', '{', '['])
        closings = set([')', '}', ']'])
        valid_combos = set(['()', '{}', '[]'])

        for l in s:
            if l in openings:
                print(f'appending opening {l}')
                stack.append(l)
            else:
                print(f'checking closing {l}')
                if len(stack) >= 1 and f'{stack[-1]}{l}' in valid_combos:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0