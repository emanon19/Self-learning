left = ['(', '[', '{']
right = [')', ']', '}']

mapp = {'(': ')', '[': ']', '{': '}'}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
                #print(stack)
                continue
            if s[i] in right:
                if stack:
                    if mapp[stack[-1]] == s[i]:
                        stack.pop()
                        #print(stack)
                    else:
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
        
