def main() -> None:
    s1 = "fooexexexe.exe"
    print(s1.strip(".exe"))
    print(s1.removesuffix(".exe"))


if __name__ == "__main__":
    main()
