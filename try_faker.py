from faker import Faker

faker = Faker()


def create_user(name: str, password: str):
    # print(faker.name())
    # Task 1. name(login), password
    if not name:
        name = faker.name()
    if not password:
        password = faker.password()

        def password_check(password):

            if len(password) < 8:
                print('Password must contain at least 8 characters')
                return False
            elif password.isalpha():
                print('Password must contain at least one non-alph character')
                return False
            elif password.isdigit():
                print('Password must contain at least 4 letters. ')
                return False
            for a in password:
                if a * 3 in password:
                    print('Password contains a consecutive character')
                    return False
            print('Password was accepted')
            return True
    print(f'User name is "{name}", password "{password}"')
    return name, password
