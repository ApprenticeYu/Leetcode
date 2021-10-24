class Solution:
    def delete_duplicate(self,head):
        if not head:
            return head
        dummy = ListNode(0,head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                value = cur.next.val
                while cur.next and cur.next.val == value:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
