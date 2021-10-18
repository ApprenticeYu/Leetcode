class Solution:
    def rotate_list(self,head,k):
        if k < 1 or not head or not head.next:
            return head
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        index = n - k % n
        if index == n:
            return head
        cur.next = head
        while index:
            cur = cur.next
            index -= 1
        ret = cur.next
        cur.next = None
        return ret
