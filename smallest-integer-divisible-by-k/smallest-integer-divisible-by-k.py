class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if(not (k%2) or not (k%5)):
            return -1
        n=1
        length=1
        while True:
            if n%k==0:
                return length
            n=n*10+1
            length+=1