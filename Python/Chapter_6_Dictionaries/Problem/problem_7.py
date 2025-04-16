#7.	Find Key with Max Value: Return the key with the maximum value.

my_dict = {'a': 10, 'b': 30, 'c': 20}

# #using sort function
# sorted_list = sorted(my_dict.items(), key= lambda x: x[1], reverse= True)
# print(f"Key with max value is {sorted_list[0][0]}")

#using for loop
max_key = None
max_value = float('-inf')
for key,value in my_dict.items():
    if value > max_value:
        max_value = value
        max_key =  key
print(f'Key for max value is {max_key}')


