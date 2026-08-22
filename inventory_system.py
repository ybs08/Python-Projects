import json


class Item:
    """Base class for anything stored in the inventory. Book and Electronics
    inherit from this and each add their own type-specific attributes."""

    def __init__(self, title, item_id, quantity):
        self.title = title
        self.item_id = item_id
        self.quantity = quantity


class Book(Item):
    def __init__(self, title, item_id, quantity, author, genre):
        super().__init__(title, item_id, quantity)
        self.kind = "Book"  # used to tell Book/Electronics apart when saving/loading
        self.author = author
        self.genre = genre

    def describe(self):
        return f"{self.title} by {self.author}. Its genre is {self.genre} with a quantity of {self.quantity}."


class Electronics(Item):
    def __init__(self, title, item_id, quantity, brand, warranty_years):
        super().__init__(title, item_id, quantity)
        self.kind = "Electronics"
        self.brand = brand
        self.warranty_years = warranty_years

    def describe(self):
        return f"{self.title} by the brand {self.brand}. It has a warranty of {self.warranty_years} years with a quantity of {self.quantity}"


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print(f"Item {item_id} has been removed.")
                return
        print(f"No item found with this ID {item_id}")

    def search(self, keyword):
        found = False
        for item in self.items:
            if keyword.lower() in item.title.lower():
                print(f"Item has been found! Its description: {item.describe()}")
                found = True
        if not found:
            print("No item has been found with this keyword")

    def list_all(self):
        for n, item in enumerate(self.items, start=1):
            print(f"Item {n}:", item.describe())

    def save(self, filename):
        # Book and Electronics need different fields saved, so each item is
        # converted to a dict based on its "kind" before being written out.
        data = []
        for item in self.items:
            if item.kind == "Book":
                data.append({
                    "Type": item.kind,
                    "Title": item.title,
                    "Author": item.author,
                    "Genre": item.genre,
                    "ID": item.item_id,
                    "Quantity": item.quantity
                })
            else:
                data.append({
                    "Type": item.kind,
                    "Title": item.title,
                    "Brand": item.brand,
                    "Warranty years": item.warranty_years,
                    "ID": item.item_id,
                    "Quantity": item.quantity
                })
        # "w" (not "a") since each save should fully represent the current
        # state of self.items, not append on top of a previous save.
        with open(filename, "w") as f:
            json.dump(data, f)

    def load(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                # Reset self.items before loading so items aren't duplicated
                # if load() is called more than once in the same run.
                self.items = []
                for loaded in data:
                    if loaded["Type"] == "Book":
                        item = Book(loaded["Title"], loaded["ID"], loaded["Quantity"], loaded["Author"], loaded["Genre"])
                    else:
                        item = Electronics(loaded["Title"], loaded["ID"], loaded["Quantity"], loaded["Brand"], loaded["Warranty years"])
                    self.items.append(item)
        except FileNotFoundError:
            print("File not saved yet.")


def main():
    tracker = Inventory()
    while True:
        print("Option 1: Add ")
        print("Option 2: Remove ")
        print("Option 3: Search ")
        print("Option 4: List all items ")
        print("Option 5: Save")
        print("Option 6: Load")
        print("Option 7: Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            item_id = input("ID: ")
            quantity = int(input("Quantity: "))
            kind = input("Type of item: ")
            if kind.lower() == "book":
                author = input("Author: ")
                genre = input("Genre: ")
                tracker.add_item(Book(title, item_id, quantity, author, genre))
            elif kind.lower() == "electronics":
                brand = input("Brand: ")
                warranty_years = int(input("Warranty years: "))
                tracker.add_item(Electronics(title, item_id, quantity, brand, warranty_years))
            else:
                print("Invalid item type to add.")
        elif choice == "2":
            item_id = input("ID for the item wanted to remove: ")
            tracker.remove_item(item_id)
        elif choice == "3":
            keyword = input("Keyword for the item wanted to remove: ")
            tracker.search(keyword)
        elif choice == "4":
            tracker.list_all()
        elif choice == "5":
            filename = input("Filename which you want to save: ")
            tracker.save(filename)
            print("Saved!")
        elif choice == "6":
            filename = input("Filename which you want to load: ")
            tracker.load(filename)
            print("Loaded!")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

