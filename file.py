#use open function to read the content of the file
f = open('sample.txt','r')  #reading mode
# data = f.read()
data = f.readline()
print(data)
data = f.readline()
# data = f.read(5) # reads the file characters of the file 
print(data)
f.close()