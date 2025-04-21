#3. is_palindrome(s) – Return True if the string s is a palindrome.

# #easier method with time and space complexity = o(n)

# def is_palindrome(s):
#     return s == s[::-1]


# a = "abcdga"
# print(is_palindrome(a))



#lengthy method

def is_palindrome(s):
    a,b = 0, len(s)-1
    while a<b:
        if s[a] != s[b]:
            return False
        a +=1
        b -=1
    return True
        
a = "abccba"

print(is_palindrome(a))