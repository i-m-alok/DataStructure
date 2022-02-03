class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sumMap = {}
        
        for i in nums1:
            for j in nums2:
                temp = i+j
                if(sumMap.get(temp)):
                    sumMap[temp]+=1
                else:
                    sumMap[temp]=1
        count=0
        for i in nums3:
            for j in nums4:
                temp = -1*(i+j)
                if(sumMap.get(temp)):
                    count+=sumMap[temp]
        return count