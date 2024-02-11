from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        dirOrFiles = []
        path = path.split("/")
        for elem in path:
            if dirOrFiles and elem == "..":
                dirOrFiles.pop()
            elif elem not in [".", "", ".."]:
                dirOrFiles.append(elem)

        return "/" + "/".join(dirOrFiles)


def main() -> None:
    inputs = [
        "/home/",
        "/../",
        "/home//foo/",
        "/home//.../",
        "/./",
        "/a/./b/../../c/",
    ]
    s = Solution()
    for path in inputs:
        print(s.simplifyPath(path))


if __name__ == "__main__":
    main()
