class Solution:
    def mergetwolists(self,l1,l2):
        prehead = ListNode(-1)
        pre = prehead
        while l1 and l2:
            if l1.value <= l2.value:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 is not None else l2
        return prehead.next
