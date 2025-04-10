#Find the Longest Word: From a sentence, print the longest word.
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

longest_word = max(para_words, key = len)
print(longest_word, len(longest_word))