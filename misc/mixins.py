class BaseTokenizer:

    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        yield from self.str_token.split("-")


class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())


class Tokenizer(UpperIterableMixin, BaseTokenizer):
    pass


def main() -> None:
    tk = Tokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
    print(list(tk))


if __name__ == "__main__":
    main()
