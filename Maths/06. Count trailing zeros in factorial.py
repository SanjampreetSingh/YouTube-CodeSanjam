class Solution:
    def naive_approach(self, number: int) -> int:
        fact = 1
        while number > 0:
            fact *= number
            number -= 1

        count = 0
        while fact % 10 == 0:
            count += 1
            fact //= 10
        return count

    def optimized_approach(self, number: int) -> int:
        count = 0
        while number >= 5:
            number //= 5
            count += number
        
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.naive_approach(100))
    print(s.optimized_approach(100))