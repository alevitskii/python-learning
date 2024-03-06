# iterator protocol
# for e in myobject:... -> Python checks:
# 1. Whether the object contains one of the iterator methods - __next__ or __iter__ (Iterable)
# 2. Whether the object is a sequence and has __len__ and __getitem__ (Sequence)

from __future__ import annotations

from datetime import date, timedelta
from typing import Sequence, overload


class DateRangeIterable:
    """An iterable that contains its own iterator object."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self

    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration()
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


class DateRangeContainerIterable:
    """An iterable that contains its own iterator object."""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


class DateRangeSequence:  # this is Sequence
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        # supposed to be able to get elements one at a time,
        # in order, starting at zero as the first index
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


class C[T]:
    def __init__(self, lst: Sequence[T]) -> None:
        self._lst = lst

    # with overload inst[1:] will be correctly identified as C[T] and inst[1] as T
    # without - both will be of type C[T] | int
    @overload
    def __getitem__(self, idx: int) -> T: ...
    @overload
    def __getitem__(self, idx: slice) -> C[T]: ...

    def __getitem__(self, idx: slice | int) -> C[T] | T:  # Self instead of C[T] doesn't work here
        if isinstance(idx, slice):
            return C(self._lst[idx])
        return self._lst[idx]

    def __repr__(self):
        return f"{type(self).__name__}({self._lst})"


def main() -> None:
    # 1. iter() is called
    # 2. next() is called every step of the loop
    # for day in DateRangeIterable(date(2018, 1, 1), date(2018, 1, 5)):
    #     print(day)

    # r1 = DateRangeIterable(date(2018, 1, 1), date(2018, 1, 5))
    # print(", ".join(map(str, r1)))
    # # r1 is exhausted
    # print(max(r1))

    # r1 = DateRangeContainerIterable(date(2018, 1, 1), date(2018, 1, 5))
    # print(", ".join(map(str, r1)))
    # print(max(r1))

    # s1 = DateRangeSequence(date(2018, 1, 1), date(2018, 1, 5))
    # for day in s1:
    #     print(day)

    # print()
    # print(s1[0])
    # print(s1[3])
    # print(s1[-1])

    inst = C([1, 2, 3])
    x = inst[1:]
    y = inst[1]
    print(f"{inst!r}, {x=}, {y=}")


if __name__ == "__main__":
    main()
