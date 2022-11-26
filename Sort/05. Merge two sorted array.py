class Solution:
    def merge_two_sorted_array(self, arr1: list, arr2: list) -> list:
        m = len(arr1)
        n = len(arr2)
        i, j = 0, 0
        res = []
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                res.append(arr2[j])
                j += 1
            else:
                res.append(arr1[i])
                i += 1

        while i < m:
            res.append(arr1[i])
            i += 1

        while j < n:
            res.append(arr2[j])
            j += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.merge_two_sorted_array([1, 2, 3, 4, 5, 6], [1, 2, 4, 5]))
