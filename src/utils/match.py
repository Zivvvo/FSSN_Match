import numpy as np
import pandas as pd

class PI:
    def __init__(self, name, available_time_slots):
        self.name =name
        self.timeslots = []
        for i in range(available_time_slots):
            self.timeslots.append(None)
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
                
class student:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()
    

class match:
    def __init__(self, students, PIs):
        self.table = {}
        self.students = students.copy()
        self.PIs = PIs.copy()
        
    def fit(self,):
        waitlist = []
        i= 0
        while i < (len(self.students)):
            student = self.students[i]
            print(student.name)
            
            if (len(student.preferences) == 0):
                waitlist.append(student)
                i += 1
                continue

            B = student.preferences.pop(0)
            
            if (not isinstance(B, PI)):
                continue
            
            if (None in B.timeslots):
                print(True)
                B.timeslots[B.timeslots.index(None)] = student
                i += 1
            
        return waitlist
    
    def generate_table(self,):
        dictionary = {}
        for PI in self.PIs:
            dictionary[PI.name] = PI.timeslots
        df = pd.DataFrame(dictionary)
        return df