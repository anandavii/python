# IN PYTHON WE CANT SOLVE THIS WITH RECURSION OR LOOPS IN THE SPECIFIED TIMELIMIT
# FOR n  >1000 it takse too much time and recursion depth is reached
# this can be solved in JAVA EASILY, hence refer both the codes

class Solution:
    def sumOfSeries(self,n):
        #code here
        sum = 0
        if n <= 0:
            return 0
        sum += n ** 3
        sum += self.sumOfSeries(n-1)
        return sum
    
# Option 2 below

    def sumOfSeries(self,n):
        #code here
        sum = 0
        if n <= 0:
            return 0
        #sum += n ** 3
        sum += n**3 + self.sumOfSeries(n-1)
        return sum