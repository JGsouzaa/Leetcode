class Solution:
    def integerBreak(self, n: int) -> int:
        if(n >= 2 and n <= 58):
            if (n == 2 or n == 3):
                return(n-1)
            
            resp = 1
            while (n > 4):
                n -= 3
                resp *= 3
            return(n*resp)
        