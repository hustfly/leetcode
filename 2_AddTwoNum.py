#Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i=0
        isUp=False
        r=ListNode(0)
        rhead=r
        while((l1 is not None) and (l2 is not None)):
            s=l1.val+l2.val
            s=s+1 if isUp else s
            if(s>=10):
                isUp=True
                s=s-10
            else:
                isUp=False
            r.val=s
            l1=l1.next
            l2=l2.next
            if((l1 is not None) and (l2 is not None)):
                r.next=ListNode(0)
                r=r.next
        while(l1 is not None):
            r.next=ListNode(0)
            r=r.next
            r.val=l1.val
            r.val=r.val+1 if isUp else r.val
            if(r.val>=10):
                isUp=True
                r.val=r.val-10
            else:
                isUp=False
            l1=l1.next
        while(l2 is not None):
            r.next=ListNode(0)
            r=r.next
            r.val=l2.val
            r.val=r.val+1 if isUp else r.val
            if(r.val>=10):
                isUp=True
                r.val=r.val-10
            else:
                isUp=False
            l2=l2.next
        if(isUp):
            r.next=ListNode(1)
        return rhead
