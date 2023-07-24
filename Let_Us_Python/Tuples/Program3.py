# A list contains tuples containing roll no, names and ge of student. write a program to gather all the names from this list into another list.

lst = [('A101', 'Shubha', 23), ('A104', 'Nisha', 25), ('A111', 'Sudha', 24)]

new_lst = []

for ele in lst:
    new_lst += [ele[1]]

print(new_lst)