class Solution:
    def naive_approach(self, number1: int, number2: int) -> int:
        max_value = max(number1, number2)
        while True:
            if max_value % number1 == 0 and max_value % number2 == 0:
                return max_value
            max_value += 1

    def gcd(self, number1: int, number2: int) -> int:
        if number2 == 0:
            return number1
        return self.gcd(number2, number1 % number2)

    def optimal_approach(self, number1: int, number2: int) -> int:
        return (number1 * number2) // self.gcd(number1, number2)


if __name__ == "__main__":
    s = Solution()
    print(s.naive_approach(12, 6))
    print(s.optimal_approach(12, 6))
