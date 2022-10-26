class Solution:
    def sum_of_first_n_natural_numbers(self, number: int) -> int:
        return (number * (number + 1)) // 2


if __name__ == '__main__':
    s = Solution()
    print(s.sum_of_first_n_natural_numbers(5))