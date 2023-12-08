# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Kyle Shearer
# 12/8/23

# User Name
user_name = input("Enter your name: ")

# Welcome message to User
print("Welcome " + user_name)

# Date of transaction
date = "12/05/23"

# Company name assigned variable
company_name = input("Enter company name: ")

# fo = fiber optics
# Fiber optic length
length_of_fo = input("Enter length of fiber optics: ")

# Fiber optic price per foot is $0.87
#Total price = 0.87 x Fiber Optic length
installation_cost_fo = 0.87 * float(length_of_fo)
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