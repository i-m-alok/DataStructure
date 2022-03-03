class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windowSize=len(p)
        windowBuffer=[0]*26
        startIndex=0
        pBuffer=[0]*26
        result=[]
        for i in range(len(p)):
            pBuffer[ord(p[i])-ord('a')]+=1
        for i in range(len(s)):
            currentWordI = ord(s[i])-ord('a')
            windowBuffer[currentWordI]+=1
            if((i-startIndex)>=windowSize):
                lastWordI=ord(s[startIndex])-ord('a')
                windowBuffer[lastWordI]-=1
                startIndex+=1
            if(self.validateEquality(windowBuffer, pBuffer)):
                result.append(startIndex)
        return result
                
    def validateEquality(self, buffer1, buffer2):
        for i in range(len(buffer1)):
            if(buffer1[i]!=buffer2[i]):
                return False
        return True
                
            
            
            
            