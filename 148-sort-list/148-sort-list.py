# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.findMid(head)
        return self.mergeSort(head)
        
    def mergeSort(self, head):
        if(not head or not head.next):
            return head
        mid=self.findMid(head)
        left=self.mergeSort(head)
        right=self.mergeSort(mid)
        return self.mergeProcedure(left,right)
    
    def mergeProcedure(self, left,right):
        tail=ListNode(None)
        head = tail
        while(left and right):
            if(left.val<right.val):
                tail.next, tail, left = left, left, left.next
            else:
                tail.next, tail, right = right, right, right.next
        tail.next = left or right
        return head.next
    
    def findMid(self, head):
        slow, fast=head, head
        while(fast.next and fast.next.next):
            slow=slow.next
            fast=fast.next.next
        mid = slow.next
        slow.next=None
        return mid
        