print("Hey! Lets start the journey.")

# Printing Name and Age

name = input("Enter you name: ")
age =  int(input("What's your age? : "))

print("Name:", name)
print("Age: ", age)


# Control Flow: If/esle, for and while loop

marks = int(input("Enter you marks in Mat350: "))

if marks >= 93: 
    print("A")
elif marks >= 90 and marks <=92:
    print("A-")
elif marks >= 87 and marks <90:
    print("B+")
elif marks >= 83 and marks <=86:
    print("B")
elif marks >= 80 and marks <=82:
    print("B-")
else: print("Fail")

# Adding value to a list and print them through for loop

num = int(input("How many numbers you want to print? :"))

listOfNumbers = []

for i in range(num):
    value = int(input(f"Enter the {i+1} number: "))
    listOfNumbers.append(value)

print("\nThe numbers are: ")
for ans in listOfNumbers:
    print(ans)