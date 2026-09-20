class Solution:
        def evalRPN(self, tokens: list[str]) -> int:
            stack = []
            ops = ('+', '-', '*', '/')
            for t in tokens:
                if t not in ops:
                    stack.append(int(t))
                    continue
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                if t == '-':
                    stack.append(a - b)
                if t == '*':
                    stack.append(a * b)
                if t == '/':
                    stack.append(int(a / b))
            return stack[0]