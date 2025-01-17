class UniversityAdmissionsAgent:
    def __init__(self, name):
        self.name = name
        self.applications = []

    def receive_application(self, student):
        self.applications.append(student)
        print(f"Application received from {student.name}")

    def process_applications(self):
        for student in self.applications:
            print(f"Processing application for {student.name}")
        
            student.application_status = "Accepted" 
