# the largest palindrome that can be made from any two 2-digit numbers is 91 and 99, making 9009

for i in range(900, 999):
    for j in range(900, 999):
        x = i * j
        print(x)
        x = str(x)
        if x == x[::-1]:
            print(x, "IS A PALINDROME") # and then I just search through the list of print(x) to find this specific print statement