class TrieNode:
    def __init__(self) -> None:
        self.count = 0
        self.child = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = TrieNode()
            curr = curr.child[ch]
        curr.count += 1

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
        return curr.count > 0

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
        return True
