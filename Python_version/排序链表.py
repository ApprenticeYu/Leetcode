class Solution:
    def sort_list(self,head):
        def merge(head1,head2):
            dummy = ListNode(0)
            temp,temp1,temp2 = dummy,head1,head2
            while temp1 and temp2:
                if temp1.value <= temp2.value:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummy.next

        def sort_list_core(head,tail):
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow,fast = head,head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sort_list_core(head,mid),sort_list_core(mid,tail))
        return sort_list_core(head,None)
