#Moving Items from One List to Another
#check unconfrimed user list and move to confrimed user list.


unconfrimed_users = ['sam','david','john']
confrimed_users = []
while unconfrimed_users:
    current_user = unconfrimed_users.pop()
    print(f"Verified user: {current_user.title()}")
    confirmed_users = confrimed_users.append(current_user)
    #Display the confirmed users

print(f"This is the list of confirmed users: {confrimed_users}")
print(f"This is the list of unconfrimed users: {unconfrimed_users}")

for confirmed_user in confrimed_users:
    print(confirmed_user.title())