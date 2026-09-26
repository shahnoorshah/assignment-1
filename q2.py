import pandas as pd

data={
    "Student_Name":["Rahul","Priya","Aman","Sneha","Riya"],
    "Roll_Number":[101,102,103,104,105],
    "Marks":[85,72,91,78,88],
    "Attendance":[90,85,95,80,92]
}

df=pd.DataFrame(data)

print("Complete Student Data: ")
print(df)
filtered_df=df[df["Marks"]>80]
print("\nStudents who scored above 80 marks: ")
print(filtered_df)