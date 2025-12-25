def dectobin(dec):
    columns = 20 # YOU CAN CHANGE THIS NUMBER - 20 columns goes up to 1 million
    bin = [0]*columns
    power = columns - 1 # power here is 19
    a = power # a is just a counter thingy (idk how to explain this)
    for i in range(columns):
        if (dec / 2**power) >= 1:
            bin[power-a + (2*i)] = 1 
            dec = dec - (2**power)
        power = power - 1 # decrease the power by 1 (shifting to the next column)
    return bin

# print(dectobin(1000000)) # put any number in here

total = 0

for i in range(1, 999999): # have to start from 1 - DO NOT START FROM 0
    decstring = str(i)
    if decstring == decstring[::-1]:
        print(decstring, "is palindromic!")
        binstring = dectobin(int(decstring))

        for j in range(len(binstring)): # remove 0s at the front of binstring before the first 1
            # print(binstring)
            while binstring[0] != 1: # while the first element of the string does not equal 1
                if binstring[j] == 0:
                    binstring.pop(j) #list.remove("specific value"); list.pop(specific index) - no square brackets for either

        if binstring == binstring[::-1]:
            print(binstring, "is palindromic!")
            total = total + int(decstring)

print(total)
