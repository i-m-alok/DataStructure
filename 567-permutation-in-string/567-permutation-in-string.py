import copy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        anaMap = {}
        result = []
        for i in s1:
            if(anaMap.get(i)):
                anaMap[i]+=1
            else:
                anaMap[i]=1
        i=0
        j=0
        print(anaMap)
        count=len(anaMap)
        while(j<len(s2)):
            windowSize=j-i
            if(windowSize<len(s1)):
                if(anaMap.get(s2[j])!=None):
                    anaMap[s2[j]]-=1
                    if(anaMap[s2[j]]==0):
                        count-=1
                j+=1
            else:
                if(count==0):
                    return True
                if(anaMap.get(s2[i])!=None):
                    anaMap[s2[i]]+=1
                    if(anaMap[s2[i]]==1):
                        count+=1
                i+=1
        if(count==0):
            return True
        return False