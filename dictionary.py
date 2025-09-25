""" You will be creating a little store in your terminal. You will have a list of
dictionaries that will be displayed to the user. Each Dictionary will have at
least 3 properties (name, price and whatever you want)
PART ONE:
The user will select one item to purchase. You will then show the user
ONLY the name of the item they purchased. You will need to use the item
index to accomplish this task.

PART TWO:
You will now make the app more complex by incorporating while loops and
a “cart”. Users will be shown the list of items and asked to purchase one.
Afterwards ask the user if they wish to continue. Once the user has decided
they are done shopping, print the names of the items purchased and the
total of the cart. """
freezer = {
    "name": "Refrigerator",
    "price": 1599.99,
    "description": "High capacity refrigerator",
}
tv = {
    "name": "TV",
    "price": 1859.99,
    "description": "Flat Screen TV",
}
laptop = {
    "name": "Laptop",
    "price": 1299.99,
    "description": "Lightweight, fast laptop"
}
confirm = "Not decided."
while confirm is not "yes" or "y" or "no" or "n":
    store_items = [freezer, tv, laptop]
    for index, item in enumerate(store_items):
        print(index, ":", item)

    purchase = input("What item do you want to buy? Input a number.")
    purchase = int(purchase)
    confirm = input(f"You selected a {store_items[purchase]["name"]}. Are you sure?")
    if confirm == "yes" or "y":
        print("Thank you for your purchase!")
    elif confirm == "no" or "n":
        print("Order canceled.")
    else:
        print("Not a valid input.")