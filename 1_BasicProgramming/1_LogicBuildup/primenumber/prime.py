# import math module to use the sqrt function
import math
class Solution:
    def isPrime (self, N):
        if N == 1 or N== 0:
            return 0
        a = int(math.sqrt(N))
        for i in range(2, a+1):
            if N % i == 0:
                return 0
        return 1