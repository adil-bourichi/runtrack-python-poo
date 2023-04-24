class Student:
    def __init__(self, first_name, last_name, student_id):
        self._first_name = first_name
        self._last_name = last_name
        self._student_id = student_id
        self._credits = 0
        self._level = self._studentEval()
        
    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._studentEval()
            
    def get_credits(self):
        return self._credits
    
    def get_full_name(self):
        return self._first_name + " " + self._last_name
    
    def studentInfo(self):
        print("Nom:", self._first_name, self._last_name)
        print("Identifiant:", self._student_id)
        print("Niveau:", self._level)
        
    def _studentEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien."
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        
john_doe = Student("John", "Doe", 145)
john_doe.add_credits(80)
john_doe.studentInfo()
