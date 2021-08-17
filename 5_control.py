3#if statements

print("type a number:")
num1 = int(input())

if num1 == 5:
    print("you typed in 5.")
elif num1 ==6:
    print("You typed in 6.")
else:
    print("You didn't type 5!")

#while and for loops

while num1 != 4:
    print("not 4")
    print("Type a number:")
    num1 = int(input())

#for x in range(0,3):
#    print(("step" + x))

# An example
print("type the first 2 digits of your SID:")
sid = int(input())

i = 0

while i <= sid:
    print("SID")
    i = i + 1