class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        anaMap = {}
        for i in s:
            if(anaMap.get(i)):
                anaMap[i]+=1
            else:
                anaMap[i]=1
        count=len(anaMap)
        for i in t:
            if(anaMap.get(i)!=None):
                anaMap[i]-=1
            else:
                return False
        for i in anaMap.values():
            if(i!=0):
                return False
        return True