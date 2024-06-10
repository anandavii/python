class Solution:
    def sumOfDivisors(self, N):
        total = 0
        for i in range(1, N + 1):
            total += (N // i) * i
        return total