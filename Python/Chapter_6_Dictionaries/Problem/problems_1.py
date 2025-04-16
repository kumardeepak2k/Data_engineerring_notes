#Create and Print Dictionary: Create a dictionary and print all key-value pairs.

info = {'Name': 'Deepak',
        'Age': 24,
        'City': 'Cuttack',
        'Gender': 'Male'
}
print('Full Dictionary')
for key,value in info.items():
    print(f"{key}: {value}")