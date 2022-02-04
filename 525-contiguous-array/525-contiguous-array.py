'''This approach relies on the same premise as the previous approach. 
But, we need not use an array of size 2n+1, since it isn't necessary that we'll encounter all the countcount values possible. 
Thus, we make use of a HashMap mapmap to store the entries in the form of (index, count)(index,count). 
We make an entry for a countcount in the mapmap whenever the countcount is encountered first, and later on use the correspoding index to find the length of the largest subarray with equal no. of zeros and ones when the same countcount is encountered again.'''
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