# Demonstrate how to create simple and multi-line strings and whether a string can change after creation.

print("Simple and Multiline Strings")
print("\n")

msg1 = "Hello"
print(f"Simple string : {msg1}")
print("\n")

msg2 = "What is this life if full of care..\We have no time to stand and stare"
print(msg2)
print("\n")

msg3 = """What is this life if full of care...
We have no time to stand and stare"""
print(msg3)
print("\n")

# Concatenate these two lines
msg4 = {'What is this life if full of care..'
        'We have no time to stand and stare'}
print(msg4)
print("\n")


# Replica during printing
msg5 = 'MacLearn!!'
print(msg5*3)
print("\n")

# concatenation using '+' operator
msg6 = 'Utopia'
msg7 = 'Today!!'
msg8 = msg6 + msg7
print(f'Concatenate {msg6} and {msg7} is {msg8}')