"""Data Structure: create a notebook where you'll use and explore tuples, lists and dictionaries. Make sure to be able to manipulate nested data structures (retrieve a list item in a dictionary in a list for example, like a JSON object). Deadline: November 22, 3:30PM  """


#Tuples are immutable ,can store multiple data types
my_tuple = (12,4,8,4,9,(3,45),'dog',(7,9,6))
#to print an element 
print(my_tuple[0])
print(type(my_tuple))
print(len(my_tuple))
print(my_tuple[5][1])
print(my_tuple[7])
print(my_tuple[6])
# #iterating
for tuple in my_tuple:
    print(tuple)
slice_tuple =my_tuple[0:3]
print(f"slice tuple is: {slice_tuple}")
# #to check if an element is existed
print("check  4 if it exist in my tuple", 4 in my_tuple)

# example two
example_2=(1,2,(3,4),(12,(15,7)))
# to print 15 
print(example_2[3][1][0])

try:
    # I am trying to replace 15 by 19
    example_2[3][1][0]=19
except TypeError as e:
    print("the error is ", e)
    print("you can't modifiy tuples")

#to modify change to list first
list_tuple = list(my_tuple)
print(f"mynew list tuple is:{list_tuple}")
list_tuple.append(300)
print(f"new item is added:{list_tuple}")
list_tuple.remove(300)
print(f"new item is removed:{list_tuple}")


# #Lists are mutable,store d/t data types and allow modifications
my_lists = ["apple", "banana", "avocado", "orange","chili",['cat','cow','dog']]
print(my_lists[2])
print(len(my_lists))
my_lists.append("onion")
print(my_lists)
my_lists.insert(1,"tomato")
print(my_lists)
my_lists.remove("chili")
print(my_lists)
# #iterating over a list
for list in my_lists:
    print(list)
# my_lists.sort()  #but not supported between list and str
# my_lists.sort(reverse=True)
# #to copy
my_new_list = my_lists.copy()
print(f"copy list is:{my_new_list}")


# #Dictionaries(key:value) - json object
my_dict = {
            "name": "Jhon",
            "last_name": "Abrham",
            "age": 30,
            "email": "Jhonabrham12@gmail.com",
            "isStudent": True,
            "address":{
                        "street": "winkelstreet",
                        "city": "Brussels"
                            },
            "phoneNumbers": ["+32-042-222-40-40", "+32-046-555-7080"]
              }

print(f"my dictionary is:{my_dict}")
# #to print key:value
for key, value in my_dict.items():
    print(f"key: {key}, Value: {value}")
# #to delete
my_dict.pop("age")
print(my_dict)
# to print key
print(my_dict["name"])
# #adding new key
my_dict["date"] = "01/02/95"
print(my_dict["date"])
my_dict["age"] = 20
for value in my_dict:
    print(value)
print(my_dict["address"]["city"])
print(my_dict["phoneNumbers"][0])


# #more nested 

my_nested = [
    {
        "name": "jhon",
        "last_name": "Abrham",
        "age": 30,
        "email": "jhonabrham12@gmail.com", 
        "address": {"city": "Brusseles", "street": "winkelstraat"}, "phoneNumber": "+32-044-222-40-40"
    },
    {
        "name": "Rich",
        "last_name": "Daniel",
        "age": 24,
        "email": "richdaniel@gmail.com", 
        "address": {"city": "Ghent", "street": "Abeelstreet"}, "phoneNumber": ["+32-044-333-40-40", "+32-033-443-22-44"]
    },
    {
        "name": "Mike",
        "last_name": "Dave",
        "age": 40,
        "email": "mikedave33@gmail.com", 
        "address": {"city": "Hasselt", "street": "houthalenstreet"}, "phoneNumber": "+32-046-222-40-30" }
]
print(my_nested)
print(my_nested[0]["name"])
print(my_nested[1])
