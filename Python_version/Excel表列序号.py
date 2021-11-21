class Solution:
    def title_to_number(self,title):
        number = 0
        multiple = 1
        for i in range(len(title) - 1,-1,-1):
            k = ord(title[i]) - ord('A') + 1
            number += k * multiple
            multiple *= 26
        return number
