#Word Frequency: Count frequency of each word in a sentence
import re

test_paragraph = '''The sun rose gently over the horizon, casting a warm golden glow across the landscape.
                    Birds chirped merrily, announcing the start of a new day. The trees, covered in morning dew,
                    swayed slightly in the cool breeze. A gentle stream ran through the meadow,
                    its clear waters sparkling in the sunlight. As the day progressed,
                    the vibrant colors of the flowers in the field began to stand out, 
                    creating a beautiful mosaic of nature\’s palette. The air smelled fresh, 
                    filled with the scent of pine and wildflowers, 
                    creating a perfect harmony between the earth and sky.'''

test_paragraph = test_paragraph.lower()
para_words = re.findall(r'\b\w+\b', test_paragraph)

counter = {}

for word in para_words:
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] += 1
print(counter)


#using counter
from collections import Counter
import re

# Input sentence
sentence = "Data, data! Innovation drives data."

# Convert sentence to lowercase and extract words
sentence = sentence.lower()
words = re.findall(r'\b\w+\b', sentence)

# Use Counter to count frequencies
freq = Counter(words)

# Print the word frequencies
print(freq)
