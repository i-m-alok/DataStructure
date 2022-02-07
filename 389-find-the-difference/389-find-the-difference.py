class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = 0
        # we can do it with bit manipulation also
        for i in s:
            count-=ord(i)
        for j in t:
            count+=ord(j)
        return chr(count)