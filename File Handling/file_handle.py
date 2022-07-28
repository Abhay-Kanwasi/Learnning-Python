# # Now first we created a file name Demo.txt 

# # Now we want to read the data in Demo.txt then how we can do it ?

# # First we open the file

f = open("Demo.txt",'r')
# # print(f.read())

# # As you can see the output we got all the content available in Demo.txt

# # Now what if if want to read only one line from Demo.txt
# print(f.readline(),end="") # It will print the next line. Output : My name is Abhay Kanwasi
# print(f.readline()) # It will print the next line. Output : This is the series of Learning Python in Github. 


# # Now if you want to create a file like Demo.txt from here...

# new = open('New Fil.txt','w')
# #new.write("Something")

# # Now if we again try to write something we lost our previous data..
# new.write("!fdfksj")

# # So if we don't want to lose the data we have to append it..
# new = open("New Fil.txt",'w')
# new.write("Abhay is a good boy")


# # Now we have 2 files so I want to copy all the data from Demo.txt and save it into New Fil.txt

# for data in f:
#     new.write(data)

# # So it will print all the data.

