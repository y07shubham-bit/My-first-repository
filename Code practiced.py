
# Correct number analyzer (final version)

def analyze_number(n) :
    if n == 0 :
        return "Zero"
    elif n > 0 :
        if n % 2 == 0 :
            return "Positive even"
        else :
            return "Positive odd"
            
    else :
        if n % 2 == 0 :
            return "Negative even"
        else :
            return "Negative odd"
            
num = int(input("Enter a number: "))
print(analyze_number(num))

# Loop control (mastery)

def filtered_table(num) :
        for i in range(1, 11) :
            result = num*i
            if result > 50 :
                break
            if result % 3 == 0 :
                continue
            print(result)
            
filtered_table(7)

# Counter with conditions

nums = [12, 15, 7, 30, 9, 42, 55, 60]

count = 0 
for n in nums :
        if n > 5 and n % 5 == 0 :
           count += 1
           
       
            
print("Count: ", count)

# Smart Counter function

def smart_count(nums, limit, div):
    count = 0
    for n in nums:
        if n > limit and n % div == 0:
            count += 1
    return count

nums = [10, 15, 20, 25, 30, 35, 40, 45]
print(smart_count(nums, 30, 10))
        
# Controlled input loop

while True:
    n = int(input("Enter number (1–10): "))
    if 1 <= n <= 10:
        print("Accepted:", n)
        break
    else:
        print("Invalid, try again")
        
# Function that explains itslef

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(even_or_odd(7))
print(even_or_odd(12))

# 30th December
# Grind day 6

# Smart grade system

def grade_with_remark(marks) :
        if marks < 0 or marks > 100 :
            return "Invalid marks"
        elif marks >= 95 :
            return "A", "Excellent"
        elif marks >= 80 :
            return "B", "Very good"
        elif marks >= 65 :
            return "C", "Good"
        elif marks >= 35 :
            return "D", "Pass"
        else :
            return "F", "Fail"
            
m = int(input("Enter marks: "))
grade, remark = grade_with_remark(m)
print("Grade: ", grade)
print("Remark: ", remark)

# Number category

def number_category(n):
    if n == 0:
        return "Zero"
    
    sign = "Positive" if n > 0 else "Negative"
    parity = "Even" if n % 2 == 0 else "Odd"
    
    return sign + " " + parity

print(number_category(7))
print(number_category(-8))

# Design function (one clear decision)

def can_vote(age) :
        if age < 0 :
            return "Invalid age"
        if age >= 18 :
            return "Eligible to vote"
        return "Not Eligible to vote"
        
print(can_vote(69))
print(can_vote(15))
print(can_vote(-35))

# Threshold counter (Logic tightening)

def count_above_threshold(nums, threshold):
        count = 0
        for n in nums:
            if n > threshold:
                count += 1
        return count
                
numbers = [9, 74, 63, 26, 29, 65, 77, 89]
print(count_above_threshold(numbers, 50))

# Result classifier 

def result_status(marks) :
        if marks < 0 or marks > 100 :
            return "Invalid", "Check input"
            
        if marks >= 75 :
            return "Pass", "Good performance bach gaya lol"
        elif marks >= 40 :
            return "Pass", "Needs improvement yaar janmo se sun raha "
        else :
            return "Fail", "Work harder dawg, Failure kahi ka "
            
            
status, message = result_status(69)
print(status)
print(message)

# Result evaluator function

def result_status(marks) :
            if marks < 0 or marks > 100 :
                return "Invalid marks"
            elif marks >= 50 :
                return "Pass"
            else :
                return "Fail"
                
print(result_status(75))
print(result_status(55))
print(result_status(33))

# Range check 

def range_check(n) :
    
    if n < 0 :
        return "Negative"
    elif n <= 10 :
        return "0 - 10"
    elif n <= 20 :
        return "10 - 20"
    else :
        return "Above 20"
        
print(range_check(25))
print(range_check(15))
print(range_check(2))

# Combined logic function

def describe_number(n) :
    if n == 0:
        return "Zero"
        
    result = "Positive" if n > 0 else  "Negative"
    result += "Even" if n % 2 == 0 else  "Odd"
    
    return result
    
print(describe_number(5))
print(describe_number(74))
print(describe_number(-69))


# Shub's code 

def describe(n) :
    
    if n == 0 :
        return "Zero"
        
    sign = "Positive" if n > 0 else "Negative"
    parity = "Even" if n % 2 == 0 else "Odd"
    
    return sign + " " + parity
    
print(describe(9))
print(describe(0))
print(describe(-69))

# Controlled loop (real world logic)
    
for i in range(1, 101) :
    if i > 75 :
        break
    if i % 4 == 0 :
        continue
    print(i)
    
# Smart count

def smart_count(nums, limit, div) :
    count = 0
    for n in nums :
        if n > limit and n % div == 0 :
            count += 1
    return count
    
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(smart_count(nums, 50, 2))


# Controlled loop

def limited_sum(limit):
    total = 0
    while True:
        n = int(input("Enter number (0 to stop): "))
        if n == 0:
            break
        if total + n > limit:
            print("Limit exceeded")
            break
        total += n
    return total

print("Final sum:", limited_sum(500))



# Bank 

def withdraw(amount, balance=10000):
    if amount <= 0:
        return "Invalid amount"
    if amount > balance:
        return "Insufficient balance"
    if amount % 100 != 0:
        return "Amount must be multiple of 100"
    return "Withdrawal successful"

print(withdraw(500))
print(withdraw(123))
print(withdraw(20000))

# Describe number

def describe_number(n):
    if n == 0:
        return "Zero"
    sign = "Positive" if n > 0 else "Negative"
    parity = "Even" if n % 2 == 0 else "Odd"
    
    return sign + " " + parity
    
print(describe_number(69))



    
    
    