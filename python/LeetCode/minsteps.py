class Solution(object):
    
    def minSteps(self, n):
        if n == 1:
            return 0
        if (is_prime(n)):
            return n
        else:
            factor_pairs = f(n)
            min_value = sys.maxint
            for pair in factor_pairs:
                if pair[0] == n or pair[1] == n:
                    continue
                current_value = self.minSteps(pair[0]) + self.minSteps(pair[1])
                if current_value < min_value:
                    min_value = current_value
            return min_value
    
def f(val):
    return [(i, val / i) for i in range(1, int(val**0.5)+1) if val % i == 0]

def is_prime(n):
    '''check if integer n is a prime'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2: 
        return True    

    # all other even numbers are not primes
    if not n & 1: 
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True