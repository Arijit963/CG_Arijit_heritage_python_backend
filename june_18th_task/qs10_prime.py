num = int(input("Enter Number: "))

if num < 2:
    print("Not Prime")

else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            is_prime = False
            break

    print("Prime" if is_prime else "Not Prime")