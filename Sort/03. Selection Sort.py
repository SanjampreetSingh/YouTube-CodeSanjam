class Solution:
    def selection_sort(self, arr: list) -> list:
        n = len(arr) - 1
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]

        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.selection_sort([10, 4, 2, 50, 30]))
