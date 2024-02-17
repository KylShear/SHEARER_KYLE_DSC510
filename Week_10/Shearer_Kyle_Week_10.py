# DSC 510
# Week 10
# Programming Assignment Week 10
# Author Kyle Shearer
# 2/17/24

# importing the requests library
import requests

def main():
    print("WELCOME USER!!")
    while True:
        print("Choose from following options: ")
        print("1. Generate Joke?")
        print("2. Quit")
        i = input("Enter Choice")
        if i == "1":
            #Retrieving joke category list
            print("\nAvailable Joke Categories are: ")
            category_list = requests.get(url="https://api.chucknorris.io/jokes/categories")
            print(category_list.json())
            category = input("Choose Category for Joke: ")

            if category in category_list.json():
                #calling on requested category
                joke = requests.get(url="https://api.chucknorris.io/jokes/random?category={}".format(category))
                print("Selected Joke Category: ", joke.json()['categories'][0])
                print("Generated Joke: ",joke.json()['value'])
                print("\n")
            else:
                print("Category does not exist\n")
        elif i == "2":
            break
        else: print("Invalid Input\n")
    # sending get request and saving the response as response object

if __name__ == '__main__':
    main()