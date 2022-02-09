class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = set()
        hashMap = dict()
        count = 0
        for i in nums:
            if(hashMap.get(i)!=None):
                hashMap[i]+=1
            else:
                hashMap[i]=1
        for i in nums:
            if(hashMap.get(i-k)!=None):
                if(i!=(i-k) or (k==0 and hashMap[i]>1)):
                    result.add(frozenset([i,i-k]))
        print(hashMap,result)
        return len(result)
            
            

# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         # nums.sort()
#         i=0
#         store = dict()
#         resultSet = set()
#         for i in nums:
#             if(i>=0):
#                 j=-(k-i)
#             else:
#                 j=k+i
#             if(store.get(j)!=None):
#                 if(i!=j or k==0 ):
#                     resultSet.add(frozenset([i,j]))
#             store[i]=j
#         return len(resultSet)

    

# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         i=0
#         store = dict()
#         resultSet = set()
#         for i in nums:
#             if(i>=0):
#                 j=-(k-i)
#             else:
#                 j=k+i
#             print(j, i)
#             if(self.isNumPresent(j, nums)):
#                 if(i!=j or k==0 ):
#                     resultSet.add(frozenset([i,j]))
#         return len(resultSet)
#     def isNumPresent(self,n, nums, j):
#         mid = 0
#         start = 0
#         end = len(nums)-1
#         while(start<end):
#             mid = start+ (end-start)//2
#             print(mid, nums[mid],n)
#             if(nums[mid]==n):
#                 return True
#             elif(nums[mid]<n):
#                 start=mid+1
#             else:
#                 end=mid
#         if(start==end and nums[start]==n):
#             return True
#         return False