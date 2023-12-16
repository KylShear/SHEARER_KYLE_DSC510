# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Kyle Shearer
# 12/16/23

# User Name
user_name = input("Enter your name: ")



# Date of transaction
date = "12/16/23"

# Company name assigned variable
company_name = input("Enter company name: ")

# fo = fiber optics
# Fiber optic length
length_of_fo = input("Enter length of fiber optics: ")

cost_by_foot = 0.00

# Manipulation of cost as length of fiber optics installed increases
if (not float(length_of_fo) > 100):
    cost_by_foot = 0.87
elif (float(length_of_fo) > 100 and float(length_of_fo) <= 250):
    cost_by_foot = 0.80
elif (float(length_of_fo) > 250 and float(length_of_fo) <= 500):
    cost_by_foot = 0.70
else:
    cost_by_foot = 0.50

installation_cost_fo = cost_by_foot * float(length_of_fo)

# Welcome message to User
print("Welcome " + user_name)

print("----------------------------------------------------")
print("----------------------------------------------------")
print("\t\t" + company_name + "\t")
print("\t\t Date: " + date + "\t")
print("----------------------------------------------------")
print("Length of Fiber Optic Cable Purchased: " + (length_of_fo)+"ft")
print("----------------------------------------------------")
print("Total Installation Cost: $", str(installation_cost_fo))
print("----------------------------------------------------")
print("----------------------------------------------------")