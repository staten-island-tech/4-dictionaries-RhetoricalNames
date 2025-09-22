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
toilet_paper = {
    "name": "Ultra-Soft toilet paper",
    "price": 15.29,
    "department": "Hygiene",
}
tv = {
    "name": "tv",
    "price": 515.29,
    "department": "entertainment",
}
store_items = [toilet_paper[name], tv]
print(store_items)