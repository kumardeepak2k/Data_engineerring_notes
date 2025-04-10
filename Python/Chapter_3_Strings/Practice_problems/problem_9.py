
user_email = input("Enter your email id: ")

local_name, domain = user_email.split("@")

if len(local_name)>2:
    masked_local = local_name[0] + '*' *(len(local_name)-2) + local_name[-1]
else:
    masked_local = local_name

print(masked_local+'@'+domain)