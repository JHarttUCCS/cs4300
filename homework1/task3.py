# Jacob Hartt
# Tom Hastings
# CS4300.001
# 02/18/2025


# Returns 1 if num postive, 0 if 0, and -1 if negative
def pos_neg(num):
    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1


def print_ten_primes():
    n = 10 # num of primes to print
    currNum = 2
    primes = []

    for i in range(n):
        # Search for the next prime
        primeReached = False
        while not primeReached:
            primeReached = True
            for prime in primes:
                if currNum % prime == 0:
                    primeReached = False

            currNum += 1

        primes.append(currNum-1) # -1 accounts for extra cycle at the end of the while loop

    print(*primes, sep=', ')

# print_ten_primes()


def sum(start, end):
    currNum = start
    total = 0

    while currNum <= end:
        total += currNum
        currNum += 1

    return total
