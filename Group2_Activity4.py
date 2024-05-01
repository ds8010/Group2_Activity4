"""
GROUP 2
Authors:

        1.Youssef Marak:
             contributed to the creating class article and defining the function read_data()
        
        2.
        
        3.Dona Pal:
            Contributed in the menu(),beautify(),main() function. Also defined the displayCart() function
            under the class Cart. 
        
GIT Repository: https://github.com/ds8010/Group2_Activity4.git

Manifesto: This program uses Python Object Oriented programming (OOP) skills to simulate a shopping cart of a DVD store.
"""


import csv
# Global dictionary to store inventory
INVENTORY = {}

# Function to read data from CSV file and populate INVENTORY dictionary
def read_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name = row[0]
            quantity = row[1]
            price = row[2]
            INVENTORY[name] = [int(quantity),float(price)]

# Class representing an article
class Article:
    __slots__ = ['__name','__quantity','__price']
    def __init__(self, name, quantity, price):
        self.__name = name
        self.__quantity = quantity
        self.__price = price
 
    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getQuantity(self):
        return self.__quantity
    
    def setQuantity(self, quantity):
        self.__quantity = quantity
    
    def __str__(self):
        return 'Article: '+ self.__name + ' Quantity: '+ str(self.__quantity)+' Price: '+str(self.__price)
    
class Cart:
    def __init__(self):
        self.__list_of_purchased = [] # stores the article object purchased
        self.name_purchased = []   # stores the name of the articles
    
    def displayCart(self):
        if self.__list_of_purchased == []:
            print('Your cart is empty.')
        else:
            n=1
            print("You have "+str(len(self.__list_of_purchased))+" items in your shopping cart.")
            for product in self.__list_of_purchased:
                print("ITEM "+str(n)+": ",product) 
                n+=1




def menu():
    """Menu Function that displays the Menu of options when called."""


    print("\t                 MENU                     ")
    print("_______________________________________________________")
    print("\t1. List all of items, inventory and price")
    print("\t2. List shopping cart items")
    print("\t3. Add an item to the shopping cart")
    print("\t4. Remove an item from the shopping cart")
    print("\t5. Checkout")
    print("_______________________________________________________")
    print("\t6. Exit")

def beautify():
    # To print a line of stars

     print('*'*100)


def main():
    """ This is our main function."""

    print('''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                \tWelcome  
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
    read_data('products.csv')
    cart = Cart()
    
    while True:
        menu()
        beautify()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            beautify()
            print("List of products in inventory:")
            print('''KEY:
Name: [Quantity, Price]\n''')
            
            for key in INVENTORY:
                print(key,":",[INVENTORY[key][0],INVENTORY[key][1]])
            beautify()

        elif choice == '2':
            print('Items in your shopping cart: ')
            cart.displayCart()
            beautify()
                
        elif choice == '3':
            name = input("Enter the name of the product to add: ").lower()
            quantity = int(input("Enter the quantity to add: "))
            if quantity < 0:
                print('Quantity cannot be negative. Try again! ')
                quantity = input("Enter the quantity to add: ")
            cart.addProduct(name, quantity)
            beautify()

        elif choice == '4':
            name = input("Enter the name of the product to remove: ")
            quantity = int(input("Enter the quantity to remove: "))
            if quantity < 0:
                print('Quantity cannot be negative. Try again! ')
                quantity = input("Enter the quantity to add: ")
            cart.removeProduct(name, quantity)
            beautify()

        elif choice == '5':
            cart.checkout()
            beautify()

        elif choice == '6':
            print("Program is closed!")
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again!")

        close = input('Do you want to continue? [y/n]: ').lower()
        beautify()
        if close == 'y':
            continue
        elif close == 'n':
            print("Program is closed!")
            break 
        else:
            print('Invalid input!')
            close = input('Do you want to continue? [y/n]: ').lower()

if __name__ == "__main__":
     main()
