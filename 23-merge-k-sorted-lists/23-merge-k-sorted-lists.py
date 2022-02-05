# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if(len(lists)==0):
            return None
        if(len(lists)==1):
            return lists[0]
        mid = len(lists)//2
        l1 = self.mergeKLists(lists[:mid])
        l2 = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(l1,l2)
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is not None and l2 is not None:
            if(l1.val>l2.val):
                new=self.mergeTwoLists(l1, l2.next)
                l2.next=new
                return l2
            elif l1.val<l2.val:
                new = self.mergeTwoLists(l1.next, l2)
                l1.next = new
                return l1
            else:
                temp = l1
                l1 = l1.next
                temp.next = l2.next
                l2.next = temp
                new = self.mergeTwoLists(l1, l2.next)
                l2.next = new
                return l2
        if l1 is None:
            return l2
        if l2 is None:
            return l1