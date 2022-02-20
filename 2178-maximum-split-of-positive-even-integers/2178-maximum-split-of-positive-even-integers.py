class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        result=[]
        if((finalSum%2)!=0):
            return []
        sums=0
        s=2
        # temp = dict()
        while(sums<finalSum):
            if(sums+s>finalSum):
                t=result.pop()
                sums-=t
            sums+=s
            result.append(s)
            s+=2
            # print(s,sums, result)
        return result