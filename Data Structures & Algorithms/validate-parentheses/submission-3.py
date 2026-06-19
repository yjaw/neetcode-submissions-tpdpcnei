class Solution:
    def isValid(self, s: str) -> bool:
        # Brackets
        stack = []
        for c in s:
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif c == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if len(stack) == 0 else False