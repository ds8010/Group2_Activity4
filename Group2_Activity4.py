"""
GROUP 2
Authors:

        1.Youssef Marak:
             Contributed to the creating class article and defining the function read_data()
        
        2.Yosef Shibele:
            Contributed on most part of the class Cart methods, addProduct(), removeProduct() and checkout().
        
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
    """Creats a blueprint for a product object. """

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
        return 'Article: '+ self.__name + '  Quantity: '+ str(self.__quantity)+'  Price: '+str(self.__price)
    
class Cart:
    """Creates a blueprint for the shopping cart object. """

    def __init__(self):
        self.__list_of_purchased = [] # stores the article object purchased
        self.name_purchased = []   # stores the name of the articles

    # A method used to add items in the shopping cart
    def addProduct(self, name, quantity): # A method used to add items in the shopping cart
        """Adds an item to the shopping cart and updates the inventory based on the quantity given."""

        if name in INVENTORY: 
                if quantity<0:
                    print('Quantity cannot be negative. Try again! ')
                elif quantity==0:
                    print(f'You have not added any {name} in the cart')
                else:
                    available_quantity = INVENTORY[name][0]
                    if available_quantity != 0:

                        if quantity <= available_quantity:
                            quantity_to_be_added = quantity

                        elif quantity > available_quantity:
                            print('We have only',available_quantity,name,'so only this quantity will be added to your cart.')
                            quantity_to_be_added = available_quantity

                        article = Article(name,quantity_to_be_added,INVENTORY[name][1])
                        if name not in self.name_purchased:
                            article.setQuantity(quantity_to_be_added)
                            self.__list_of_purchased.append(article)
                            self.name_purchased.append(name)
                            INVENTORY[name][0] -= quantity_to_be_added

                        elif name in self.name_purchased:
                            for item in self.__list_of_purchased:
                                if item.getName() == name:
                                    quantity_in_cart = item.getQuantity()
                                    item.setQuantity(quantity_to_be_added + quantity_in_cart)
                                    INVENTORY[name][0] -= quantity_to_be_added

                    elif available_quantity == 0:
                        print('Sorry, we are out of stock of',name)
        
        else:
            print(name,'is currently not available in our inventory.')

    # A method used to remove item from the shopping cart
    def removeProduct(self, name, quantity): 
        """Removes items or only decreases the quantity of the item from the shopping cart based on the quantity given."""

        if name in self.name_purchased:
            if quantity<0:
                print('Quantity cannot be negative. Try again! ')
            else:
                for article in self.__list_of_purchased:
                    if article.getName() == name:
                        quantity_in_cart = article.getQuantity()
                        if quantity < quantity_in_cart:
                            article.setQuantity(quantity_in_cart-quantity)
                            print(f'You removed {quantity} items of {name} . Now you have {quantity_in_cart-quantity} {name} in your cart.')
                            INVENTORY[name][0] += quantity
                        elif quantity >= quantity_in_cart:
                            self.name_purchased.remove(name)
                            self.__list_of_purchased.remove(article)
                            print(f'You had only {quantity_in_cart} {name} .So all of {name} items are removed from your cart.')
                            INVENTORY[name][0] += quantity_in_cart
                        break
        else:
            print(f'You do not have {name} in your cart. ')
    

    def checkout(self):
        """Prints the items purchased and the total bill. And then removes the items from the shopping cart""" 
        if self.__list_of_purchased!=[]:
            print(f'You are buying {len(self.__list_of_purchased)} items.')
            total_price = 0
            for item in self.__list_of_purchased:
                name = item.getName()
                quantity = item.getQuantity()
                price = INVENTORY[name][1]
                print(f'{name}, {quantity}, {price}')
                if item.getQuantity() >= 3:
                    total_price += price* quantity * 0.10 * 1.07# Apply 10% discount and 7% VAT
                else:
                    total_price += price * quantity * 1.07
                
            self.__list_of_purchased = []
            self.name_purchased = []
            print('Total bill including VAT and discounts is: $'+str(total_price))
        
        else:
            print('You did not choose any item to buy. First add your item to the shopping cart.')
    
    def displayCart(self):
        """Prints the number of item in the shopping cart and prints each items"""
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

    print("_______________________________________________________")
    print("|\t                 MENU                          |")
    print("|______________________________________________________|")
    print("|\t1. List all of items, inventory and price      |")
    print("|\t2. List shopping cart items                    |")
    print("|\t3. Add an item to the shopping cart            |")
    print("|\t4. Remove an item from the shopping cart       |")
    print("|\t5. Checkout                                    |")
    print("|\t6. Exit                                        |")
    print("|______________________________________________________|")


def beautify():
    # To print a line of stars

     print('*'*100)


def main():
    """ This is our main function."""

    print('''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                \tWelcome  
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
    while True:
        file_path = input('Enter the path of your csv file: ')
        try:
            read_data(file_path)
            break
        except FileNotFoundError:
            print('File is not found! ')
            continue

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
            try:
                if name in INVENTORY:
                    quantity = input("Enter the quantity to add: ")
            
                    cart.addProduct(name, int(quantity))
                else:
                    print(name,'is currently not available in our inventory.')
            except ValueError:
                print('You entered a string value for quantity. It should be a positive integer. ')
            beautify()    
            
        elif choice == '4':
            name = input("Enter the name of the product to remove: ")
            try:
                if name in INVENTORY:
                    quantity = input("Enter the quantity to remove: ")
            
                    cart.removeProduct(name, int(quantity))
                else:
                    print(name,'is currently not available in our inventory.')
            except ValueError:
                print('You entered a string value for quantity. It should be a positive integer. ')
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
