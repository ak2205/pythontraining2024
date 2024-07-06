#qn 4

a = [6, 7, 8, 9, 10]
b = [3, 4, 5, 6, 1]
c = dict(list(zip(a, b)))
print(c, "\n")

#qn 5

sampl_tuple = (5, 6, 7, 8, 1, 10, 1, 1, 2, 2, 11)
e = set(sampl_tuple)
f = tuple(e)
print(f, "\n")

#qn 6

h = (1, 2, 3, 4, 5, 6)
k = (5, 6, 7, 8, 9, 10)
o = set(h)
u = set(k)
t = o.symmetric_difference(u)
x = tuple(t)
print(x, "\n")

#qn 8

w = ["monday","sunday","wednesday","thursday","friday"]
q = w[4][::-1]
print(q, "\n")

#qn 9
#Convert below dictionary values into a set:

s_dict = {"1": "monday", "2": "Satday", "3": "wedday", "4": "sunday", "0": "tuesday", "5": "monday", "6": "wedday"}
r = s_dict.values()
j = set(r)
print(j, "\n")

#Question10:
#Concatenate keys and values of below dictionary in to a list and identify its length

w_dict = {"1": "mon", "2": "Sat", "3": "wed", "4": "sun", "0": "tues"}
q_yo = w_dict.keys()
print(q_yo, "\n")
y_qo = w_dict.values()
print(y_qo)
ert = list(q_yo) + list(y_qo)
print(ert)
print(len(ert))
