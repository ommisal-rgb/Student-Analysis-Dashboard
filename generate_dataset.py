import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

num_students = 600

# Sample Names
first_names = ["Aarav", "Ananya", "Rohan", "Priya", "Aditya", "Sneha", "Rahul", "Kavya", "Vikram", "Isha",
               "Siddharth", "Meera", "Arjun", "Tanvi", "Karan", "Riya", "Dev", "Pooja", "Amit", "Neha",
               "Varun", "Shruti", "Manish", "Divya", "Akash", "Anushka", "Nikhil", "Simran", "Yash", "Kriti"]
last_names = ["Sharma", "Verma", "Patel", "Gupta", "Singh", "Kumar", "Rao", "Joshi", "Mehta", "Nair",
              "Chopra", "Deshmukh", "Reddy", "Mishra", "Bhat", "Agarwal", "Shah", "Kulkarni", "Malhotra", "Saxena"]

names = [f"{np.random.choice(first_names)} {np.random.choice(last_names)}" for _ in range(num_students)]

student_ids = [f"STU2024{str(i).zfill(3)}" for i in range(1, num_students + 1)]
genders = np.random.choice(["Male", "Female"], size=num_students, p=[0.52, 0.48])
branches = np.random.choice(
    ["Computer Science", "Electronics & Comm", "Information Tech", "Electrical Eng", "Mechanical Eng", "Civil Eng"],
    size=num_students,
    p=[0.25, 0.20, 0.20, 0.15, 0.10, 0.10]
)
semesters = [f"Semester {np.random.randint(1, 9)}" for _ in range(num_students)]
parent_education = np.random.choice(["High School", "Bachelor", "Master", "Doctorate"], size=num_students, p=[0.20, 0.45, 0.25, 0.10])
internet_access = np.random.choice(["Yes", "No"], size=num_students, p=[0.88, 0.12])
extracurriculars = np.random.choice(["High", "Medium", "Low"], size=num_students, p=[0.30, 0.50, 0.20])

# Generate correlated continuous variables
attendance = np.random.normal(82, 10, num_students)
attendance = np.clip(attendance, 52.0, 99.5).round(1)

study_hours = np.random.normal(20, 7, num_students)
study_hours = np.clip(study_hours, 6, 38).astype(int)

# Score generation influenced by study hours & attendance
midterm_base = 0.4 * attendance + 1.2 * study_hours + np.random.normal(15, 8, num_students)
midterm_score = np.clip(midterm_base, 35.0, 99.0).round(1)

assignment_base = 0.5 * attendance + 0.8 * study_hours + np.random.normal(20, 6, num_students)
assignment_score = np.clip(assignment_base, 42.0, 100.0).round(1)

final_base = 0.45 * midterm_score + 0.35 * assignment_score + 0.2 * attendance + np.random.normal(0, 5, num_students)
final_exam_score = np.clip(final_base, 32.0, 99.5).round(1)

# CGPA calculation on 10.0 scale
cgpa_base = (0.4 * final_exam_score + 0.3 * midterm_score + 0.3 * assignment_score) / 10.0
cgpa = np.clip(cgpa_base, 4.10, 9.85).round(2)

# Categorical derivations
passing_status = []
performance_category = []

for i in range(num_students):
    att = attendance[i]
    c = cgpa[i]
    if c >= 8.5 and att >= 80.0:
        passing_status.append("Academic Distinction")
        performance_category.append("High Performer")
    elif c >= 6.0 and att >= 65.0:
        passing_status.append("Pass")
        performance_category.append("Average Performer")
    elif att < 65.0 or c < 5.5:
        passing_status.append("At-Risk")
        performance_category.append("Needs Improvement")
    else:
        passing_status.append("Pass")
        performance_category.append("Average Performer")

df = pd.DataFrame({
    "Student_ID": student_ids,
    "Student_Name": names,
    "Gender": genders,
    "Branch": branches,
    "Semester": semesters,
    "Attendance_Percentage": attendance,
    "Study_Hours_Per_Week": study_hours,
    "Midterm_Score": midterm_score,
    "Assignment_Score": assignment_score,
    "Final_Exam_Score": final_exam_score,
    "CGPA": cgpa,
    "Extracurricular_Activities": extracurriculars,
    "Parent_Education_Level": parent_education,
    "Internet_Access": internet_access,
    "Passing_Status": passing_status,
    "Performance_Category": performance_category
})

# Save to CSV and Excel
csv_path = "C:/Users/ommis/.gemini/antigravity-ide/scratch/student-performance-dashboard/student_performance_dataset.csv"
xlsx_path = "C:/Users/ommis/.gemini/antigravity-ide/scratch/student-performance-dashboard/student_performance_dataset.xlsx"

df.to_csv(csv_path, index=False)
df.to_excel(xlsx_path, index=False)

print(f"Dataset generated successfully with {len(df)} records!")
print(f"CSV saved at: {csv_path}")
print(f"Excel saved at: {xlsx_path}")
print("\nDataset Summary Stats:")
print(df.describe())
