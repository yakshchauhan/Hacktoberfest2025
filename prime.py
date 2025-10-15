# Print first N prime numbers

n = int(input("Enter how many prime numbers you want: "))
count = 0
num = 2

print(f"First {n} prime numbers are:")
while count < n:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
    num += 1
