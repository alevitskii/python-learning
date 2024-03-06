import os.path


class Solution:
    def simplifyPath(self, path: str) -> str:
        dirOrFiles = []
        splitted_path = path.split("/")
        for elem in splitted_path:
            if dirOrFiles and elem == "..":
                dirOrFiles.pop()
            elif elem not in [".", "", ".."]:
                dirOrFiles.append(elem)

        return "/" + "/".join(dirOrFiles)


class Solution2:
    def simplifyPath(self, path: str) -> str:
        return os.path.normpath(path)


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
