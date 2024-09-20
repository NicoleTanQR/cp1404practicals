"""
CP1404/CP5632 - Practical
Broken program to determine score status

get score
if score < 0 or score > 100
    print "Invalid score"
else if score >= 90
    print "Excellent"
else if score >= 50
    print "Passable"
else
    print "Bad"
"""

MINIMUM_THRESHOLD = 0
MAXIMUM_THRESHOLD = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50

score = float(input("Enter score: "))
if score < MINIMUM_THRESHOLD or score > MAXIMUM_THRESHOLD:
    print("Invalid score")
elif score >= EXCELLENT_THRESHOLD:
    print("Excellent")
elif score >= PASSABLE_THRESHOLD:
    print("Passable")
else:
    print("Bad")
