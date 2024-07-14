"""
Word Occurrences
Estimate: 10 minutes
Actual:   13 minutes
"""
word_in_text = {}
max_length = 0

text = input("Text: ")
words = text.split()
for word in words:
    if word in word_in_text:
        word_in_text[word] += 1
    else:
        word_in_text[word] = 1
    if len(word) > max_length:
        max_length = len(word)

sorted_word_in_text = {}
for word in sorted(word_in_text):
    sorted_word_in_text[word] = word_in_text[word]

for word in sorted_word_in_text:
    print(f"{word:{max_length}} : {sorted_word_in_text[word]}")
