# make an argument optional
def get_formatted_name(f_name, l_name, m_name=''):
    if m_name :
        full_name = f"{f_name} {m_name} {l_name}"
    else :
        full_name = f"{f_name} {l_name}"
    return full_name.title()

musician = get_formatted_name('om','pathak')
# print(musician)

musician = get_formatted_name('om', 'pathak', 'xyz',)
# print(musician)

# return a dictionary 
def build_person(f_name, l_name, age=None):
    person = {'first':f_name, 'last':l_name}
    if age:
        person['age']= age
    return person 

musician = build_person('Sahil', 'Shirsekar', 19)
# print(musician)

while True:
    print("\nPlease tell your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")