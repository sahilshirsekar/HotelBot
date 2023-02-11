# user = input("Enter your username\n")
# a =  len(user)

# if (a < 10):
#     print("Username should contain more than 10 characters")
# else:
#     print("Valid username")

# a = ["harry","shubham","rohit","shipra","sahil"]
# name = input("Enter the name\n")
# if (name in a):
#     print("Yes")
# else:
#     print("No")

# marks = int(input("Enter the marks\n"))

# if marks>90:
#     grade = "O"
# elif marks>=80:
#     grade = "A"
# elif marks>= 70:
#     grade = "B"
# elif marks >= 60:
#     grade = "C"
# elif marks >= 50 :
#     grade = "D"
# else:
#     grade ="F"

# print(grade)

# fruits = ['mango','kiwi','litchi']
# for i in fruits :
#     if i == 'kiwi':
#         print("Sorry, we are out of kiwi")
#     else:
#         print("Adding " + i + ".")
    

# requested_toppings = ['mushrooms','olives','green peppers','pepperoni',
#                         'pineapple','extra cheese']
# available_toppings = ['mushrooms','french fries','extra cheese']

# for requested_topping in requested_toppings :
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else : 
#         print("Sorry, we don't have " + requested_topping)

# current_names = ['Atharva3','SSS','Tejal24','Neymar','Parthtsec']
# new_users = ['Umangy','SSS','Neymar','Hyde','Aspiressss']

# for i in new_users :
#     if i in current_names :
#         print("PLease, enter a new username.")
#     else:
#         print("Username is available")

list = [1,2,3,4,5,6,7,8,9]
for i in list:
    if i == 1:
        print(str(i) + "st")
    elif i == 2:
        print(str(i) + "nd")
    elif i == 3:
        print(str(i) + "rd")
    elif i == 4:
        print(str(i) + "th")
    elif i == 5:
        print(str(i) + "th")
    elif i == 6:
        print(str(i) + "th")
    elif i == 7:
        print(str(i) + "th")
    elif i == 8:
        print(str(i) + "th")
    else:
        print(str(i) + "th")
        