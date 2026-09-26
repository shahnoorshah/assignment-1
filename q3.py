import pandas as pd

data={
    "Student_Name":["Rahul","Priya","Aman","Sneha","Riya"],
    "Roll_Number":[101,102,103,104,105],
    "Marks":[95,82,73,88,65],
    "Attendance":[90,85,95,80,92]
}

df=pd.DataFrame(data)

def calculate_grade(marks):
    if marks>=90:
        return "A"
    elif marks>=80:
        return "B"
    elif marks>=70:
        return "C"
    elif marks>=60:
        return "D"
    else:
        return "F"

df["Grade"]=df["Marks"].apply(calculate_grade)
print(df)