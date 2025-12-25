list = [1, 2] # start off with numbers 1 and 2 in the list
total = 0

# 50 is an abitrary number - it generates enough numbers to the point list[i] exceeds 4,000,000

for i in range(50): 
    list.append(list[i] + list[i+1])
    if list[i] <= 4000000 and list[i] % 2 == 0:
        total = total + list[i]

print(list)
print(total)