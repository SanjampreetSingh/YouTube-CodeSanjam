class Solution:
    def first_occurence(self, arr: list) -> int:
        low = 0
        high = len(arr) - 1
        arr.reverse()
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < 1:
                low = mid + 1
            else:
                if mid == 0 or arr[mid] != arr[mid - 1]:
                    return mid
                else:
                    high = mid - 1
        return -1

    def count_ones(self, arr: list) -> int:
        start = self.first_occurence(arr)
        if start < 0:
            return 0
        return len(arr) - start


if __name__ == "__main__":
    s = Solution()
    print(s.count_ones([0, 0, 0, 0]))
