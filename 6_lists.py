# Say we want to store a lot of numbers at a time. We could use a lot of 
# variables:
print("Input number 1:")
var1 = input()

print("Input number 2:")
var2 = input()

print("Input number 3:")
var3 = input()

print("Input number 4:")
var4 = input()

list_of_numbers = []
current_position = 0

#len()
while (len(list_of_numbers) < 5):
    print("Input number "+str(current_position)+":")
    current_position += 1
    list_of_numbers.append(input())