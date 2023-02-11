letter = '''Dear <|Name|>,
You are selected!

Date: <|DATE|>
'''
name= input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)