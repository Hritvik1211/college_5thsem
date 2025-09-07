
def print_fibonacci(n):

    if n <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

print_fibonacci(10)
