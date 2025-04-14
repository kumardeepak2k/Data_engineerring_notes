#swap keys and values 

info = {'Name': 'Deepak',
        'Age': 24,
        'City': 'Cuttack',
        'Gender': 'Male'
}
swapped = {}
swapped = {value:key for key,value in info.items()}
print(swapped)


for key,value in info.items():
    swapped[value] = key

print(swapped)