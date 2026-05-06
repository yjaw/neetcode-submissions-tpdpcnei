class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == '+':
                b = stack.pop()
                a = stack.pop()
                c = a + b
                stack.append(c)
            elif t == '-':
                b = stack.pop()
                a = stack.pop()
                c = a - b
                stack.append(c)
            elif t == '*':
                b = stack.pop()
                a = stack.pop()
                c = a * b
                stack.append(c)
            elif t == '/':
                b = stack.pop()
                a = stack.pop()
                c = int(a / b)
                stack.append(c)
            else:
                stack.append(int(t))
            print(stack)
        return stack[-1]