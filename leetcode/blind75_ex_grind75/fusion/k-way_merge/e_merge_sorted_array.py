class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_index = m + n - 1
        n1idx = m - 1
        n2idx = n - 1
        while n1idx >= 0 and n2idx >= 0:
            if nums1[n1idx] > nums2[n2idx]:
                nums1[insert_index] = nums1[n1idx]
                insert_index -= 1
                n1idx -= 1
            else:
                nums1[insert_index] = nums2[n2idx]
                insert_index -= 1
                n2idx -= 1
        while n1idx >= 0:
            nums1[insert_index] = nums1[n1idx]
            n1idx -= 1
            insert_index -= 1
        while n2idx >= 0:
            nums1[insert_index] = nums2[n2idx]
            n2idx -= 1
            insert_index -= 1


class Solution2:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1


def main() -> None:
    inputs = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),  # [1, 2, 2, 3, 5, 6]
    ]
    s = Solution2()
    for nums1, m, nums2, n in inputs:
        s.merge(nums1, m, nums2, n)
        print(nums1)


if __name__ == "__main__":
    main()
