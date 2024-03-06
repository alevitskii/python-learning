import tomllib


def main() -> None:
    with open("F:\\MyDocs\\Repos\\andrei-levitskii\\python-learning\\3.11\\settings.toml", "rb") as f:
        data = tomllib.load(f)
        print(data)


if __name__ == "__main__":
    main()
