class Solution:
    def binary_search(self, arr: list, element: int, start: int, end: int) -> int:
        if start > end:
            return -1

        mid = (start + end) // 2

        if arr[mid] == element:
            return mid
        elif arr[mid] > element:
            return self.binary_search(arr, element, start, mid - 1)
        else:
            return self.binary_search(arr, element, mid + 1, end)


if __name__ == "__main__":
    s = Solution()
    print(s.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 0, 9))
