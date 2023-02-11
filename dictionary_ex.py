# person = {
#     'first_name': 'sahil',
#     'last_name' : 'shirsekar',
#     'age' : 19,
#     'city':'virar',
# }
# for i,j in person.items():
#     print(str(i) + str(j))

favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'java',
    'phil' : 'python',
}
friends = ['phil','sarah']

for name in favourite_languages :
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
        " , I see your favourite language is " +
        str(favourite_languages[name].title()))

for language in set(favourite_languages.values()):
    print(language.title())