from collections import deque
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = set(['+', '-', '*', '/'])
        output = 0

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                if len(stack) >= 2:
                    val_1 = stack.pop()
                    val_2 = stack.pop()
                    if t == '+':
                        stack.append(val_1 + val_2)
                    elif t == '-':
                        stack.append(val_2 - val_1)
                    elif t == '*':
                        stack.append(val_1 * val_2)
                    elif t == '/':
                        stack.append(int(val_2 / val_1))
        return stack[0]
            