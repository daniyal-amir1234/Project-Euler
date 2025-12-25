# split a number into its own digits: the 1s column, the 10s column and the 100s column
# front fill with zeros
# new python method: insert(), e.g.:
# fruits.insert(1, "orange")
# GF: list.insert(index, "string") # insert "string" into list at index 0

string = ""
count = 0
for i in range(1000):
    string = ""

    number = list(str(i))
    if len(number) == 1:
        number.insert(0, "0")
        number.insert(0, "0")
    elif len(number) == 2:
        number.insert(0, "0")

    # the 100s column
    # 'and' is not said in just 100 (one hundred). same for 200, 300 and so on. so remove 3*9=27 from count at the end
    if number[0] == "1":
        string = string + "onehundredand"
    elif number[0] == "2":
        string = string + "twohundredand"
    elif number[0] == "3":
        string = string + "threehundredand"
    elif number[0] == "4":
        string = string + "fourhundredand"
    elif number[0] == "5":
        string = string + "fivehundredand"
    elif number[0] == "6":
        string = string + "sixhundredand"
    elif number[0] == "7":
        string = string + "sevenhundredand"
    elif number[0] == "8":
        string = string + "eighthundredand"
    elif number[0] == "9":
        string = string + "ninehundredand"


    # special case: the teens. this teens special case covers BOTH the 10s and the 1s column for the range 10-19 in any hundreds, if that makes sense
    # 10-19 are dealt with after this whole for loop
    # 110-119, 210-219 and so on are dealt like this:
        
    # "if number[0] != 0" excludes 010-019
    print(number)
    if number[0] != 0 and number[1] == "1" and number[2] == "0": # if 100s = 0, and 10s = 1 and...
        string = string + "ten"
    elif number[0] != 0 and number[1] == "1" and number[2] == "1":
        string = string + "eleven"
    elif number[0] != 0 and number[1] == "1" and number[2] == "2":
        string = string + "twelve"
    elif number[0] != 0 and number[1] == "1" and number[2] == "3":
        string = string + "thirteen"
    elif number[0] != 0 and number[1] == "1" and number[2] == "4":
        string = string + "fourteen"
    elif number[0] != 0 and number[1] == "1" and number[2] == "5":
        string = string + "fifteen"
    elif number[0] != 0 and number[1] == "1" and number[2] == "6":
        string = string + "sixteen"
    elif number[0] != 0 and number[1] == "1" and number[2] == "7":
        string = string + "seventeen"
    elif number[0] != 0 and number[1] == "1" and number[2] == "8":
        string = string + "eighteen"
    elif number[0] != 0 and number[1] == "1" and number[2] == "9":
        string = string + "nineteen"
        
    # the 10s column
    if number[1] == "2":
        string = string + "twenty"
    elif number[1] == "3":
        string = string + "thirty"
    elif number[1] == "4":
        string = string + "forty"
    elif number[1] == "5":
        string = string + "fifty"
    elif number[1] == "6":
        string = string + "sixty"
    elif number[1] == "7":
        string = string + "seventy"
    elif number[1] == "8":
        string = string + "eighty"
    elif number[1] == "9":
        string = string + "ninety"


    # the 1s column
    if number[1] != "1":
        if number[2] == "1":
            string = string + "one"
        elif number[2] == "2":
            string = string + "two"
        elif number[2] == "3":
            string = string + "three"
        elif number[2] == "4":
            string = string + "four"
        elif number[2] == "5":
            string = string + "five"
        elif number[2] == "6":
            string = string + "six"
        elif number[2] == "7":
            string = string + "seven"
        elif number[2] == "8":
            string = string + "eight"
        elif number[2] == "9":
            string = string + "nine"


    # print(number)
    print(string)

    count = count + len(string)
    print("Count", count)

# SHIT string WASN'T RESET HERE SO IT COUNTS ninehundredandninetynine AGAIN HERE
string = ""
# string = string + "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen" # i thought i needed this line what

string = string + "onethousand"
count = count + len(string)
print(count)
print("Final count:", count-27)