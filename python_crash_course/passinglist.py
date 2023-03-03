def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'tye', 'marget']
greet_users(usernames)