# # a = {}
# # print(type(a))
# # print(a)

# b = set()
# print(type(b))
# b.add(2)
# b.add((4,5,6))
# b.add(4)
# print(b)
# print(len(b))
# b.remove(2)
# print(b)

# print(b.pop())
# print(b.union({(4,5),11}))
# b= {1,8,2,3}
# print(b.intersection({8,11}))

myDict= {
    "pankha":"Fan",
    "dabba":"Box",
    "vastu":"Item"
}
list = myDict.keys()
print("Your options are ",list)
a = input("Enter the hindi word\n")
print("The english meaning of your word is",myDict.get(a))