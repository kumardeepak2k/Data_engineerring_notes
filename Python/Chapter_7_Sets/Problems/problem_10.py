#Given a list of integers, use only sets (not another list or dict) to detect if any duplicate exists.

a = [111,111,2,2,2,33,4,4,5,5,6,6,4,4,33]
set_a = set(a)

if len(a) == len(set_a):
    print(False)
else:
    print(True)