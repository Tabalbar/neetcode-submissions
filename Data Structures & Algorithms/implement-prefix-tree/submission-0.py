class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr =  self.root
        for char in word:
            if char not in curr.children:
                node = TrieNode()
                curr.children[char] = node
                curr = curr.children[char]
            else:
                curr = curr.children[char]
        
        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        if curr.isEndOfWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True
        
        