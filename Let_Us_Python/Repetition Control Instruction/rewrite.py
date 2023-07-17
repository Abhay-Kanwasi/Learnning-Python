# Rewrite this program using for loop

# i = 0
# while i<len(lst):
#     if i>3:
#         break
#     else:
#         print(i,lst[i],s[i])
#         i += 1



lst = ['desert','dessert','to','too','lose','loose']
s = 'Mumbai'
for i in range(len(lst)):
    if i>3:
        break
    else:
        print(i, lst[i], s[i])
    

