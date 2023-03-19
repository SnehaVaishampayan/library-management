from Constants import authenticated_users
from Constants import admin_list


# This function is responsible for authenticating the logged in user.
def is_user_authenticated(login_data):
    print(login_data['username'])
    print(type(authenticated_users))
    if login_data['username'] in authenticated_users.keys():
        if authenticated_users[login_data['username']] == login_data['password']:
            return True
    return False

# This function is responsible for checking if the logged in user is Admin
def is_user_admin(login_username):
    print("in is_user_admin")
    if login_username in admin_list:
        return True
    else:
        return False