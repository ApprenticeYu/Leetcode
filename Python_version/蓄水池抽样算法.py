import random

class Solution:
    def __init__(self,head):
        self.head = head
    def get_random(self):
        count = 0
        reverse = 0
        cur = self.head
        while cur:
            count += 1
            temp = random.randint(1,count)
            if temp == count:
                reverse = cur.val
            cur = cur.next
        return reverse
