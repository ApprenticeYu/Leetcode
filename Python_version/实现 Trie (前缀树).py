class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def search_prefix(self,prefix):
        node = self
        for v in prefix:
            ch = ord(v) - ord('a')
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert_word(self,word):
        node = self
        for v in word:
            ch = ord(v) - ord('a')
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self,word):
        node = self.search_prefix(word)
        return node and node.isEnd

    def start(self,prefix):
        return self.search_prefix(prefix)
