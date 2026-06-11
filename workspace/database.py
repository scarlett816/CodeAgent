"""
模拟数据库
"""

users = [

    {
        "username": "admin",
        "password": "123456"
    },

    {
        "username": "guest",
        "password": "guest"
    }

]


def get_user(username):

    for user in users:

        if user["username"] == username:

            return user

    return None


def verify_password(username, password):

    user = get_user(username)

    if user is None:

        return False

    return user["password"] == password