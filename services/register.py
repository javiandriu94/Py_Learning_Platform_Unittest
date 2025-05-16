from models.student import Student

class Register:
    def __init__(self):
        self.__users = {}

    def register_student(self,username,password,student_id):
        if username in self.__users:
            raise ValueError ('Username already exists!')
        student = Student (username, password, student_id)
        self.__users[username]= student
        return student
    
    def list_registed_users (self):
        return list(self.__users.value())
