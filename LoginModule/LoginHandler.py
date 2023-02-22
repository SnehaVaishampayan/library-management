from Constants import authenticated_users


# This function is responsible for authenticating the logged in user.
def is_user_authenticated(login_data):
    print(login_data['username'])
    print(type(authenticated_users))
    if login_data['username'] in authenticated_users.keys():
        if authenticated_users[login_data['username']] == login_data['password']:
            return True
    return False
