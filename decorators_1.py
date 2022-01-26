# implement decorator that check user's 'is_admin' status
# if user is admin - function should return 200, else - 400


class User:
    def __init__(self, first_name: str, is_admin: bool):
        self.first_name = first_name
        self.is_admin = is_admin


def is_admin(func):
    def wrapper(user):
        if user.is_admin:
            return func(user)
        return 400
    return wrapper


@is_admin
def view(user: User):
    print(f'Request from user {user.first_name}')
    return 200


# this is tests
user_1 = User(first_name='John', is_admin=True)
user_2 = User(first_name='John', is_admin=False)

assert view(user_1) == 200
assert view(user_2) == 400

print('Success')
