#6. count_vowels(s) – Count and return the number of vowels in the string.

def count_vowels(s):
    vowel_lst = ['a','e','i','o','u','A','E','I','O','U']
    count = 0
    for char in s:
        if char in vowel_lst:
            count +=1
    return count


a = "abdgjakglipoutwetnslg"
print(count_vowels(a))