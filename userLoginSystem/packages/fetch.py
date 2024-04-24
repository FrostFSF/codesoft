userTemplate = {"username": "", "password": ""}

def user(username, password):
    thisUser = userTemplate
    thisUser["username"] = str(username)
    thisUser["password"] = str(password)

    return userTemplate