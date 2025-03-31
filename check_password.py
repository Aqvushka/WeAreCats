class PasswordError(Exception):
    pass


class LenghtError(PasswordError):
    def __init__(self):
        self.message = 'The password must contain more than 8 characters'
        super().__init__(self.message)


class LetterError(PasswordError):
    def __init__(self):
        self.message = 'The password must contain characters of different case'
        super().__init__(self.message)


class DigitError(PasswordError):
    def __init__(self):
        self.message = 'The password must contain at least one digit'
        super().__init__(self.message)


class SequenceError(PasswordError):
    def __init__(self):
        self.message = 'The password must not contain letters next to each other on the keyboard'
        super().__init__(self.message)


def check_password(password):
    neighbooring_char = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукуенгшщзхъ',
                         'фывапролджэ', 'ячсмитьбью']
    if len(password) > 8:
        fl_register_upper = False
        fl_register_lower = False
        fl_digit = False
        for i in range(len(password)):
            if password[i].isdigit():
                fl_digit = True
            if not password[i].isdigit():
                if password[i] == password[i].lower():
                    fl_register_lower = True
                else:
                    fl_register_upper = True
        if fl_register_upper and fl_register_lower and fl_digit:
            fl_neighbooring_char = False
            for i in range(2, len(password)):
                for j in neighbooring_char:
                    if password[i - 2:i].lower() in j or ''.join(reversed(password[i - 2:i].lower())) in j:
                        fl_neighbooring_char = True
            if fl_neighbooring_char == False:
                print('ok')
            raise SequenceError
        if not fl_register_upper or not fl_register_lower:
            raise LetterError
        else:
            raise DigitError
    raise LenghtError


if __name__ == '__main__':
    while True:
        password = input()
        try:
            check_password(password)
        except PasswordError as e:
            print(f'Your password is bad: {e}')
