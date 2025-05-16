from models.user import User

class Student(User):
    __slots__ = ('_username','_password','_student_id','_courses')

    def __init__(self, username, password, student_id):
        super().__init__(username,password)
        self._student_id = student_id
        self._courses = []

    @property
    def student_id (self):
        return self._student_id
    
    
    def enroll_course (self, course):
        if course not in self.courses:
            self._courses.append(course)
    
    def list_courses (self):
        return self._courses
    
    def __str__(self):
        return f"Student:{self._username} (ID:{self._student_id})"
        
