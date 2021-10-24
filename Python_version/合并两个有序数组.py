class Solution:
    def merge(self,nums1,m,nums2,n):
        p1 = m - 1
        p2 = n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] >= nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
