"""
Word Occurrences
Estimate: 40 minutes
Actual:   98 minutes
"""

word_to_count = {}
words = input("Text: ").split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1
word_width = max((len(word) for word in word_to_count))
for word, count in sorted(word_to_count.items()):
    print(f"{word:{word_width}} : {count}")
