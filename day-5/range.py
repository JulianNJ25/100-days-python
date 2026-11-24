
# Range alone doesnt do anything, it must be paired in something else like a funcion
# or a for loop
for number in range(a, b):
    print(number)

# Range is non inclusive, so 10 will not be printed here
for number in range(1, 10):
    print(number)

# 10 is going to be printed in here
for number in range(1, 11):
    print(number)

# Prints the total sum of 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)