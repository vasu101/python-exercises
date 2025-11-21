def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 0


# --- Main program ---

n = int(input("Give me a number: "))

if is_even(n):
    print("The number is even.")
else:
    print("The number is odd.")

# Extra: divisible by 4
if n % 4 == 0:
    print("It is also a multiple of 4!")


# Extra: num/check
num = int(input("Give me a number to check: "))
check = int(input("Give me a number to divide by: "))

if num % check == 0:
    print(f"{num} is evenly divisible by {check}.")
else:
    print(f"{num} is NOT evenly divisible by {check}.")
