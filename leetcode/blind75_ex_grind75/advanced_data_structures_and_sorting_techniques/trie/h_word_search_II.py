from typing import Dict, List


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_string: bool = False


class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    # Function to insert a string in the trie
    def insert(self, string_to_insert) -> None:
        node = self.root
        for c in string_to_insert:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_string = True

    # Function to search a string from the trie
    def search(self, string_to_search) -> bool:
        node = self.root
        for c in string_to_search:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_string

    # Function to search prefix of strings
    def starts_with(self, prefix) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    # Function to delete the characters in the searched word that are not shared
    def remove_characters(self, string_to_delete) -> None:
        node = self.root
        child_list = []
        for c in string_to_delete:
            child_list.append([node, c])
            node = node.children[c]
        for pair in reversed(child_list):
            parent = pair[0]
            child_char = pair[1]
            target = parent.children[child_char]
            if target.children:
                return
            del parent.children[child_char]


class Solution:
    def dfs(self, words_trie, node, grid, row, col, result, word=""):
        if node.is_string:
            result.append(word)
            node.is_string = False
            words_trie.remove_characters(word)
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            char = grid[row][col]
            child = node.children.get(char)
            if child is not None:
                word += char
                grid[row][col] = None
                for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    self.dfs(words_trie, child, grid, row + row_offset, col + col_offset, result, word)
                grid[row][col] = char

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_for_words = Trie()
        result = []
        for word in words:
            trie_for_words.insert(word)
        for j in range(len(board)):
            for i in range(len(board[0])):
                self.dfs(trie_for_words, trie_for_words.root, board, j, i, result)
        return result


if __name__ == "__main__":
    inputs = [
        # ([["o", "a", "a", "n"],
        #   ["e", "t", "a", "e"],
        #   ["i", "h", "k", "r"],
        #   ["i", "f", "l", "v"]],
        #  ["oath", "pea", "eat", "rain"]),
        # ([["a", "b"],
        #   ["c", "d"]],
        #  ["abcb", "bacd"]),
        (
            [["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]],
            ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"],
        ),
    ]
    s = Solution()
    for board, words in inputs:
        print(s.findWords(board, words))
