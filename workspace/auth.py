"""
用户认证模块
"""


def login(username: str, password: str) -> bool:
    """
    模拟登录
    """

    if username == "admin" and password == "123456":
        return True

    return False


def authenticated(user: dict) -> bool:
    """
    判断用户是否已经登录
    """

    return user.get("logged_in", False)


def current_user():

    return {
        "username": "admin",
        "logged_in": True
    }