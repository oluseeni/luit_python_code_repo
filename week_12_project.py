# This is week 12 project.

# In this project, we will be creating a list of AWS Service Inventory

# Objectives of the project are staed below:

# Create a list of services using Python. IE: S3, Lambda, EC2, etc

# 1. The list should be empty initially.
# 2. Populate the list using append or insert.
# 3. Print the list and the length of the list.
# 4. Remove two specific services from the list by name or by index.
# 5. Print the new list and the new length of the list.

# 1. The list should be empty initially.
aws_serv_inv = []

# 2. Populate the list using append or insert.
aws_serv_inv.append("S3")
aws_serv_inv.append("Lambda")
aws_serv_inv.append("DynamoDB")
aws_serv_inv.append("SNS")
aws_serv_inv.append("SQS")
aws_serv_inv.append("Elasticache")
aws_serv_inv.insert(3, "Cloud9")
aws_serv_inv.insert(4, "API Gateway")

# 3. Print the list and the length of the list.
print(aws_serv_inv)
print(len(aws_serv_inv))

# 4. Remove two specific services from the list by name or by index.
aws_serv_inv.remove("SNS")
del aws_serv_inv[5]

# 5. Print the new list and the new length of the list.
print(aws_serv_inv)
print(len(aws_serv_inv))

# This completes the python code for my week 12 project.
# Thank you and see you on the next one.
