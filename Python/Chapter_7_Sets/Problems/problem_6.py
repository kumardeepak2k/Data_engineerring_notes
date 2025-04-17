# Write functions to check if one set is a subset or superset of another, using logical conditions only.
 
def subset(set_a,set_b):
    for item in set_a:
        if item not in set_b:
            return(False)    
    return(True)

a = {1,2,3,4,5}
b = {3,4}

print(subset(b,a))