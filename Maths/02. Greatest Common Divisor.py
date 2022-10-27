class Solution:
    def naive_approach(self, num1: int, num2: int) -> int:
        min_value = min(num1, num2)
        while min_value > 0:
            if num1 % min_value == 0 and num2 % min_value == 0:
                break
            min_value -= 1
        return min_value

    def euclidean_approach(self, num1: int, num2: int) -> int:
        while num1 != num2:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1

        return num1

    def optimized_euclidean_approach(self, num1: int, num2: int) -> int:
        if num2 == 0:
            return num1
        return self.optimized_euclidean_approach(num2, num2 % num1)


if __name__ == '__main__':
    s = Solution()
    print(s.naive_approach(12, 6))
    print(s.euclidean_approach(12, 6))
    print(s.optimized_euclidean_approach(12, 6))