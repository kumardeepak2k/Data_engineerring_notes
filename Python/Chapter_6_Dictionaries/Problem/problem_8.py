#Group Words by Length: Given a list of words, group them by their lengths using a dictionary.

words = ["apple", "banana", "kiwi", "pear", "cherry", "fig"]

list = {}

for word in words:
    word_length = len(word)
    if word_length in list:
        list[word_length].append(word)
    else:
        list[word_length] = [word]

print(list)