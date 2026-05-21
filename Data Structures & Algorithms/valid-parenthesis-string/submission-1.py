class Solution:
    def checkValidString(self, s: str) -> bool:
        max_left = 0
        min_left = 0

        for c in s:
            if c == '(':
                max_left += 1
                min_left += 1
            if c == ')':
                max_left -= 1
                min_left -= 1
            if c == '*':
                max_left += 1
                min_left -= 1
            
            if max_left < 0:
                return False
            
            if min_left < 0:
                min_left = 0
        
        return min_left == 0