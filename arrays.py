import array as arr

a = arr.array('i',[1,2,3])
print("The new array created is :", end=" ")
for i in range(3):
    print(a[i],end=" ")
print()

b = arr.array('d',[2.3,3.6,4.5])
print("The new created array is :", end=" ")
for i in range(3):
    print(b[i], end=" ")