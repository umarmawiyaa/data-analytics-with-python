# Question 1: Working with Lists

numbers = [12, 7, 20, 5, 8, 15, 6, 11]

print("All numbers:")
total = 0

for number in numbers:
    print(number)
    total += number

print("Sum of all numbers:", total)

print("Even numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number)



# Question 2: Dictionary Basics

student = {
    "name": "umar",
    "age": 18,
    "course": "Python",
    "marks": [75, 68, 82]
}

print("\nStudent details:")
for key, value in student.items():
    print(key, ":", value)

total_marks = 0
for mark in student["marks"]:
    total_marks += mark

average = total_marks / len(student["marks"])
print("Average marks:", average)

if average >= 50:
    print("Result: Passed")
else:
    print("Result: Failed")


    # Question 3: List of Dictionaries

employees = [
    {"name": "Ali", "department": "IT", "salary": 50000},
    {"name": "Sara", "department": "HR", "salary": 45000},
    {"name": "Umar", "department": "Finance", "salary": 60000}
]

highest_paid = employees[0]
total_salary = 0

print("\nEmployee details:")
for employee in employees:
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print("Salary:", employee["salary"])
    print()

    total_salary += employee["salary"]

    if employee["salary"] > highest_paid["salary"]:
        highest_paid = employee

print("Highest salary employee:", highest_paid["name"])
print("Highest salary:", highest_paid["salary"])
print("Total salary expense:", total_salary)


# Question 4: While Loop with User Input

entered_numbers = []

print("\nEnter numbers one by one. Enter -1 to stop.")

while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    if number == -1:
        break

    entered_numbers.append(number)

print("Complete list:", entered_numbers)

if entered_numbers:
    print("Largest number:", max(entered_numbers))
    print("Smallest number:", min(entered_numbers))
else:
    print("No numbers were entered.")


    # Question 5: Word Frequency Counter

sentence = input("\nEnter a sentence: ")
words = sentence.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:")
for word, count in word_count.items():
    print(word, ":", count)


    # Question 6: Nested Loops – Multiplication Table

print("\nMultiplication table from 1 to 5:")

for row in range(1, 6):
    for column in range(1, 6):
        print(row * column, end="\t")
    print()