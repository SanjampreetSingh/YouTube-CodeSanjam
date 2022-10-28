class Solution:
    def palindrome_of_a_number(self, number: int) -> int:
        temp = number
        reversed_number = 0

        while temp > 0:
            last_digit = temp % 10
            reversed_number = reversed_number * 10 + last_digit
            temp //= 10

        return reversed_number == number


if __name__ == "__main__":
    s = Solution()
    print(s.palindrome_of_a_number(123321))
    print(s.palindrome_of_a_number(12343321))
