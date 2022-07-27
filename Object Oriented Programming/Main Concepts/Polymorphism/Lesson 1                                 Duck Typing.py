# Concept :- Before understanding the concept. Let's see the theorey.

"""
Theory :- A bird which is walking like a duck, which is quacking like a duck and which is swimming like a duck. That's bird is a duck.

Moral of the story :- It doesn't matter whether it is a duck or not what matters is the behaviour of that bird, if it is matching with a duck that's a duck..
"""

# Let's see example to understand how this concept applied..

class VsCode:

    def execute(self):
        print("Compiling")
        print("Running")

class Laptop:

    def code(self,ide): # Here ide doesn't have any type of it so we create a class for it(VsCode)
        ide.execute()   # Inside that ide create an execute function.

ide = VsCode()
lap1 = Laptop()

lap1.code(ide)




#........COMMING SOON