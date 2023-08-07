# A filter operation applies a function to all the elements of a sequence. A sequence of those elements for which the function returns True.

# sequence = [2,4,4,6,6,5]
# filtered_sequence = list(filter(lambda x : x%2==0, sequence))
# print(filtered_sequence)


# Question 1 : Checking whether each element in a list is an alphabet and returning a list of alphabets.

sequence_for_question1 = ['2','a','g']
filtered_sequence = list(filter(str.isalpha, sequence_for_question1))
print(filtered_sequence)