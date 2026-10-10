class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        m={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if i in m:
                if not stack or stack[-1]!=m[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        
        return not stack