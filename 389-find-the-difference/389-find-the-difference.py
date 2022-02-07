class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = 0
        for i in s:
            count-=ord(i)
        for j in t:
            count+=ord(j)
        return chr(count)