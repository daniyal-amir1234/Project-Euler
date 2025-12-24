fibonacci = [1, 2]

def fibonacci_index():
    for i in range(30000): # 30000 is an arbitrary number
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
        if len(str(fibonacci[i])) == 1000: # first term the contains 1000 digits
            return i+2 # +2 to account for the 2 terms added at the beginning

print(fibonacci_index())