# we can not change the value in tuple, tuple is immutable 
# use case [list]: when values are needed to be changed in future : use list
# use case (tuple): when value are not needed to be changed in future: use tuple

"""t = (12, -2, "dj",2,2,2,2,2, "uao2", 54)
print(t)
index = t.index("dj")
print(index)
count = t.count(2)
print(count)
# tuple unpacking"""
"""a = (1)
print(type(a))  # this will give "int type"

b = (1,)
print(type(b))"""   # because of the ',' afte 1, will give you "class tuple"
# here is the tuple unpacking:
a, b = (32, 23)
print(a)
print(b)