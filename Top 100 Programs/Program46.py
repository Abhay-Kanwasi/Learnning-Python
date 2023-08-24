# Reverse a number in python

class Reverse_Number:
    def using_string(number):
        convert_to_string_number = str(number)
        reverse_number = convert_to_string_number[::-1]
        return reverse_number

    def using_maths(number):
        remainder = 0
        while number > 0:
            last_digit = number % 10 
            remainder = remainder * 10 +  last_digit   
            number = number // 10
        return remainder

    # We can't use recursion inside class so we use @staticmethod
    @staticmethod
    def using_recursion(number):
        def reverse_helper(number, reversed_num=0):
            if number == 0:
                return reversed_num
            else:
                last_digit = number % 10
                reversed_num = reversed_num * 10 + last_digit
                return reverse_helper(number // 10, reversed_num)
        
        return reverse_helper(number)


print(Reverse_Number.using_recursion(123))
print(Reverse_Number.using_string(123))
print(Reverse_Number.using_maths(123))

