# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)
        
    def mergeSort(self, head):
        length=self.findLength(head)-1
        if(length<=0):
            return head
        mid=0
        midPtr=head
        while(mid<(length)//2):
            midPtr=midPtr.next
            mid+=1
        # print(length, midPtr, mid)
        temp=None
        if(midPtr):
            temp=midPtr.next
            midPtr.next=None
        left=self.mergeSort(head)
        right=self.mergeSort(temp)
        # print(self.mergeProcedure(left,right))
        return self.mergeProcedure(left,right)
    
    def mergeProcedure(self, left,right):
        leftPtr=left
        rightPtr=right
        tempHead = None
        tail=None
        # print(leftPtr, rightPtr)
        # print("______________")
        while(leftPtr and rightPtr):
            temp=None
            # print(tail)
            if(leftPtr.val<=rightPtr.val):
                temp=leftPtr
                leftPtr=leftPtr.next
            else:
                temp=rightPtr
                rightPtr=rightPtr.next
            temp.next=None
            if(tempHead==None and tail==None):
                tempHead=temp
                tail=temp
            else:
                tail.next=temp
                tail=tail.next
        if(leftPtr==None):
            tail.next=rightPtr
        elif(rightPtr==None):
            tail.next=leftPtr
        # print("______________",tail)
        return tempHead
        
    def findLength(self, head):
        # print(head)
        ptr=head
        count=0
        while(ptr):
            count+=1
            ptr=ptr.next
        return count