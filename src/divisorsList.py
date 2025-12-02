# Finding all divisors efficiently by checking only up to the square root of the number.


import math

num = int(input("Enter a number: "))

result = []
limit = int(math.sqrt(num))

for i in range(1, limit + 1):
    if num % i == 0:
        result.append(i)
        if i != num // i:
            result.append(num // i)

print(sorted(result))
