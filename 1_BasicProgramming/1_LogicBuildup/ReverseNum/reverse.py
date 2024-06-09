class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31
        negative = x < 0
        rev = 0
        x = abs(x)
        while x != 0:
            if (rev > max_int/10 or 
                rev < min_int/10):
                return 0
            a = x % 10 if x > 0 else x % -10
            rev = rev *10 + a
            x = x//10
        rev = -rev if negative else rev
        return rev
