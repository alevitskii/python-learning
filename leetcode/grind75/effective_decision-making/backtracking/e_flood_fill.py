class SolutionDFS:
    def fill(self, image, sr, sc, color, orig_color):
        if sr < 0 or sr >= len(image) or sc >= len(image[0]) or sc < 0 or image[sr][sc] != orig_color:
            return
        image[sr][sc] = color
        self.fill(image, sr + 1, sc, color, orig_color)
        self.fill(image, sr - 1, sc, color, orig_color)
        self.fill(image, sr, sc + 1, color, orig_color)
        self.fill(image, sr, sc - 1, color, orig_color)

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        self.fill(image, sr, sc, color, image[sr][sc])
        return image


class SolutionBFS:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        queue = [(sr, sc)]
        while queue:
            csr, csc = queue[0]
            queue = queue[1:]
            if image[csr][csc] != color:
                if csr + 1 < len(image) and image[csr + 1][csc] == image[csr][csc]:
                    queue.append((csr + 1, csc))
                if csr - 1 >= 0 and image[csr - 1][csc] == image[csr][csc]:
                    queue.append((csr - 1, csc))
                if csc + 1 < len(image[0]) and image[csr][csc + 1] == image[csr][csc]:
                    queue.append((csr, csc + 1))
                if csc - 1 >= 0 and image[csr][csc - 1] == image[csr][csc]:
                    queue.append((csr, csc - 1))
            image[csr][csc] = color
        return image


def main() -> None:
    inputs = [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 0),
    ]
    s = SolutionDFS()
    for image, sr, sc, color in inputs:
        print(s.floodFill(image, sr, sc, color))


if __name__ == "__main__":
    main()
