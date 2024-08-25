class UserAlreadyExistsError(Exception):
    pass

class UserNotFoundError(Exception):
    pass

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        if self._is_email_registered(email):
            raise UserAlreadyExistsError(f"Email {email} já está registrado.")
        user = User(name, email)
        self.users.append(user)
        return user

    def update_user(self, email, new_name=None, new_email=None):
        user = self._find_user_by_email(email)
        if new_name:
            user.name = new_name
        if new_email:
            if self._is_email_registered(new_email) and new_email != email:
                raise UserAlreadyExistsError(f"Email {new_email} já está registrado.")
            user.email = new_email
        return user
    
    def remove_user(self, email):
        user = self._find_user_by_email(email)
        self.users.remove(user)

    def _is_email_registered(self, email):
        return any(user.email == email for user in self.users)

    def get_users(self):
        return self.users

    def _find_user_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        raise UserNotFoundError(f"Usuário com email {email} não encontrado.")