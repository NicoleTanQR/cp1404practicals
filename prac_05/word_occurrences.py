"""
Word Occurrences
Estimate: 40 minutes
Actual:   98 minutes
"""

word_to_count = {}
words = input("Text: ").split()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
word_width = max((len(word) for word in word_to_count))
for word, count in sorted(word_to_count.items()):
    print(f"{word:{word_width}} : {count}")
