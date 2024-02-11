class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        def dfs(row, col, reach):
            reach.add((row, col))
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # Check all 4 directions
                new_row, new_col = row + x, col + y
                if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                    continue
                if (new_row, new_col) in reach:
                    continue
                if heights[new_row][new_col] < heights[row][col]:
                    continue
                dfs(new_row, new_col, reach)

        num_rows, num_cols = len(heights), len(heights[0])
        pacific_reach = set()
        atlantic_reach = set()
        for i in range(num_rows):
            dfs(i, 0, pacific_reach)
            dfs(i, num_cols - 1, atlantic_reach)
        for i in range(1, num_cols, 1):
            dfs(0, i, pacific_reach)
            dfs(num_rows - 1, i - 1, atlantic_reach)
        return list(pacific_reach.intersection(atlantic_reach))


def main() -> None:
    inputs = [
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ],
        [[1]],
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
    ]
    s = Solution()
    for heights in inputs:
        print(s.pacificAtlantic(heights))


if __name__ == "__main__":
    main()
