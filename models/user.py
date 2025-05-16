import datetime
class User:
    __slots__ = ('_username','_password', '_email', '_role')
    
    def __init__(self, username: str, password: str, email: str, role: str='student'):
        self._username = username
        self._password = password
        self._email =  email
        self._role = role
        self.created_at = datetime.now()
        self.last_login = None

    @property
    def username (self):
        return self._username
    
    
    def check_password(self, password: str):
        return self._password == password
    
    def change_password(self, old_password: str, new_password: str):
        if self.check_password(old_password):
            self._password = new_password
        else:
            raise ValueError("Incorrect current password")
    
    def update_last_login(self):
        self.last_login = datetime.now()

    @property
    def email (self):
        return self._email
    
    @email.setter
    def email(self, new_email: str):
        if "@" and "." not in new_email:
            raise ValueError("Invalid email format")
        self.email = new_email

    def is_admin(self):
        return self._role == "admin"
    
    def __str__(self):
        return f"User:{self.username}"