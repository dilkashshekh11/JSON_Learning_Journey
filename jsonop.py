import json # import json library to convert json object
print("This is python json operations")

jsonUser = """ 
                {
                    "name" : "Dilkash",
                    "phone" : "9812345678",
                    "skills" : ["java","Python"],

                    "address" : {
                        "city" : "janakpur",
                        "pincode" : 2354
                                }
                } """

# print(jsonUser)
print(type(jsonUser))

# convert json object to python dictionary
userDict = json.loads(jsonUser)            # loads: convert json -> dictionary
print(userDict)
print(type(userDict))

# Acess values
print(userDict['name'])
print(userDict['phone'])
print(userDict['skills'])
print(userDict['address']['city'])
print(userDict['address']['pincode'])

todo = {
    'title' : "learn python core for ai",
    "isCompleted" : True 
    }

jsonTodo = json.dumps(todo)   # dumps:  convert dictionary -> JSON
print(jsonTodo)
print(type(jsonTodo))