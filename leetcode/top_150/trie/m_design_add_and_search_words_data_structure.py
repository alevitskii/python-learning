from dataclasses import dataclass, field


@dataclass
class TrieNode:
    end: bool = False
    keys: dict = field(default_factory=dict)


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str, node=None) -> None:
        if node is None:
            node = self.root
        if len(word) == 0:
            node.end = True
            return
        elif word[0] not in node.keys:
            node.keys[word[0]] = TrieNode()
            self.addWord(word[1:], node.keys[word[0]])
        else:
            self.addWord(word[1:], node.keys[word[0]])

    def search(self, word: str, node=None) -> bool:
        if node is None:
            node = self.root
        if len(word) == 0:
            return node.end
        if word[0] == ".":
            for key in node.keys:
                if self.search(word[1:], node.keys[key]):
                    return True
            return False
        elif word[0] not in node.keys:
            return False
        return self.search(word[1:], node.keys[word[0]])


def main() -> None:
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))  # return False
    print(wordDictionary.search("bad"))  # return True
    print(wordDictionary.search(".ad"))  # return True
    print(wordDictionary.search("b.."))  # return True


if __name__ == "__main__":
    main()
