class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic=dict()
        i=0
        j=0
        while(i<len(s) and dic.get(s[i])==None):
            dic[s[i]]=i
            i+=1
        maxCount=len(dic)
        while(i<len(s)):
            if(dic.get(s[i])!=None):
                maxCount=max(len(dic), maxCount)
                index=dic[s[i]]
                while(j<=index):
                    del dic[s[j]]
                    j+=1
            dic[s[i]]=i
            i+=1
        return max(maxCount, len(dic))        
                    
            