# For given string 'Bamboozled', write a program to obtain the following output:

'''
1. B a
2. e d
3. e d
4. mboozled
5. mboozled
6. mboozled
7. Bamboo
8. Bamboo
9. Bamboo
10. delzoobmaB
11. Bamboozled
12. Bmoze
13. Bbzd
14. Boe
15. BamboozledHype!
16. BambooMonger!
'''

# Use multiple ways to get any of the above outputs

sentence = 'Bamboozled'
print("The sentence is : ", sentence)
print("\nOutput can be :")
print("1. B a\n2. e d\n3. e d\n4. mboozled\n5. mboozled\n6. mboozled\n7. Bamboo\n8. Bamboo\n9. Bamboo\n10. delzoobmaB\n11. Bamboozled\n12. Bmoze\n13. Bbzd\n14. Boe\n15. BamboozledHype!\n16. BambooMonger!")

do = int(input("Enter your desired output number: "))

if do == 1:
    # extract B a
    print(sentence[0],"",sentence[1])
    print("B a extracted\n")

elif do == 2:
    # extract e d
    print(sentence[-2],"",sentence[-1])

elif do == 3:
    # extract e d
    print(sentence[8],"",sentence[9])
    print("e d extracted\n")

elif do == 4 or do == 5 or do == 6:
    # extract mboozled
    print(sentence[2:])
    print(sentence[2:10])
    print(sentence[-8:])
    print("mboozled extracted\n")

elif do == 7 or do == 8 or do == 9:
    # extract Bamboo
    print(sentence[:6])
    print(sentence[0:6])
    print(sentence[-10:-4])
    print("Bamboo extracted\n")

elif do == 10:
    # Reverse Bamboo
    print(sentence[::-1])
    print(sentence[-1:-11:-1])
    print("Reverse Bamboo extracted\n")

elif do == 11:
    # Normal sentence at it is
    print(sentence)
    print(sentence[0:11:1])
    print("Bamboozled extracted\n")

elif do == 12:
    # extract Bmoze
    print(sentence[0:11:2])
    print(sentence[-11:-1:2])
    print("Bmoze extracted\n")

elif do == 13:
    # extract Bbzd
    print(sentence[0:11:3])
    print(sentence[-11::3])
    print("Bbzd extracted\n")

elif do == 14:
    # extract Boe
    print(sentence[0:11:4])
    print(sentence[-11::4])
    print("Boe extracted\n")

elif do == 15:
    # print BamboozledHype!
    phrase = "Hype!"
    print(sentence+phrase)
    print("BamboozledHype! printed\n")

elif do == 16:
    # print BambooMonger!
    phrase1 = "Monger"
    print(sentence[0:6]+phrase1)
    print("BambooMonger! printed\n")

else:
    print("Please enter the number according to what action want to performed on",sentence,"\nHint: Number must between 1 to 16")