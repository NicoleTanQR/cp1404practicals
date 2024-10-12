"""Practical 3 - Random Numbers"""

# For print(random.randint(5, 20))
# Saw 20, 5, and 18 on the console
# Smallest I could have seen is 5, largest 20

# For print(random.randrange(3, 10, 2))
# Saw 3, 7, and 9 on the console
# Smallest I could have seen is 3, largest 9
# Could not have produced a 4

# For print(random.uniform(2.5, 5.5))
# Saw 3.5888765550500317, 3.525665531414343, and 4.808999839365551 on
# the console
# Smallest I could have seen is 2.5, largest 5.5 or a number less than
# and closest to 5.5 depending on rounding

from random import randint

print(randint(1, 100))
