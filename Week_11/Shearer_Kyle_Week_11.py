# DSC 510
# Week 11
# Programming Assignment Week 11
# Author Kyle Shearer
# 2/24/24


class CashRegister:
    number_items = 0

    def __init__(self):
        self.items = []
    def add_item (self,price):
        self.items.append(price)
        self.number_items = self.number_items+1
        print("item add with price ${}".format(price))

    def getTotal(self):
        return sum(self.items)

    def getCount(self):
        return self.number_items


def main():
    print("Welcome!")
    a = CashRegister()

    while True:
        print("Choose from following options: ")
        print("1. Add Item")
        print("2. Total Price & Count of Items")
        print("3. Quit")
        i = input("Enter Choice")
        if i == "1":
            x = input("Enter Item Price: ")
            if isinstance(x, (int, float)):  # pass tuple
                a.add_item(float(x))
            else:
                print("Invalid Input for Price")


        elif i == "2":
            print("Total Price of all Items: {}".format(a.getTotal()))
            print("Total Items: {}".format(a.getCount()))
        elif i == "3":
            break
        else: print("Invalid Input\n")



if __name__ == '__main__':
    main()