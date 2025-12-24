x = 600851475143
factors = [] # list of factors

print("running")
for i in range(1, 1000000):  # 1000000 is an abitrary number - YOU MUST INCREASE IT TO SEARCH FOR MORE FACTORS
    if i != 0: # so ACTUALLY if i is 0 then just pass over everything and iterate again
        if x % i == 0: 
            print(i, "divides into", x)
            factors.append(i)
            
# check if the i list/list_of_factors can't divide into anything except itself and 1 (i or 1) hence is prime factor
print(factors)


# check if every number in factors is prime or not
for n in factors:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not prime") # if this shows up, ignore any subsequent statements about the same number
    print(n, "is prime")