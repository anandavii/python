class Solution:    
    #Complete this function
    def printNos(self,N):
            if N<=0:
                return
            self.printNos(N-1)
            print(N,end=" ")

# Option 2 is Below   
    #Complete this function
    def printNos(self,N):
        def fun(N):
            if N<=0:
                return
            fun(N-1)
            print(N,end=" ")
        fun(N)