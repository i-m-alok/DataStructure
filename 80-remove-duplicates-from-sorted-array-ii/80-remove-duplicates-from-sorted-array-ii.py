class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j=0
        k=0
        while(j< len(nums)):
            if(nums[i]==nums[j]):
                count=j-i+1
                if(count>2):
                    # k=j
                    while(j<len(nums) and nums[j]==nums[i]):
                        j+=1
                    count=0
                    i=j
                else:
                    nums[k]=nums[j]
                    k+=1
                    j+=1
                print(nums)
            else:
                nums[k]=nums[j]
                i=j
                k+=1
                j+=1
        return k