"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    if sales < 1000
        bonus_rate = 0.1
    else
        bonus_rate = 0.15
    bonus = sales * bonus_rate
    print bonus
    get sales
"""

BONUS_RATE_LOW = 0.1
BONUS_RATE_HIGH = 0.15
BONUS_RATE_HIGH_THRESHOLD = 1000

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_RATE_HIGH_THRESHOLD:
        bonus_rate = BONUS_RATE_LOW
    else:
        bonus_rate = BONUS_RATE_HIGH
    bonus = sales * bonus_rate
    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))
