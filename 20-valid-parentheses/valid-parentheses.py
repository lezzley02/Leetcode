class Solution:
    def isValid(self, s: str) -> bool:
        openP="({["
        closeP=")}]"
        stack=[]
        d= dict(zip(closeP,openP))

        for i in s:
            if i in openP:
                 stack.append(i)
            else :
                if not stack:
                     return False 
                else:
                    if d[i]== stack[-1]:
                         stack.pop()
                    else:
                         return False
        return not stack
