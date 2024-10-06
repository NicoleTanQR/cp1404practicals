"""
total_price = 0
get number_of_items
while number_of_items < 0
    print "Invalid number of items!"
    get number_of_items
for item in number_of_items
    get item_price
    total_price += item_price
if total_price > 100
    total_price *= 0.9
print number_of_items, total_price
"""

INVALID_INPUT_THRESHOLD = 0
DISCOUNT_THRESHOLD = 100
NEW_PRICE_RATE = 0.9
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < INVALID_INPUT_THRESHOLD:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for item in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > DISCOUNT_THRESHOLD:
    total_price *= NEW_PRICE_RATE
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
