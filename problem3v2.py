def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


print(is_prime(87625999))