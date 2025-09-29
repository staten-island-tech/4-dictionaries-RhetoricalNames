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
store_items = [{
    "name": "Refrigerator",
    "price": 1599.99,
    "description": "High capacity refrigerator",}
,{
    "name": "TV",
    "price": 1859.99,
    "description": "Flat Screen TV",}
,{
    "name": "Laptop",
    "price": 1299.99,
    "description": "Lightweight, fast laptop"}]
checkout = "Not confirmed"
confirm = "Not decided."
total = 0
cart = []
while checkout is not "y" or checkout is not "yes":
    for index, item in enumerate(store_items, start = 1):
        print(index, ":", item)
    print(f"{len(store_items) + 1} : View Cart")
    print(f"{len(store_items) + 2} : Check out items")
    choice = input("What do you want to do? Input a number.")
    choice = int(choice)
    if choice == len(store_items) + 1:
        print(cart)
    elif choice == len(store_items) + 2 and (len(cart) > 0):
        print(f"Items: {cart}. Total: {total}")
        checkout = input("Are you ready to check out your items?")
        print(checkout)
        if checkout == "no" or checkout == "n":
            print("Purchases canceled.")
            quit()
    else:
        choice = int(choice)
        choice = choice - 1
        confirm = input(f"You selected a {store_items[choice]["name"]}. Are you sure?")
        if confirm == "yes" or confirm == "y":
            print("Item added to cart.")
            cart.append(store_items[choice]["name"])
            total = (total + store_items[choice]["price"])
        elif confirm == "no" or confirm == "n":
            print("Item not added to cart.")
        else:
            print("Invalid input. Please try again.")
print("Thank you for shopping here!")