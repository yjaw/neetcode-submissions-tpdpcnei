class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = { "+": lambda a, b: a + b,
               "-": lambda a, b: a - b,
               "*": lambda a, b: a * b,
               "/": lambda a, b: int(a / b)}
        
        stack = []

        for t in tokens:
            if t in op:
                b, a = stack.pop(), stack.pop()
                print(a, b)
                stack.append(op[t](a, b))
            else:
                stack.append(int(t))
        
        return stack[0]