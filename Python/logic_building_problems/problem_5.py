#5. remove_duplicates(lst) – Return list with duplicates removed.


#easy method but it will not maintain the order as sets are unordered

# def remove_duplicates(lst):
#     new_lst = set(lst)
#     return list(new_lst)


# a = [222,222,55,44,222,44,55,44,55555,34242,2342342,43,43,434,34,43]

# print(remove_duplicates(a))


#efficient method

def remove_duplicates(lst):
    new_lst = []
    for char in lst:
        if char not in new_lst:
            new_lst.append(char)
    return new_lst

a = [222,222,55,44,222,44,55,44,55555,34242,2342342,43,43,434,34,43]
s = remove_duplicates(a)
print(s)


