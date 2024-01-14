# DSC 510
# Week 5
# Programming Assignment Week 5
# Author Kyle Shearer
# 1/14/24

#Function for operator/calculator
def performCalculation (op):
    numberOne = input("Enter 1st Variable:")
    numberTwo = input("Enter 2nd Number:")
    result=0
    if(op=='-'):
        result= int(numberOne)-int(numberTwo)
    elif(op=='+'):
        result= int(numberOne)+int(numberTwo)
    elif(op=='/'):
        result= int(numberOne)/int(numberTwo)
    elif(op=='*'):
        result= int(numberOne)*int(numberTwo)
    else :
        print("Wrong Operator type")
    print("Calculated Result: ",result)

# Function for calculating total and average of provided variables
def calculateAverage ():
    Numb = input("Enter Count of Numbers: ")
    sum = 0
    average = 0

    # For Loop
    for x in range (int(Numb)):
        n = int(input("Enter Number: "))
        sum = sum + n
        average = sum / (x+1)
    print("Total: ", sum)
    print("Average: ", average)

    # While Loop
def main():
    while True:
        print("Choose one of the operations below: ")
        print("1. Calculator based on the operator.")
        print("2. Sum and Average of provided number.")
        print("3. Quit")
        perform = input("Enter your choice:")
        if perform == "1":
            operator = input("Enter Operator: ")
            performCalculation(operator)
        elif perform == "2":
            calculateAverage()
        elif perform =="3" :
            print("Quit")
            break
        else:
            print("Wrong Choice.")




if __name__ == "__main__":
    main()