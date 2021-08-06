import pandas as pd

from utils.match import student, PI, match

def load_csv(path):
    return pd.read_csv("C:/Users/Zhe Fan/Downloads/FSSN_responses.csv")

def generate_profs(df, timeslots):
    prof_list = list(dict.fromkeys(df.iloc[:,3].to_list()))
    list_of_tups = []
    for prof in prof_list:
        obj = PI(prof, timeslots)
        list_of_tups.append(obj)
    return list_of_tups

def generate_pref_list(df):
    df1=df.iloc[:,3:6]
    pref_list = df1.values.tolist()
    return pref_list

def generate_students(df, preference_list, profs):
    student_list =  list(dict.fromkeys(df.iloc[:,2].to_list()))
    list_of_students= []
    for stu, pref in zip(student_list, preference_list):
        pref_prof = []
        for x in pref:
            for y in profs:
                if (y.name == x):
                    pref_prof.append(y)
        list_of_students.append(student(stu, pref_prof))
    return list_of_students

