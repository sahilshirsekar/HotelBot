def build_profile(first, last, age ,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['age'] = age
    return user_info
 
user_profile = build_profile('albert', 'einstein', 25,  location = 'princeton', field = 'physics')
print(user_profile)