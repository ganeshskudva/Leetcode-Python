class Trie:
    def __init__(self):
        self.child = [None] * 26
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def _get_key(self, ch):
        return ord(ch) - ord('a')

    def _match(self, word, idx, root):
        if idx >= len(word):
            return root.is_word

        if word[idx] != '.':
            return root.child[self._get_key(word[idx])] and self._match(word, idx + 1, root.child[self._get_key(word[idx])])

        for ch in range(26):
            if root.child[ch] and self._match(word, idx + 1, root.child[ch]):
                return True

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if not curr.child[self._get_key(ch)]:
                curr.child[self._get_key(ch)] = Trie()
            curr = curr.child[self._get_key(ch)]
        curr.is_word = True

    def search(self, word: str) -> bool:
        res = self._match(word, 0, self.root)
        return False if res is None else res
