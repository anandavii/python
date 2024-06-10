class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = 2 ** 31 - 1
        min = -2 ** 31
        negative = x < 0
        x = abs(x)
        rev = 0
        while x != 0:
            num = x % 10
            rev = rev * 10 + num
            x = x//10
        if rev > max or rev < min:
            return 0 
        if negative:
            rev = -rev
        return rev