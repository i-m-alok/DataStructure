class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        count=0
        for i in range(len(columnTitle)-1,-1,-1):
            res+=((26**count)*(ord(columnTitle[i])-64))
            count+=1
        return res