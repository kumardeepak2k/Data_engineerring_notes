#Count Even and Odd: Count the number of even and odd numbers in a list.

a = [2,4,5,235,23245,57547,43534,325364,4363476,363,63,34]
even_count = 0
odd_count = 0


for num in a:
    if num % 2 == 0:
        even_count +=1
    else:
        odd_count += 1
print(f"Even - {even_count}, Odd - {odd_count}")


#using list comprehenesion

even_co = len([num for num in a if num%2==0])
odd_co = len([num for num in a if num%2!=0])
print (even_co, odd_co)