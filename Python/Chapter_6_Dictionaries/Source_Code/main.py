#Dictionary methods

# dict.get(key) vs dict[key]

data = {'name': 'Deepak', 'age': 24}
print(data['age'])     # 24
# print(data['gender'])  # ❌ KeyError
print(data.get('age'))     # 24
print(data.get('gender'))  # None
print(data.get('gender', 'Not Specified'))  # 'Not Specified'

#modifying dictionary

data["gender"] = "Female"
data.update({"gender": "Male"})
print(data)

#using dictionary unpacking

new_data = {**data, 'hobby': 'Cricket', 'city': 'Bhubaneswar'}
print(new_data)

#Removing Elements
data ={'name': 'Deepak', 'age': 24, 'Gender': 'Male', 'City':'Cuttack'}
print(data.pop('age'))

#last item
print(data.popitem())
print(data)

#del
del data['Gender']
print(data)

#clear
data.clear()
print(data)

#Dict Methods

#keys
data = {'name': 'Deepak', 'age': 24}
print(data.keys())  # dict_keys(['name', 'age'])
print(data.values())
print(data.items())

#🔹 setdefault(key, default)
# Returns the value of the key if it exists. If not, inserts the key with the given default and returns that.

data.setdefault('location', 'Odisha')
print(data)   # {'name': 'Deepak', 'age': 24, 'location': 'Odisha'}

#duplicating dict
copy_data = data.copy()
print(copy_data)

#from keys
players = ['Alice', 'Bob', 'Charlie']
scores = dict.fromkeys(players, 0)  # Initialize all players' scores to 0

print(scores)  # {'Alice': 0, 'Bob': 0, 'Charlie': 0}



