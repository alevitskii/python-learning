from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {char: index for index, char in enumerate(s)}
        partitions = []
        start, end = 0, 0
        for i, char in enumerate(s):
            last_index = last_occurrence[char]
            end = max(end, last_index)
            if i == end:
                partitions.append(i - start + 1)
                start = i + 1
        return partitions


if __name__ == "__main__":
    inputs = [
        "ababcbacadefegdehijhklij",
        "eccbbbbdec",
    ]
    s = Solution()
    for string in inputs:
        print(s.partitionLabels(string))
