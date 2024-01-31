from typing import List


class Solution:
    def length_to_bytes(self, x):
        length = len(x)
        bytes = []
        for i in range(4):
            bytes.append(chr(length >> (i * 8)))
        bytes.reverse()
        bytes_string = "".join(bytes)
        return bytes_string

    def bytes_to_length(self, bytes_string):
        result = 0
        for c in bytes_string:
            result = result * 256 + ord(c)
        return result

    def encode(self, strings: List[str]) -> str:
        encoded_string = ""
        for x in strings:
            encoded_string += self.length_to_bytes(x) + x
        return encoded_string

    def decode(self, string: str) -> List[str]:
        i = 0
        decoded_string = []
        while i < len(string):
            length = self.bytes_to_length(string[i : i + 4])
            i += 4
            decoded_string.append(string[i : i + length])
            i += length
        return decoded_string


if __name__ == "__main__":
    inputs = [["6^Hello_5", "5_World^6"], ["a", "b", "c", "d"]]
    s = Solution()
    for strings in inputs:
        print(s.decode(s.encode(strings)))
