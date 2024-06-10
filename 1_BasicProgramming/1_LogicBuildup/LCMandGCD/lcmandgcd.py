class Solution:
    def lcmAndGcd(self, A , B):
        orgA,orgB = A, B
        while B>0:
            gcd = A%B
            A = B
            B = gcd
        gcd = A
        lcm = (orgA*orgB)//gcd
        return lcm,gcd