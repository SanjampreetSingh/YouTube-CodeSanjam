class Solution:
    def print_unions_of_sorted_arrays(self, arr1: list, arr2: list):
        i, j = 0, 0
        m = len(arr1)
        n = len(arr2)

        while i < m and j < n:
            if i > 0 and arr1[i] == arr1[i - 1]:
                i += 1
            elif j > 0 and arr2[j] == arr2[j - 1]:
                j += 1
            elif arr1[i] < arr2[j]:
                print(arr1[i], end=" ")
                i += 1
            elif arr1[i] > arr2[j]:
                print(arr2[j], end=" ")
                j += 1
            else:
                print(arr1[i], end=" ")
                i += 1
                j += 1
        while i < m:
            if i > 0 and arr1[i] != arr1[i - 1]:
                print(arr1[i], end=" ")
            i += 1
        while j < n:
            if j > 0 and arr2[j] != arr2[j - 1]:
                print(arr2[j], end=" ")
            j += 1


if __name__ == "__main__":
    s = Solution()
    s.print_unions_of_sorted_arrays([1, 2, 3, 4, 5], [1, 5, 5, 6, 6, 6, 7])
