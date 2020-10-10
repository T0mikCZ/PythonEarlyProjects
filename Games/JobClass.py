class Job:

    def __init__(self, jobName, jobSalary):
        self.jobName = jobName
        self.jobSalary = jobSalary

    def promote(self):
        self.jobSalary += int((self.jobSalary / 2)) 