numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in numbers:
    if i < 2:
        continue
    if i == 2:
        primes.append(i)
        continue

    if i % 2 == 0:
        not_primes.append(i)
        continue

        for j in range(3, int(j ** 0.5) + 1, 2):
            if j % i == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print("Простые числа: ", primes)
print("Остальные числа: ", not_primes)






