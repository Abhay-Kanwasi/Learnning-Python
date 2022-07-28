# # JSON - Java Script Object Notation


# # 1. JSON to Python

# import json

# people_string = '''
# {
#     "people" : [
#         {
#             "name" : "Abhay Kanwasi",
#             "phone" : "123-43-5-44",
#             "emails" : ["abhaykanwasi123@gmail.com","kanwasiabhay123@gmail.com"],
#             "has licensed" : false
#         },
#         {
#             "name" : "Parveen Rawat",
#             "phone" : "987-768-123",
#             "email" : "parveenrawat123@gmail.com",
#             "has licensed" : true
#          }
#     ]
# }
# '''

# data = json.loads(people_string) # Here we load our data 

# print(data) # Here we print our data

# for info in data["people"]:
#     print(info["name"])



# 2. Python to JSON

import json

people_string = '''
{
    "people" : [
        {
            "name" : "Abhay Kanwasi",
            "phone" : "123-43-5-44",
            "email" : ["abhaykanwasi123@gmail.com","kanwasiabhay123@gmail.com"],
            "has licensed" : false
        },
        {
            "name" : "Parveen Rawat",
            "phone" : "987-768-123",
            "email" : "parveenrawat123@gmail.com",
            "has licensed" : true
         }
    ]
}
'''
data = json.loads(people_string)

for info in data['people']:
    del info['email']

new_string = json.dumps(data)

# If you want that new_string will print as it be in the format of string
new_string = json.dumps(data,indent=2)
print(new_string)