class Solution(object):
    def isPalindrome(self, x):
        copyX = x
        #negative = x < 0
        x = abs(x)
        rev = 0
        while x != 0:
            digit  = x%10
            rev = rev * 10 + digit
            x = x//10
        if copyX == rev:
            return True
        else:
            return False
        