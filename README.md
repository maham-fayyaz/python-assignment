# Python Programming Assignment: Number Exploration Tool #
## Instructions: ##
### 1. Creating an Empty List
First we will create an empty **list* to store the numbers*

`num_list=[]`
### 2. Asking for User's Name

then ask for prompts the **user* to enter their name and input is stored in the variable user_name.*

`user_name=input("Enter your name:")`
### 3. Printing an Empty Line
`print()`
### 4. Loop for Collecting Favorite Numbers
Then using a **for* loop, the program asks for three numbers one by one.* 

`for i in range(1,4):`

~ *The numbers are converted to integers using int(), and then added to the list num_list=[] .*

`num=int(input(f"Enter your {i} favorite number:"))`

~ then the entered number is **appended* to the list num_list.*

`num_list.append(num)`
### 5. Displaying the Final Message
After the **loop*, the program prints a personalized greeting to the user, using their name stored in user_name, and suggests exploring their *favorite numbers.

`print(f"\nHello, {user_name}! let's explore your favorite number:")`
### 6. Check if Numbers Are Even or Odd
We use **loop* which goes through each number in *num_list.
 
`for num in num_list:`

*If: if the remainder when divided by 2 is (0), Or condition is (TRUE), the line prints a message saying that the number is *even*.
else: If the number is not divisible by (2), or the condition num % 2 == 0 is (FALSE) , then *else* prints a message saying that the number is *odd.

`if num % 2 == 0:`

`>>print(f"The number {num} is even.")`

`else:`

`>>print(f"The number {num} is odd.")`
`>print()`

~**This last line prints an empty line**
### 7. Create Tuples with Numbers and Their Squares
Next, the program iterates over the **list* of numbers again, creating a *tuple* for each number that includes the number and its square. This is stored in another *list* and print it .*

`for num in num_list:`

` >`print(f"The number {num} and its square:`
`({num},{num ** 2})")``
### 8.Calculate and Display the Sum:
*Then we will calculates the sum of all the numbers stored in num_list and assigns this total to the variable sum_numbers and print the result.*

`sum_numbers=sum(num_list)`

`>print(f"\nAmazing! The sum of your favorite numbers is: {sum_numbers}")`
### 9.Checking If Sum is Prime:
Then program checks if the sum of the three numbers is a **prime number. If the sum is 0 or 1, it directly prints that it is not a **prime number. Otherwise, it checks if the sum is divisible by any number between 2 and the sum minus one. If it finds any divisor, it declares the sum as not **prime; otherwise, it prints that the sum is **prime.

``prime = False  ``

`if sum_numbers == 0 or sum_numbers == 1:`

`>>print(sum_numbers, "is not a prime number")`

`else:`

`>for i in range(2, sum_numbers):`

` >>if (sum_numbers % i) == 0:`

 `>>>prime = True`

`if prime:`

 `>>print(f"Alas! {sum_numbers}, is not a prime number")`

` else:`

`>>print(f"Wow! {sum_numbers}, is a prime number")`
