class Tech_learners_mentors():
    def __init__(self):
        self.interests = []
        self.expertise = []
        self.learners = []
        self.mentors = []
        self.hours = []
        self.minutes = []
        self.time = []
    def addStacksInterest(self,interest):
        self.interests.insert(0,interest)
    def addStacksExpertise(self,expertise):
        self.expertise.insert(0,expertise)
    def setMentorOrLearner(self,name,interest_or_expertise):
        self.name=name
        self.interest_or_expertise=interest_or_expertise
        if(self.interest_or_expertise in self.interests):
            self.learners.insert(0,self.name)
        if(self.interest_or_expertise in self.expertise):
            self.mentors.insert(0,self.name)
    def setAvailableTime(self):
        for person in self.mentors:
            print("Enter Available time for",person,"in railway time format")
            print("Enter the hours part")
            hours=input()
            self.hours.insert(0,hours)
            print("Enter the minutes part")
            minutes=input()
            self.minutes.insert(0,minutes)
        self.hours.reverse()
        self.minutes.reverse()
        j=0
        for i in self.hours:
            self.time.insert(0,i*60+self.minutes[j])
            j=j+1
        self.time.reverse()
    def getMentor(self,required_hrs,required_mins):
        self.r_hrs=required_hrs
        self.r_mins=required_mins
        r_time=self.r_hrs*60+self.r_mins
        j=0
        for i in time:
            if(i==r_time):
                print("Available mentor:",self.mentors[j])
            j=j+1
