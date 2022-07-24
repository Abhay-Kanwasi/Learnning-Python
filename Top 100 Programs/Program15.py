# How  to count vowels in a string.

a = "AbhayKanwasi"

count = 0

b = a.lower()
print(b)

vowel = ['a','e','i','o','u']
for i in b:
    if i in vowel:
        count+=1
print("The vowels in given string :",count)


