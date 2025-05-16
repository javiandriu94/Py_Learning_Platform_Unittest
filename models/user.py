class User:
    __slots__ = ('_username','_password')
    
    def __init__(self, username, password ):
        self._username = username
        self._password = password

    @property
    def username (self):
        return self._username
    
    def check_password(self,password):
        return self.password == password
    
    def __repr__(self):
        return f"User:'{self.username}'"