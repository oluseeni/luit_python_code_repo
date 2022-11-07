import random
import string


# Generate Random Characters and Numbers for EC2 name.
def random_string(chr_size=8, string=string.ascii_letters + string.digits):
    return ''.join(random.sample(string, chr_size))
    
    
# User Input of desired Number of EC2 Instances to name.
num_ec2 = int(input("Enter number of EC2 Instances to name: "))

if num_ec2 < 1:
    print("Please enter a valid number of instances.")
elif num_ec2 > 1:
    print("")


# User input of desired department.
department = input("enter your deparment name: ")


# Generating combination of department and unique charaters for EC2 names.
for _ in range(1, num_ec2 + 1):
    dep = department
    unique_ec2_name = dep + "-" + random_string()
    print ("Possible EC2 Instance Name:", unique_ec2_name)




