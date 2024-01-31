from collections import deque
from typing import List


class Solution:
    def is_one_char_diff(self, gene1, gene2):
        diff = 0
        for i in range(len(gene1)):
            if gene1[i] != gene2[i]:
                diff += 1
            if diff > 1:
                return False
        return diff == 1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque()
        queue.extend([g for g in bank if self.is_one_char_diff(startGene, g)])
        seen = set()
        round_number = 1
        while queue:
            count, length = 0, len(queue)
            while count < length:
                count += 1
                gene = queue.popleft()
                if gene in seen:
                    continue
                if gene == endGene:
                    return round_number
                seen.add(gene)
                queue.extend([g for g in bank if self.is_one_char_diff(gene, g)])
            round_number += 1
        return -1


if __name__ == "__main__":
    inputs = [
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"]),
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]),
        ("AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]),
    ]
    s = Solution()
    for startGene, endGene, bank in inputs:
        print(s.minMutation(startGene, endGene, bank))
