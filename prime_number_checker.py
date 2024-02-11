def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            print("Not a prime number")
        else:
            print("Prime number")


n = int(input("Enter a number: "))
prime_checker(number=n)