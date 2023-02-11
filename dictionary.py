# myDict = {
#     "fast": "In a quick manner",
#     "sahil": "Amateur Coder",
#     "marks": [1,2,3],
#     "anotherdict":{'Sahil':'Football fan'} ,
#     1:2
# }
# # print(list(myDict.keys()))
# # print(list(myDict.values()))
# # print(list(myDict.items()))
# # print(myDict)
# updateDict = {
#     "Lavesh":"Peon",
#     "Shubham":"Peon",
#     "Divya":"Peon",
#     "sahil":"Professional Coder"
# }
# # myDict.update(updateDict)
# # print(myDict)


# print(myDict.get("sahil"))
# print(myDict["sahil"])

# Alien game!!

alien_0 = { 'color':'green','points': 5}
# # print(alien_0['color'])
# print(alien_0['points'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'red'
print('The alien color now is ' + alien_0['color'])
alien_0 = {'x_position' : 0,'y_position': 25, 'speed': 'medium'}
print('Original x_position: ' + str(alien_0['x_position']))

#Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else :
    x_increment = 3

# The position is the old position plus the i crement.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# delete a key-value pair(s)
alien_0['points'] = 5
print(alien_0)

del alien_0['points']
print(alien_0)