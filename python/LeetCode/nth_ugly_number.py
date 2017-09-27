class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_set = set([1, 2, 3, 5])
        ugly_numbers = []
        i = 1
        while len(ugly_numbers) != n:
            if i in ugly_set:
                ugly_numbers += [i]
            else:
                # check primeness
                if is_prime(i):
                    i += 1
                    continue
                else:
                    if not has_non_ugly_prime_factor(i):
                        ugly_numbers += [i]
            i += 1
        print(ugly_numbers)
        return ugly_numbers[n - 1]

def has_non_ugly_prime_factor(val):
    ugly_set = set([1, 2, 3, 5])
    cond = True
    i = 1
    while cond and i < int(val**0.5) + 1:
        if val % i == 0:
            new_pair = (i, val / i)
            if (is_prime(new_pair[0]) and new_pair[0] not in ugly_set):
                return True
            elif (is_prime(new_pair[1]) and new_pair[1] not in ugly_set):
                return True
        i += 1
    return False

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
