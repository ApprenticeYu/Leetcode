class Solution:
    def list_to_BST(self,head):
        def get_length(head):
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret

        def loop(left,right):
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode()
            root.left = loop(left,mid - 1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = loop(mid + 1,right)
            return root
        n = get_length(head)
        return loop(0,n - 1)
