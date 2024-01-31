class TimeMap:
    def __init__(self):
        self._map = {}

    def _binary_search(self, key, timestamp):
        left, right = 0, len(self._map[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self._map[key][mid][0] == timestamp:
                return mid
            if self._map[key][mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return mid if self._map[key][mid][0] < timestamp else mid - 1

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._map:
            self._map[key] = []
        self._map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map or timestamp < self._map[key][0][0]:
            return ""
        idx = self._binary_search(key, timestamp)
        return self._map[key][idx][1]


class TimeMap2:
    def __init__(self):
        self.values_dict = {}
        self.timestamps_dict = {}

    #  Set TimeStamp data variables
    def set_value(self, key, value, timestamp):
        if key in self.values_dict:
            if timestamp < self.timestamps_dict[key][-1]:
                value = self.timestamps_dict[key][-1]
            elif value != self.values_dict[key][len(self.values_dict[key]) - 1]:
                self.values_dict[key].append(value)
                self.timestamps_dict[key].append(timestamp)
        else:
            self.values_dict[key] = [value]
            self.timestamps_dict[key] = [timestamp]

    # Find the index of right most occurrence of the given timestamp
    # using binary search
    def search_index(self, n, key, timestamp):
        left = 0
        right = n
        mid = 0
        while left < right:
            mid = (left + right) >> 1
            if self.timestamps_dict[key][mid] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return left - 1

    # Get time_stamp data variables
    def get_value(self, key, timestamp):
        if key not in self.values_dict:
            return ""
        else:
            index = self.search_index(len(self.timestamps_dict[key]), key, timestamp)
            if index > -1:
                return self.values_dict[key][index]
            return ""


if __name__ == "__main__":
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    print(time_map.get("foo", 1))
    print(time_map.get("foo", 3))
    time_map.set("foo", "bar2", 4)
    print(time_map.get("foo", 4))
    print(time_map.get("foo", 5))
    print(time_map.get("foo", 3))
    print(time_map.get("foo", 0))
