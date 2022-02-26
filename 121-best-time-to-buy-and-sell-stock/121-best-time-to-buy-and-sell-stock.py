class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minArr = []
        minVal = sys.maxsize-1
        for i in prices:
            if(minVal>i):
                minArr.append(i)
                minVal=i
            else:
                minArr.append(minVal)
        # print(minArr)
        maxProfit=-sys.maxsize+1
        for i in range(len(prices)-1, -1, -1):
            diff=prices[i]-minArr[i]
            if(diff >maxProfit):
                maxProfit=diff
        return maxProfit