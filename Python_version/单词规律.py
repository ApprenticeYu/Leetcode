class Solution:
    def word_(self,pattern,s):
        word2ch = dict()
        ch2word = dict()
        s = s.split()
        if len(pattern) != len(s):
            return False
        for ch,word in zip(pattern,s):
            if (ch in ch2word and ch2word[ch] != word) or (word in word2ch and word2ch[word] != ch):
                return False
            word2ch[word] = ch
            ch2word[ch] = word
        return True
