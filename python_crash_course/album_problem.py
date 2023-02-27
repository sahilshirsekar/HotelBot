def make_album(name, title, no_of_songs=None):
    if no_of_songs:
        album = {'artist_name':{name}, 'album_title':{title}, 'no_of_songs' : {no_of_songs}}
    else :
        album = {'artist_name':{name}, 'album_title':{title}}
    return album

# few function call
a = make_album('John killer','greed-speed')
print(a)
b = make_album('Grame itcher', '8 tea', 8)
print(b)
c = make_album('Daniel Brown', 'beast is sleeping')
print(c)

# creating user-definde album
while True:
    print("Tell your favourite artist's name and his album")
    print("(enter q to quit)")
    name = input("Enter his/her name: ")
    if name == 'q':
        break
    title = input("Enter his/her album name: ")
    if title == 'q':
        break

    user_album = make_album(name, title)
    print(user_album)


