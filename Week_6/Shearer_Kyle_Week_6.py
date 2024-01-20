# DSC 510
# Week 6
# Programming Assignment Week 6
# Author Kyle Shearer
# 01/20/24

#Function for temperature input/value
def temp_list():
    temperatures = [];
    while True:
        temp_input = input("Input Temperature or q to exit: ");
        if temp_input == "q":
            break;
        elif temp_input.isalpha():
            print("Invalid temperature value")
        else:
            temperatures.append(float(temp_input))

    return temperatures
#main where we call on the function as well as attain specific results.
def main():
    result_list = temp_list()
    largest_temp = max(result_list)
    print("Largest Temperature Entered: ", largest_temp)
    smallest_temp = min(result_list)
    print("Smallest Temperature Entered: ", smallest_temp)
    total = len(result_list)
    print("Total Temperatures Enteres: ", total)

if __name__ == "__main__":
    main()




