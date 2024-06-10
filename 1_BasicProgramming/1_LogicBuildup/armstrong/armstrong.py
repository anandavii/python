class Solution:
    def armstrongNumber (self, n):
        copyN = n
        sum = 0
        while n >0:
            num = n % 10
            sum = sum + (num ** 3)
            n = n//10
        if sum == copyN:
            return "Yes"
        else:
            return "No"