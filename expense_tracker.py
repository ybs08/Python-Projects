#Make the class transaction with all its attributes

import json
class Transaction:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

#Now for the expense tracker class which will use the first class to work

class ExpenseTracker:
    def  __init__(self):
       self.transactions = []  
       
       #the list in which transactions will be stored
    
    def add_transaction(self, transaction):
       self.transactions.append(transaction)
       
       #each transaction here uses the Transaction class to store all its attributes
    
    def get_total(self):
        total = 0
        for transaction in self.transactions: #transaction here is used as a loop variable to loop over each item in the list
            total += transaction.amount       #then adding each amount of each transaction to the total until the transactions end
        return total
       
        #returning the total amount of the transactions 
    
    def get_total_by_category(self, category): #we add the category here to specify which category we want to find its total amount
        total = 0
        for transaction in self.transactions: 
            if transaction.category == category:  #if conditional to find the wanted category
                total += transaction.amount       #adding the amounts to the total
        return total
    
    def save_to_file(self, filename):  #function to save the saved transactions to a file as a list of dictionaries with a variable file name
        data = []                  
        for transaction in self.transactions:
            data.append({                           #adding each transaction in the transactions list to the data list as dictionaries
                "amount": transaction.amount,
                "category": transaction.category,
                "date": transaction.date,
                "description": transaction.description})
        with open(filename, "w") as f:    #opening the file with the wanted file name to add the data list
            json.dump(data, f)
    
    def load_from_file(self, filename):   #getting the values from the file again to return them to the transactions list again
        try:
            with open(filename, "r") as f:
                data = json.load(f)       #putting the data as the list in the file
            for item in data:             #looping over each item in the list in the file
                transaction = Transaction(item["amount"], item["category"], item["date"], item["description"])  #putting the transaction variable as each attribute of each item in the list which is in the file
                self.transactions.append(transaction) #then adding them to the transactions list
        except FileNotFoundError:
            print("No saved file found yet - starting fresh") #message if there is no file saved yet
def main():
    tracker = ExpenseTracker()
    while True: 
        print("\n --- Expense Tracker ---")
        print("Option 1: Add")
        print("Option 2: View Total")
        print("Option 3: View by category")
        print("Option 4: Save")
        print("Option 5: Load")
        print("Option 6: Quit")
    
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            date = input("Date: ")
            description = input("Description: ")
            transaction = Transaction(amount, category, date, description)
            tracker.add_transaction(transaction)
        
        elif choice == "2":
            print("Total:", tracker.get_total())
        
        elif choice == "3":
            category = input("Wanted category: ")
            print("Total by category:", tracker.get_total_by_category(category) )

        elif choice == "4":
            filename = input("Insert file name: ")
            tracker.save_to_file(filename)
        elif choice == "5":
            filename = input("Insert file name: ")
            tracker.load_from_file(filename)
            print("Loaded")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()
            



     

