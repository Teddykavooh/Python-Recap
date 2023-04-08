#The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
			if user not in user_groups:
				user_groups[user] = [group]
			else:
				user_groups[user] += [group]
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

'''dict.update Method'''
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)

my_string = "123456"
print(my_string)
print(type(int(my_string)))

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

z = [x for x in range(0, 102) if x % 3 == 0]
print(z)