class Solution:
    def bubble_sort(self, arr: list) -> list:
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.bubble_sort([2, 10, 7, 8]))
