# when you sort unicode alphabetically you may encounter wrong
# behaviour sometimes because of some characters if use lower
# so it's better to use casefold
def main() -> None:
    print("ß".upper())
    print("ß".lower())
    print("ß".casefold())


if __name__ == "__main__":
    main()
