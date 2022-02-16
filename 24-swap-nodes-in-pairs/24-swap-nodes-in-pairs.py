# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapTwicePair(head)
    
    def swapTwicePair(self, root):
        # print(root)
        if(root and root.next):
            tempHead = root
            tempNext = self.swapTwicePair(root.next.next)
            root.next.next = root
            tempHead = root.next
            root.next = tempNext
            return tempHead
        return root