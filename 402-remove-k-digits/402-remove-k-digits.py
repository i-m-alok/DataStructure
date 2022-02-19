class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while(len(stack) and stack[-1]>int(i) and k):
                stack.pop(-1)
                k-=1
            stack.append(int(i))
        while(len(stack) and k):
            stack.pop(-1)
            k-=1
        count = 0
        result = 0
        while(len(stack)):
            result+=stack[-1]*(10**count)
            count+=1
            stack.pop()
        return str(result)