class Solution:
    def first_occurence(self, arr: list, x: int) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                if mid == 0 or arr[mid] != arr[mid - 1]:
                    return mid
                else:
                    high = mid - 1
        return -1

    def last_occurence(self, arr: list, x: int) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                if mid == len(arr) - 1 or arr[mid] != arr[mid + 1]:
                    return mid
                else:
                    low = mid + 1
        return -1

    def count_occurence(self, arr: list, x: int) -> int:
        first = self.first_occurence(arr, x)
        if first == -1:
            return 0
        else:
            return self.last_occurence(arr, x) - first + 1


if __name__ == "__main__":
    s = Solution()
    print(s.count_occurence([10, 20, 20, 20, 30], 20))
