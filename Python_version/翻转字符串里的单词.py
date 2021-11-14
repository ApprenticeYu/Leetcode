import collections

class Solution:
    def reverse_words(self,S):
        left,right = 0,len(S) - 1
        while left <= right and S[laft] == ' ':
            left += 1
        while left <= right and S[right] == ' ':
            right -= 1
        d = collections.deque()
        word = []
        while left <= right:
            if S[left] != ' ':
                word.append(S[left])
            elif S[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            left += 1
        d.appendleft(''.join(word))
        return ' '.join(d)
