class Solution:
    def factorialNumbers(self, N):
        fact=1
        i=2
        l=[]
        while(fact<=N):
            l.append(fact)
            fact*=i
            i+=1
        return l
# SOLUTION 2 IS BELOW

def factorialNumbers(self, N):
        result = []
        
        def helper(fac, i):
            if fac > N:
                return
            result.append(fac)
            helper(fac * (i + 1), i + 1)
        
        helper(1, 1)
        return result