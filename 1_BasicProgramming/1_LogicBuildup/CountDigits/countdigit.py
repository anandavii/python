class Solution:
    def evenlyDivides (self, N):
        copyN = N
        count = 0
        while copyN >= 1:
            a = copyN % 10
            if a != 0:
                if N%a ==0:
                    count += 1
            copyN = copyN//10
        return count