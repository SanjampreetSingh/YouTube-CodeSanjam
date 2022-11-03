class Solution:
    def sieve(self, n: int) -> list:
        primes = [True for _ in range(n+1)]

        p = 2
        while p*p <=n:
            if primes[p]:
                j = p * p
                while j <= n:
                    primes[j] = False
                    j += p
            p += 1

        ans = []
        for i in range(2,n+1):
            if primes[i]:
                ans.append(i)

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.sieve(23))