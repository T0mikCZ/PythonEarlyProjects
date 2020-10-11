class Job:

    def __init__(self, jobName, jobSalary, jobEnergy):
        self.jobName = jobName
        self.jobSalary = jobSalary
        self.jobEnergy = jobEnergy

    def promote(self):
        self.jobSalary += int((self.jobSalary / 2)) 