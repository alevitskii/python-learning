import datetime


def main() -> None:
    # it'd throw "ValueError: Invalid isoformat string" in 3.10
    # now it parses more formats and can include timezones
    print(f'{datetime.datetime.fromisoformat("20111104T000523")!r}')
    print(f'{datetime.datetime.fromisoformat("2011-W01-2T00:05:23.283")!r}')
    print(f'{datetime.datetime.fromisoformat("2019-07-05T00:05:23.283")!r}')
    print(f'{datetime.datetime.fromisoformat("2019-07-05T00:05:23Z")!r}')
    print(f'{datetime.datetime.fromisoformat("2019-07-05T00:05:23+00:00")!r}')
    print(f'{datetime.datetime.fromisoformat("2011-11-04T00:05:23+04:00")!r}')


if __name__ == "__main__":
    main()
