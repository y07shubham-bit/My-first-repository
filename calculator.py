# Project no. 1 
# Simple calculator 


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition: " , x + y)
print("Subtraction: " , x - y)
print("Multiplication: " , x * y)
print("Division: " , x / y)
print("Average: " , (x + y) / 2)
print("Exponential: " , x**y)
print("Modulus: " , x % y)


name = input("Kon hai tu: ")
age = input("Kitne saal ka hai: ")
print("Oye" , name + "!" , "Tu hai" , age + "Saal ka" , "Bhag idhar se")

# 22nd december
# Grind day 1 

# if/else

#Simple calculator

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Addition: " , x + y)
print("Subtraction: " , x - y)
print("Multiplication: " , x * y)
print("Division: " , x / y)
print("Average: " , (x + y) / 2)
print("Exponential: " , x**y)
print("Modulus: " , x % y)

#Even/odd

num = int(input("Enter a number: "))

if num % 2 == 0 :
    print("Even")

else :
    print("Odd")

#Positive\negative\zero

num = int(input("Enter number: "))

if num > 0 :
    print("Positive")
elif num < 0 :
    print("Negative")
else :
    print("Zero")

#Grade system

marks = int(input("Enter marks: "))

if marks >= 90 :
    print("Grade A")
elif marks >= 75 :
    print("Grade B")
elif marks >= 60 :
    print("Grade C")
else :
    print("Grade D (fail)")

#Driving license

age = int(input("Enter age: "))

if age >= 18 :
    print("You are eligible for license")
else :
    print("Sorry! You are not eligible for license")

# Loop 

for i in range(1, 11) :
    print(i)
    
for i in range(10, 0, -1) :
    print(i)
    
for i in range(20, 0, -2) :
    print(i)
#🔑 Rule to remember
#Copy code

#range(start, stop, step)
#start → where to begin
#stop → where to stop (not included)
#step → how to move
    
for i in range(1, 21) :
    if i % 2 == 0 :
        print(i)
        
# Multiplication table

num = int(input("Enter a number: "))

for i in range(1, 11) :
        if num*i >= 50 :
            break
        print(f"{num} x {i} = {num*i}")
        
num = int(input("Enter a number: "))

for i in range(1, 11):
    result = num * i
    
    if result % 3 == 0:
        continue   # skip this iteration
    
    print(f"{num} x {i} = {result}")
    
for i in range(1, 11) :
    result = num*i
    
    if result % 4 == 0 :
        continue
        
    print(f"{num} x {i} = {result}")
    
#count = 1
#while count <= 1 :
   # if count == 3 :
  #      break
#    print(count)
#    count += 1
    
#count = 1
#while count <= 5 :
#    if count == 4 :
      #  continue
  #      count += 1
        
    #print(count)
  #    count += 1
    
# functions

def add(a, b) :
    return a + b
    
print(add(10, 7))
print(add(6, 7))


def even_odd(num) :
    if num % 2 == 0 :
        return "Even"
    else :
        return "Odd"
        
print(even_odd(6))
print(even_odd(3))

#🔑 One-line summary (lock this in)
#def → defines the function
#return → sends result & stops function
#print() → displays the returned value
        
        
def calculator(a,b) :
    print("Addition: ", a + b)
    print("Subtraction: ", a - b)
    print("Multiplication: ", a*b)
    print("Division: ", a/b)
    print("Exponential: ", a**b)
    print("Modulus: ", a % b)
    print("Average: ", (a + b)/2)
    
    
calculator(17, 5)

# 23rd december
# Grind Day 2
# Even/odd + positive/negative

num = int(input("Enter a number: "))

if num % 2 == 0 :
        print("Even")
else :
        print("Odd")
        
if num > 0 :
        print("Positive")
elif num < 0 :
        print("Negative")
else :
        print("Zero")
        
# Grade with bounds

marks = int(input("Enter marks: "))

if 0 <= marks <= 100 :
        if marks >= 90 :
            print("Grade A")
        elif marks >= 75 :
            print("Grade B")
        elif marks >= 60 :
            print("Grade C)")
        else :
            print("Grade D")
            
else :
         print("Invalid marks")
         
         
# Table with break
   
for i in range(1, 21) :
         result = num*i
         if result % 4 == 0 :
             continue
         print(f"{num} x {i} = {result}")
         
count = 1
while count <= 10 :
         if count % 2 == 1 :
             count += 1
             continue
         print(count)
         count += 1
         
# Table Function with control

def table_upto_limit(num, limit) :
         for i in range(1, 11) :
             result = num * i
             if result > limit :
                 break
             print(f"{num} x {i} = {result}")
         
table_upto_limit(6, 40)
table_upto_limit(4, 30)

# Filter inside function (continue)

def skip_multiples(num, skip) :
    for i in range(1, 11) :
        result = num * i
        if result % skip == 0 :
            continue
        print(f"{num} x {i} = {result}")
        
skip_multiples(6, 3)
skip_multiples(5, 2)
skip_multiples(7, 3)
skip_multiples(8, 2)

# While loop function

def odd_numbers_upto(n) :
    count = 1
    while count <= n :
        if count % 2 == 0 :
            count += 1
            continue
        print(count)
        count += 1
        
odd_numbers_upto(15)

# Password checker

correct = "python shub batman"
tries = 10

while tries > 0:
    pwd = input("Enter password: ")
    if pwd == correct:
        print("Access granted")
        break
    else:
        tries -= 1
        print("Wrong! Tries left:", tries)

if tries == 0:
    print("Access denied")

# Count positives, negatives, zeros

nums = [2, 5, 7, 8, -9, -5, -2, -8, 0, 0, 0]

pos = 0
neg = 0
zero = 0

for n in nums:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)

# Menu Based Calculator

def calculator(a, b) :

        print("1. Add")  
        print("2. Subtract")  
        print("3. Multiply")  
        print("4. Divide")  
          
        choice = int(input("Choose option: "))  
          
        if choice == 1 :  
            print("Result:", a + b)  
        elif choice == 2 :  
            print("Result:", a - b)  
        elif choice == 3 :  
            print("Result:", a * b)  
        elif choice == 4 :  
            if b != 0 :  
            
                print("Result:", a/b)  
            else :
                print("Cannot divide by zero")  
        else :  
            print("Invalid input")

calculator(72, 51)