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