class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding = {")": "(", "]": "[", "}": "{"}
        
        for i in s:
            if i not in corresponding:
                stack.append(i)
            else:
                if stack and stack[-1] == corresponding[i]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0