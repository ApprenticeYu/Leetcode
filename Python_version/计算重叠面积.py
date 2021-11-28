class Solution:
    def compute_area(self,ax1,ay1,ax2,ay2,bx1,by1,bx2,by2):
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        width = min(ax2,bx2) - max(ax1,bx1)
        height = min(ay2,by2) - max(ax1,bx1)
        area = max(width,0) * max(height,0)
        return area1 + area2 - area
