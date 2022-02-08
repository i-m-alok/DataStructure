class Solution:
    def addDigits(self, num: int) -> int:
        if(num<10):
            return num
        sums = 0
        while(num>0):
            sums+= num%10
            num=num//10
        return self.addDigits(sums)