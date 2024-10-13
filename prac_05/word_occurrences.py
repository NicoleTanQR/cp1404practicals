"""
Word Occurrences
Estimate: 40 minutes
Actual:    minutes
"""

dictionary = {}
text = input("Text: ").split()
for word in text:
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
for word, count in dictionary.items():
    print(f"{word} : {count}")
