# Union 

engineers = {'Abhay', 'Ayush', 'Ravi', 'Dinesh'}
managers = {'Aditya','Ravi'}

print(f'Union of {engineers} and {managers} is : {engineers | managers}\n')

print(f'Intersection of {engineers} and {managers} is {engineers & managers}\n')

print(f'Diffrence- Engineers who are not managers are : {engineers - managers}\n')

print(f'Difference- managers who are not engineers are : {managers - engineers}\n')

print(f'Symmetic difference - managers who are not engineers and engineers who are not managers are {managers ^ engineers}')