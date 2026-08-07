class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])

        for t in tokens:
            if t in operators:
                op_2 = stack.pop()
                op_1 = stack.pop()
                if t == "+":
                    new = op_1 + op_2
                elif t == "-":
                    new = op_1 - op_2
                elif t == "*":
                    new = op_1 * op_2
                else:
                    if op_1 / op_2 > 0:
                        new = math.floor(op_1 / op_2)
                    else:
                        new = math.ceil(op_1 / op_2)
                stack.append(new)
            else:
                stack.append(int(t))
        return stack[0]