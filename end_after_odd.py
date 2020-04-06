# Problem Statement
#-------------------------------
'''------------------------
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. **Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.**

Example:
linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6
---------------------------------------------'''
#--------------------------------------------

def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    x = head
    slow=head
    while(x is not None):
        if x.data%2 != 0:
            even=head
            trail=None
            while(even is not None and even.data % 2 != 0):
                trail=even
                even=even.next
            if even==None:
                return head
            elif trail==None:
                y=x.next
                head=x
                head.next=even
                even.next=y
            else:
                y=x.next
                trail.next=x
                x.next=even
                slow.next=y
        slow=x
        x=x.next
    return head
