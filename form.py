class human:
    def __init__(self, fName, lName, age):
        self.firstName = fName
        self.lastName = lName
        self.age = age

    def display(self):
        print('Name: ' + self.firstName + ' ' + self.lastName + '\nAge: ' + self.age)

class student(human):
    def __init__(self, fName, lName, age, studentNumber, school):
        super().__init__(fName, lName, age)
        self.studentNumber = studentNumber
        self.school = school

    def display(self):
        print('Name: ' + self.firstName + ' ' + self.lastName + '\nAge: ' + self.age 
            + '\nStudent Number: ' + self.studentNumber + '\nSchool: ' + self.school)

global person

print('Please enter your full name.')
fullName = input().split(' ')   # Splits the converted name into a list containing first and last name
                                # e.g -> 'John Doe' => ['John', 'Doe']

if len(fullName) <= 1:
    fullName.append('')

# if type(fullName) is not str:
# Don't have to test, names are strings be default

print('Please enter your age.')
age = input()

while age.isdigit() == False:
    print('Please enter a number as your age.')
    age = input()

global isStudent
isStudent = False
# Instantiates the 'isStudent' global variable, with a default value of false.

print('Are you a student?')
res = input()

if res == True or res.lower() == 'yes' or res.lower() == 'y':
    isStudent = True
# Because we set 'isStudent' as false initially, we only have to test if it's a positive response, and if
# so, we overide it. This means we use less code for the same outcome.

if isStudent:
    print('Please enter your student number.')
    studNum = input()
    while studNum.isdigit() == False:
        print('Your student number has to be a number. Please enter a number.')
        studNum = input()
    
    print('Please enter the name of your school.')
    school = input()
    
    person = student(fullName[0], fullName[1], age, studNum, school)
else:
    person = human(fullName[0], fullName[1], age)

person.display()
