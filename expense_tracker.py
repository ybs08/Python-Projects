import json


class Transaction:
    """Stores the details of a single expense entry."""

    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description


class ExpenseTracker:
    """Holds a list of Transactions and provides ways to total, save, and
    reload them."""

    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_total(self):
        total = 0
        for transaction in self.transactions:
            total += transaction.amount
        return total

    def get_total_by_category(self, category):
        total = 0
        for transaction in self.transactions:
            if transaction.category == category:
                total += transaction.amount
        return total

    def save_to_file(self, filename):
        # Convert each Transaction object into a plain dict first, since
        # json.dump() can only write basic types (dicts, lists, strings,
        # numbers) - not custom objects.
        data = []
        for transaction in self.transactions:
            data.append({
                "amount": transaction.amount,
                "category": transaction.category,
                "date": transaction.date,
                "description": transaction.description
            })
        # "w" so each save fully represents the current transaction list,
        # rather than appending on top of a previous save.
        with open(filename, "w") as f:
            json.dump(data, f)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            # Rebuild each dict back into a real Transaction object.
            for item in data:
                transaction = Transaction(item["amount"], item["category"], item["date"], item["description"])
                self.transactions.append(transaction)
        except FileNotFoundError:
            print("No saved file found yet - starting fresh")


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
            tracker.add_transaction(Transaction(amount, category, date, description))

        elif choice == "2":
            print("Total:", tracker.get_total())

        elif choice == "3":
            category = input("Wanted category: ")
            print("Total by category:", tracker.get_total_by_category(category))

        elif choice == "4":
            filename = input("Insert file name: ")
            tracker.save_to_file(filename)
            print("Saved!")

        elif choice == "5":
            filename = input("Insert file name: ")
            tracker.load_from_file(filename)
            print("Loaded")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
            



     

