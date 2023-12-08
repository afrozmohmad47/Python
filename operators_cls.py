# operator : A symbol which performs the operation between operands..

# Arthimetic Operators(+,-,*,/,//,%,**)
# Relational or Comparison Operators(==,!=,>,<,>=,<=)
# Logical Operators(and,or,not)
# Assignment Operators(=,+=,-=,*=......)
# Membership Operators(in,not in)
# Identity Operators(is, is not)
# Bitwise Operators(Bitwise AND(&),Bitwise OR(|),Bitwise XOR(^),Left shift(<<),Right Shift(>>),Bitwise NOT(~))
# Ternary Operator()


# Arthimetic Operators:

# /                //            %


# 17/3 - 5.6666667                   17//3 -5                         17%3 - 2

# 3)17(5.6666667                    3) 17 (5.66667                    3)17(5
#   15                                 15                               15
# -------                           ------------                      --------
#    20                                20                                2
#    18                                18
# ------                            ------------
#     2                                 2


# 3)167(55
#   15
# ---------
#    17
#    15
# ---------
#     2


# ** -- power

# print(3*4)

# print(3**4)


# Relational Operators()


# name = "Kishore" # THis will assign the value to name varibale..


# # print(name == 'kishore')  # We are checking whether name value and "kishore" is same or not

# # print(name != 'kishore')

# # a=21

# # print(a>30)

# print(name > 'kishore') # False..


# Logical Operators(and,or,not):


# BODMAS - 
# A        B        A and B       A or B         not(A)      not(A and B)      not((A or B) and (A and B))
# -----------------------------------------------------------------------------------------------------------
# T        F           F            T              F                T                      T 
# F        T           F            T              T                T                      T 
# T        T           T            T              F                F                      F 
# F        F           F            F              T                T                      T 

# username = "rajesh"
# password = "password"

# input() -- It will help you to gve the userinput at runtime..

# username1 = input("Enter your username:")

# password1 = input("Enter your password:")


# mobile = "8898398876"

# # print(username1 == username and password1==password)

# mobile1 = input("Enter your number:")

# # print((username1 == username and password1==password) or (mobile1 == mobile and password1==password))


# print((username1 == username or mobile1==mobile) and (password1==password))

# Assignment Operators(=,+=,-=,/=,*=):

# a=32  

# a+=5 # a=a+5

# print(a)

# a-=2
# print(a)

# a*=3
# print(a)

# Membership Operators(in,not in):

# str1 = "Python is a programming language."

# print('P' in str1)

# print('prog' in str1)

# print('s ap' in str1) # False

# print('s ap' not in str1) # True


list1 = ["7372873287","7382873232","8392893232","93728728732","7382382929","9327328233"]


# print("8392893232" in list1) # True

# print("839289323" in list1) # (False)complete value has to match not the subpart


tuple1 = ("7372873287","7382873232","8392893232","93728728732","7382382929","9327328233")

# print("8392893232" in tuple1) # True

# print("839289323" in tuple1) # (False)complete value has to match not the subpart


# address = {"H.no":301,"building-name":"lake view","Locality":"Madhapur","city":"Hyderabad","pincode":"500084"}


# print('city' in address)

# print('500084' in address)

# Identity Operators(is,is not):

# a=12

# print(a is 12)
# print(a == 12)


# name="ramesh"

# print(name is 'ramesh')
# print(name == 'ramesh')

# tuple1 = (1,2,3,4)

# print(id(tuple1))
# print(tuple1 is (1,2,3,4))

# print(id((1,2,3,4)))

# print(tuple1 == (1,2,3,4))

# list1 = [1,2,3,4]

# print(list1 is [1,2,3,4])  # it will check the memory allocation
# print(list1 == [1,2,3,4])

# print(id(list1))
# print(id([1,2,3,4]))

# print(list1 is not [1,2,3,4])