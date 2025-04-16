#Check Membership
# Write a program to check whether a given element exists in a set.

a = {2,45,34435,34,35,'rggr',33.343}

b =2

#my logic
Keep_running = False
for char in a:
    if b == char:
        Keep_running = True
        break
if Keep_running:
    print("Exist")
else:
    print("Does not exist")

#effficient way
if b in a:
    print("We found it")
else:
    print("No")