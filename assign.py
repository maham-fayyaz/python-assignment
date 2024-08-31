num_list = []
user_name = input("Write your name: ")
print()

# collect three favorite numbers 
for i in range(1, 4):
    num = int(input(f"enter your {i} favorite number: "))
    num_list.append(num)

# check if each number is even or odd
print(f"\nHello, {user_name}! let's explore your favorite number")
for num in num_list:
    if num % 2 == 0:
        print(f"the number {num} is even")
    else:
        print(f"the number {num} is odd")
# display each number and its square
print()
for num in num_list:
    print(f"the number {num} and its square: ({num}, {num ** 2})")

# calculate and display the sum of the numbers 
sum_numbers = sum(num_list)
print(f"\nAmazing! the sum of your favorite numbers is: {sum_numbers}")

# check if the sum is a prime number 
if sum_numbers == 0 or sum_numbers == 1:
    print(num, "is not a prime number")
elif sum_numbers > 1:
    for i in range(2, sum_numbers):
        if (num % i) == 0:
            prime = True
    if prime:
        print(f"Alas! {sum_numbers}, is not a prime number")
    else:
        print(f"Wow! {sum_numbers}, is a prime number")