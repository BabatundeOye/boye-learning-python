#EC2 Random Name Generator

import random
import string

# Departments sharing an AWS environment

dept = ['Marketing', 'Accounting', 'FinOps']

# Allow the user to input how many EC2 instances they want names for and output the same amount of unique names
# Allow the user to input the name of their department that is used in the unique name

ec2_instances = int(input("How many instances do you need? "))
dept = str(input("Enter your department name: "))

# Generate random characters and numbers that will be included in the unique name

char_numb = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(10))
print(char_numb)

# Selected department and EC2 is my unique name

print((dept + ' ' + char_numb) + ' ' + 'is my unique name')