


class WordDictionary:
    def __init__(self):
        self.l = list()

    def addWord(self, word: str) -> None:
        self.l.append(word)

    def search(self, word: str) -> bool:
        for w in self.l:
            if len(w) != len(word):
                continue
            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == ".":
                    i += 1
                else:
                    break
            if i == len(w):
                return True
        return False


