# Sieve of Eratosthenes
# Finding the prime number between 1 and 100
sieve = [True] * 100

for i in range(2, int(100 ** 0.5) + 1):
    if sieve[i] == True:
        for j in range(2 * i, 100, i):
            sieve[j] = False

print([i for i in range(2, 100) if sieve[i] == True])
