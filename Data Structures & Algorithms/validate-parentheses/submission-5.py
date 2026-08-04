class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding = {")": "(", "]": "[", "}": "{"}

        # for i in s:
        #     if i in corresponding.keys():
        #         stack.append(i)
        #     if i in corresponding.values():
        #         if stack and stack[0] == 
        #         print(stack[0] )
        #         print(corresponding[stack[0]])
        #         # stack.pop(corresponding)

        for i in s:
            if i not in corresponding:
                stack.append(i)
            else:
                if stack and stack[-1] == corresponding[i]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0