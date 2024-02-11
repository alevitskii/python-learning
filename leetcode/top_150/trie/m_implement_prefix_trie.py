from dataclasses import dataclass, field


class PrefixTrie:
    END = "end"

    def __init__(self) -> None:
        self.root = {}

    def insert(self, word) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.END] = True

    def search(self, word) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.END in node

    def starts_with(self, prefix) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


@dataclass
class TrieNode:
    end: bool = False
    keys: dict = field(default_factory=dict)


# T: O(l) (l - word length), S:(n)
class PrefixTrie2:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word, node=None) -> None:
        if node is None:
            node = self.root
        if len(word) == 0:
            node.end = True
            return
        elif word[0] not in node.keys:
            node.keys[word[0]] = TrieNode()
            self.insert(word[1:], node.keys[word[0]])
        else:
            self.insert(word[1:], node.keys[word[0]])

    def search(self, word, node=None) -> bool:
        if node is None:
            node = self.root
        if len(word) == 0:
            return node.end
        elif word[0] in node.keys:
            return self.search(word[1:], node.keys[word[0]])
        return False

    def starts_with(self, prefix, node=None) -> bool:
        if node is None:
            node = self.root
        if len(prefix) == 0:
            return True
        elif prefix[0] in node.keys:
            return self.starts_with(prefix[1:], node.keys[prefix[0]])
        return False


def main() -> None:
    trie = PrefixTrie()
    trie.insert("apple")
    print(trie.search("dog"))
    trie.insert("dog")
    print(trie.search("dog"))
    print(trie.starts_with("app"))
    print(trie.search("app"))
    trie.insert("app")
    print(trie.search("app"))

    trie = PrefixTrie2()
    trie.insert("apple")
    print(trie.search("dog"))
    trie.insert("dog")
    print(trie.search("dog"))
    print(trie.starts_with("app"))
    print(trie.search("app"))
    trie.insert("app")
    print(trie.search("app"))


if __name__ == "__main__":
    main()
