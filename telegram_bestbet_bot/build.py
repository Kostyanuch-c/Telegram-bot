import hashlib


class PasswordBuilder:
    def __init__(self, passwordGenerator):
        self.passwordGenerator = passwordGenerator

    def build_password(self, len=10, options=[]):
        print(self.passwordGenerator)
        print(options)
        password = self.passwordGenerator.generate_password(len, options)
        m = hashlib.sha1()
        m.update(password.encode())
        digest = m.hexdigest()

        return {'password': password, 'digest': digest}
