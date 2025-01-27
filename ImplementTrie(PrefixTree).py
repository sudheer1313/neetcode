


class Node:
    def __init__(self):
        self.hashmap = {}
        self.endswith = False


class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.hashmap:
                cur.hashmap[w] = Node()
            cur = cur.hashmap[w]
        cur.endswith = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.hashmap:
                return False
            cur = cur.hashmap[w]
        return cur.endswith

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.hashmap:
                return False
            cur = cur.hashmap[w]
        return True



