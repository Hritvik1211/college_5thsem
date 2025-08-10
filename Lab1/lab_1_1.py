def find_prime_factors(number):
    divisor = 2
    prime_factors = []

    while divisor * divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    if number > 1:
        prime_factors.append(number)

    return prime_factors


num = int(input("Enter a number to determine its prime factors: "))
print("Prime factors are:", find_prime_factors(num))
