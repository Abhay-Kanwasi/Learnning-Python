# Write a program to display the words that are repeated more than or equal to N times in the text which is case-sensitive. (N will be the user entered value). 

paragraph = input("Write a short paragraph : \n")
n = int(input("Enter the limit for duplicate words you can allowed in a text : "))

new = paragraph.split(" ")

counts = dict()

for word in new:
    if word in counts:
        counts[word]+=1