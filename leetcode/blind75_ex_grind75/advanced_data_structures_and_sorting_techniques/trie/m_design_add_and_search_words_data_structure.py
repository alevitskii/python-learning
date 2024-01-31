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


class TrieNode2:
    # Initialize TrieNode instance
    def __init__(self):
        self.children = []
        self.complete = False
        for i in range(0, 26):
            self.children.append(None)


class WordDictionary2:
    # Initialize the root with TrieNode and set
    # the 'can_find' boolean to FALSE
    def __init__(self):
        self.root = TrieNode2()
        self.can_find = False

    # Function to add a new word to the dictionary
    def addWord(self, word):
        n = len(word)
        cur_node = self.root
        for i, val in enumerate(word):
            # Find the correct index of the character in the list of nodes
            index = ord(val) - ord("a")
            # If the letter is not present in the trie, then
            # create a new trie node for it,
            # otherwise use the existing trie node for this letter
            if cur_node.children[index] is None:
                cur_node.children[index] = TrieNode2()
            cur_node = cur_node.children[index]
            if i == n - 1:
                # If we've reached the end of word and complete flag is already set
                # this means that it is already present in the dictionary
                if cur_node.complete:
                    print("\tWord already present!")
                    return
                # Once all the characters are added to the trie,
                # set the 'complete' variable to TRUE
                cur_node.complete = True
        print("\tWord added successfully!")

    # Function to search for a word in the dictionary
    def search(self, word):
        # Set the 'can_find' variable as FALSE
        self.can_find = False
        # Perform depth-first search to iterate over the children nodes
        self.search_helper(self.root, word, 0)
        return self.can_find

    def search_helper(self, node, word, i):
        # If the word has already been found and there is no need
        # for further searching, return the control to the calling context
        if self.can_find:
            return
        # Return the control to the calling context
        # if the current node is empty
        if not node:
            return
        # If we have found the last character of the query string
        # in the trie and the complete flag is set, we have found the entire word
        if len(word) == i:
            if node.complete:
                self.can_find = True
            return

        # If the word contains a wildcard character ".", match
        # it with all of the children (letters) of the current node and
        # perform depth first search starting at each child
        if word[i] == ".":
            for j in range(ord("a"), ord("z") + 1):
                self.search_helper(node.children[j - ord("a")], word, i + 1)
        else:
            # otherwise, simply locate the child corresponding to the current character
            index = ord(word[i]) - ord("a")
            # and continue the depth-first traversal
            self.search_helper(node.children[index], word, i + 1)

    # Function to get all words in the dictionary
    def get_words(self):
        words_list = []
        # Return an empty list if the root is NULL
        if not self.root:
            return []
        # Perform depth first search on the trie
        return self.dfs(self.root, "", words_list)

    def dfs(self, node, word, words_list):
        # If the node is NULL, return the 'words_list'
        if not node:
            return words_list
        # If the word is complete, add it to the 'words_list'
        if node.complete:
            words_list.append(word)

        for j in range(ord("a"), ord("z") + 1):
            prefix = word + chr(j)
            words_list = self.dfs(node.children[j - ord("a")], prefix, words_list)
        return words_list


if __name__ == "__main__":
    wordDictionary = WordDictionary2()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad"))  # return False
    print(wordDictionary.search("bad"))  # return True
    print(wordDictionary.search(".ad"))  # return True
    print(wordDictionary.search("b.."))  # return True
