#Count the number of prime numbers less than a non-negative number, n.

class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<2):
            return 0
        isPrime = [True]*n
        isPrime[0] = isPrime[1] = False
        
        for i in range(2, math.ceil(math.sqrt(n))):
            if (isPrime[i]):
                for multiples in range(i*i, n, i):
                    isPrime[multiples] = False
                    
        return sum(isPrime)