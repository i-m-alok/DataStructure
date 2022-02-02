class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anaMap = {}
        result = []
        for i in p:
            if(anaMap.get(i)):
                anaMap[i]+=1
            else:
                anaMap[i]=1
        i=0
        j=0
        print(anaMap)
        count=len(anaMap)
        while(j<len(s)):
            windowSize=j-i
            # print(i,j, windowSize)
            # print("A", anaMap)
            if(windowSize<len(p)):
                if(anaMap.get(s[j])!=None):
                    anaMap[s[j]]-=1
                    if(anaMap[s[j]]==0):
                        count-=1
                j+=1
            else:
                # print("B",i,j, count,anaMap)
                if(count==0):
                    result.append(i)
                if(anaMap.get(s[i])!=None):
                    anaMap[s[i]]+=1
                    if(anaMap[s[i]]==1):
                        count+=1
                # if(anaMap.get(s[j])!=None):
                #     anaMap[s[j]]-=1
                #     if(anaMap[s[j]]==0):
                #         count-=1
                # else:
                #     if(anaMap.get(s[i])):
                #         anaMap[s[i]]+=1
                i+=1
        if(count==0):
            result.append(i)
        return result
            
            
            