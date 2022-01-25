# implement decorator that check user's 'is_admin' status
# if user is admin - function should return 200, else - 400


class User:
    def __init__(self, first_name: str, is_admin: bool):
        self.first_name = first_name
        self.is_admin = is_admin


def is_admin(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        # Have we got another way to take the user from function?
        response = 200 if args[0].is_admin else 400
        return response
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
