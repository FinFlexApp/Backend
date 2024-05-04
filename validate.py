import re


def validate(data, regex):
    """Custom Validator"""
    return True if re.match(regex, data) else False


def validate_password(password: str):
    """Password Validator"""
    reg = r"[0-9a-zA-Z!@#$%^&*]{8,}"
    return validate(password, reg)


def validate_email(email: str):
    """Email Validator"""
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return validate(email, regex)


def validate_user(**args):

    """User Validator"""
    if not args.get('email'):
        return {
            'error': 'Нужен Email',
        }
    if not args.get('password'):
        return {
            'error': 'Нужен Password',
        }
    if not args.get('nickname'):
        return {
            'error': 'Нужен Nickname',
        }
    if not args.get('firstname'):
        return {
            'error': 'Нужен Firstname',
        }
    if not args.get('surname'):
        return {
            'error': 'Нужен Surname',
        }
    if not validate_email(args.get('email')):
        return {
            'error': 'Нужен Email'
        }
    if not validate_password(args.get('password')):
        return {
            'error': 'Пароль недействителен. Он должен содержать не менее 8 символов и состоять из \
                символов 0-9a-zA-Z!@#$%^&*'
        }
    if not 2 <= len(args['nickname']) <= 40:
        return {
            'error': 'Name must be between 2 and 40 lenth'
        }
    return True


def validate_email_and_password(email, password):
    """Email and Password Validator"""
    if not (email and password):
        return {
            'error': 'Нужен пароль и  email'
        }
    if not validate_email(email):
        return {
            'error': 'Электронная почта недействительна'
        }
    if not validate_password(password):
        return {
            'error': 'Password is invalid, Should be atleast 8 characters with \
                upper and lower case letters, numbers and special characters'
        }
    return True
