#Python offers hash() method to encode the data into unrecognisable value.

# # Python 3 code to demonstrate 
# # working of hash()
# # initializing objects
# int_val = 5
# str_val = 'Fasilkom UNEJ'
# flt_val = 24.56
  
# # Printing the hash values.
# # Notice Integer value doesn't change
# # You'l have answer later in article.
# print ("The integer hash value is : " + str(hash(int_val)))
# print ("The string hash value is : " + str(hash(str_val)))
# print ("The float hash value is : " + str(hash(flt_val)))

# Python 3 code to demonstrate 
# property of hash()
  
# initializing objects
# tuple are immutable
tuple_val = (1, 2, 3, 4, 5)
  
# list are mutable
list_val = [1, 2, 3, 4, 5]
  
# Printing the hash values.
# Notice exception when trying
# to convert mutable object
print ("The tuple hash value is : " + str(hash(tuple_val)))
# print ("The list hash value is : " + str(hash(list_val)))

# class Person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name

#     def __eq__(self, other):
#         return self.age == other.age and self.name == other.name

#     def __hash__(self):
#         print('The hash is:')
#         return hash((self.age, self.name))

# person = Person(20, 'Budi')
# print(hash(person))