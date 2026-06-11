from auth import login
from database import get_user


def main():

    username = "admin"

    password = "123456"

    success = login(
        username,
        password
    )

    if success:

        print("登录成功")

        user = get_user(username)

        print(user)

    else:

        print("登录失败")


if __name__ == "__main__":

    main()