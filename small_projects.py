# Calculator App:

print("\nWelcome to the calculator application!\n")
operator = input("Enter your opeartion (+, -, *, /): ")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

def add(a,b):
        return a + b
def sub(a,b):
        return a - b
def mul(a,b):
        return a * b
def div(a,b):
        return a / b


match operator: 
    case "+" :
        print(f"Addition of these numbers: {add(a,b)}")
    case "-" :
        print(f"Subtraction of these numbers: {sub(a,b)}")
    case "*" :
        print(f"Multiplication of these numbers: {mul(a,b)}")   
    case "/" :
        print(f"Division of these numbers: {div(a,b)}")  
   

# Login System


def signUp():
      print("---Sign Up---")
      username = input("Enter username: ")
      password = input("Enter password: ")

      print("Sign up successful!\n")
      return username, password

def login_system(Check_username, Check_password):
      
      attempts = 3
      print("---Login System---")
      while attempts > 0: 
          username = input("Enter Usernmae: ")
          password = input("Enter password: ")

          if username == Check_username and password == Check_password:
                print("Login Successfull!")
                return True
          else: 
            attempts -= 1
            print("Invalid username or password!")
            print(f"Attempt remaining: {attempts}")

      print('Account locked!')
      return False
           
      
saved_username ,saved_password = signUp()
login_system(saved_username, saved_password)

# Student Marks Manager

print("---Students Marks--")

def students_marks():
     Student_mList =[]

     n = int(input("Enter the number of students marks wants to show:"))
     for i in range(n):
          marks = float(input(f"Emter the marks of studnet number{i+1}: "))
          Student_mList.append(marks)
     return Student_mList

def calculate_average(marks):
     total = sum(marks)
     avr = total / len(marks)
     return avr
def highest_lowest(marks):
     highest = max(marks)
     lowest = min(marks)
     return highest, lowest

studnet_markss = students_marks()

average = calculate_average(studnet_markss)
high, low = highest_lowest(studnet_markss)


print("---Results---")

print(f"Marks: {studnet_markss}")
print(f"Average: {average}")
print(f"Highest: {high}")
print(f"Lowest: {low}")

# To-Do List App

tasks = []

def add_task():
     task = input("Enter task: ")
     tasks.append(task)
     print("task added successfully!")

def view_task():
    if len(tasks) == 0:
      print("No task found!")  

    else: 
         print("\n Tasks: ") 
         for i in range(len(tasks)):
              print(i+1, "task" , tasks[i])
              print()

def delete_task():
     view_task()
     if len(tasks) == 0:
         return

     num = int(input("Enter task number: "))

     if 1<=num<=len(tasks):
          removed = tasks.pop(num -1) 
          print("Task removed", removed, "\n")

     else: 
          print('Invalid task!')
while True: 
    print('---To do list---')
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input('Enter choice: ')

    if choice == "1": 
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        delete_task()
    elif choice == "4": 
        print("Thank you!")
        break

    else:
        print('Invalid choice!')
      
# Number Guessing Game

import random

def guessing_game():
     
     num = random.randint(1,10)
     attempt = 0
     print("Guessing game!")
     print("Guess number between 1 to 100")

     while True: 
          number = int(input("Guess any number between 1 to 100: "))
          attempt += 1

          if number > num: 
               print("High guess!")
          elif number < num:
               print("Low guess!")
          else: 
               print(f"Correct Guess! You guessed it in {attempt} attempt")
               break
guessing_game()          
 
#  ATM Simulation

def check_balanace(balance):
     print("Your current balance:", balance)
     

def deposite(balance):

     amount = float(input("Enter youy deposite amount: "))

     if amount > 0:
          balance += amount
          print("Deposite Successfull!")
     else:
          print("Invalid Choice!")

     return balance

def withdraw(balance):
    amount = float(input("Enter your withdrw amount: "))

    if amount <= 0:
          print("Invalid choice!")
    elif amount > balance:
          print("Insufficient Balance!")
    else:
          balance -= amount
          print("Withdraw Successfull!")

    return balance

def atm():

    balance = 1000


    while True:
        print("---ATM Menu---")
        print("1. Check Balance")
        print("2. Deposite Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
               check_balanace(balance)

        elif choice =="2":
              balance = deposite(balance)

        elif choice == "3":
              balance =  withdraw(balance)

        elif choice == "4":
               print("Thank you for using ATM")
               break

        else:
               print("Invalid choice!")

atm()
