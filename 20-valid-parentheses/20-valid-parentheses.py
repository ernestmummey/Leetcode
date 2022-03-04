class Solution:
    def isValid(self, s: str) -> bool:
        _open = '({['
        dic = {'(':')', '{':'}', '[':']'}
        stack = []
        
        for bracs in s:
            if bracs in _open:
                stack.append(bracs)
            elif stack and bracs == dic[stack[-1]]:
                stack.pop()
            
            else:
                return False
            
        return stack == []
                
             