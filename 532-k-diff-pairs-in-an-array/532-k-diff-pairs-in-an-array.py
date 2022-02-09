
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashMap = dict()
        count = 0
        for i in nums:
            if(hashMap.get(i)!=None):
                hashMap[i]+=1
            else:
                hashMap[i]=1
        for i in hashMap:
            if(hashMap.get(i-k)!=None):
                if(i!=(i-k) or (k==0 and hashMap[i]>1)):
                    count+=1
        # print(hashMap,result)
        return count
    
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         result = set()
#         hashMap = dict()
#         count = 0
#         for i in nums:
#             if(hashMap.get(i)!=None):
#                 hashMap[i]+=1
#             else:
#                 hashMap[i]=1
#         for i in nums:
#             if(hashMap.get(i-k)!=None):
#                 if(i!=(i-k) or (k==0 and hashMap[i]>1)):
#                     result.add(frozenset([i,i-k]))
#         # print(hashMap,result)
#         return len(result)