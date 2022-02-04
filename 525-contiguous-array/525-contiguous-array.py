class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums = [-1 if(x==0) else x for x in nums]
        sumMap = dict()
        sumMap[0]=-1
        maxLen = 0
        diff = 0
        for i in range(len(nums)):
            diff+=nums[i]
            if(sumMap.get(diff)!=None):
                tempLen = i-(sumMap[diff])
                if(maxLen<tempLen):
                    maxLen=tempLen
            else:
                sumMap[diff]=i
        # print(sumMap)
        return maxLen