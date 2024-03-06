# By default, zoneinfo will use the system’s time zone data if available;
# if no system time zone data is available, the library will fall back to using the first-party package tzdata,
# deployed on PyPI try to
# Windows does not officially ship a copy of the time zone database. So need to use tzdata
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def main() -> None:
    dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
    print(dt)
    print(dt.tzname())
    dt_add = dt + timedelta(days=1)
    print(dt_add)
    print(dt_add.tzname())


if __name__ == "__main__":
    main()
