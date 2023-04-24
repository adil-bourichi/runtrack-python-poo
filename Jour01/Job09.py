class Student:
    def __init__(self, first_name, last_name, student_id):
        self._first_name = first_name
        self._last_name = last_name
        self._student_id = student_id
        self._credits = 0
        
    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            
    def get_credits(self):
        return self._credits
john_doe = Student("John", "Doe", 145)
john_doe.add_credits(7)
john_doe.add_credits(10)
john_doe.add_credits(13)
print("Le nombre de crédits de", john_doe._first_name, john_doe._last_name, "est de", john_doe.get_credits(), "points")
