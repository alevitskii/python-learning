import contextlib
import errno
import hashlib
import mmap
import os
import struct
import time
from collections.abc import Generator
from typing import BinaryIO


def open_file(fname: str, size: int) -> BinaryIO:
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    try:
        return open(fname, "r+b")
    except IOError as e:
        if e.errno != errno.ENOENT:
            raise

        temp = "{}.{}.tmp".format(fname, os.getpid())
        with open(temp, "wb") as f:
            f.seek(size - 1)
            f.write(b"\0")

        try:
            os.unlink(fname)
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise

        os.rename(temp, fname)
        return open(fname, "r+b")


class HashMMap[*Ts]:
    def __init__(self, mm: mmap.mmap, fmt: str) -> None:
        self._mm = mm
        self._fmt = "Q" + fmt
        self._item_size = struct.calcsize(self._fmt)
        self._buckets = len(self._mm) // self._item_size

    @staticmethod
    def _hash(key: str) -> int:
        return int(hashlib.md5(key.encode()).hexdigest()[:8], 16)

    def _offset(self, hash: int) -> int:
        return hash % self._buckets * self._item_size

    def __iter__(self) -> Generator[tuple[*Ts]]:
        for i in range(self._buckets):
            values = self._get_from(i * self._item_size)
            if values[0] != 0:
                yield values[1:]

    def __setitem__(self, key: str, values: tuple[*Ts]) -> None:
        h = self._hash(key)
        offset = self._offset(h)
        struct.pack_into(self._fmt, self._mm, offset, h, *values)

    def _get_from(self, offset: int) -> tuple[int, *tuple[*Ts]]:
        return struct.unpack_from(self._fmt, self._mm, offset)

    def __getitem__(self, key: str) -> tuple[*Ts]:
        h0 = self._hash(key)
        offset = self._offset(h0)
        values = self._get_from(offset)
        if values[0] != h0:
            raise KeyError
        return values[1:]

    def __delitem__(self, key: str) -> None:
        h = self._hash(key)
        offset = self._offset(h)
        self._mm[offset : offset + self._item_size] = b"\0" * self._item_size

    def flush(self) -> None:
        self._mm.flush()


class UsageMap:
    FILE_SIZE = 1 << 20  # 1 MB

    def __init__(self, fname: str):
        self._f = open_file(fname, self.FILE_SIZE)
        self._mm = mmap.mmap(self._f.fileno(), 0)
        self._hmap: HashMMap[int, int] = HashMMap(self._mm, "III")

    def close(self) -> None:
        self._hmap.flush()
        self._mm.close()
        self._f.close()

    def touch(self, key: str, stamp: int | None = None, id: int = 0) -> None:
        if stamp is None:
            stamp = int(time.time())
        self._hmap[key] = (
            stamp,
            id,
        )

    def last_usage(self, key: str) -> tuple[int, int] | tuple[None, None]:
        try:
            return self._hmap[key]
        except KeyError:
            return None, None

    def flush(self) -> None:
        self._hmap.flush()


if __name__ == "__main__":
    qty = 1000000

    file = ""
    with contextlib.closing(UsageMap(file)) as mp:
        t1 = time.time()

        for x in range(qty):
            mp.touch(str(x))

        t2 = time.time()

        washed_out = 0
        for x in range(qty):
            washed_out += 1 if mp.last_usage(str(x)) is None else 0

        t3 = time.time()

        print("washed out (percent)", 100.0 * washed_out / qty)
        print("per one touch (ms)", 1000.0 * (t2 - t1) / qty)
        print("per one last_usage (ms)", 1000.0 * (t3 - t2) / qty)
