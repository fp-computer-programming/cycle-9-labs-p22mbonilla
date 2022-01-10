# Author MB 01/10/2022

def double_stuff(lst):
    for i, v in enumerate(lst):
        lst[i] = 2 * v
    return lst

print(double_stuff([1, 2, 3, 4]) == [2, 4, 6, 8])
print(double_stuff([1.1, 2, 3.14, 4]) == [2.2, 4, 6.28, 8])
print(double_stuff([1, "a", 2, "b"]) == [2, "aa", 4, "bb"])
