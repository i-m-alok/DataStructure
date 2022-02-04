class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        tempHash = set()
        for i in range(len(nums)):
            firstPtr = i+1
            lastPtr = len(nums)-1
            # print(i)
            while(firstPtr<lastPtr):
                tSum = nums[i]+nums[firstPtr]+nums[lastPtr]
                if(tSum<0):
                    firstPtr+=1
                elif(tSum>0):
                    lastPtr-=1
                else:
                    s = frozenset([nums[i],nums[firstPtr],nums[lastPtr]])
                    # print(tempHash,s)
                    if( not s in tempHash):
                        res.append([nums[i],nums[firstPtr],nums[lastPtr]])
                        # tempHash = tempHash.union(set(s))
                        tempHash.add(frozenset(s))
                    lastPtr-=1
                    firstPtr+=1
        print(nums,res)
        return res