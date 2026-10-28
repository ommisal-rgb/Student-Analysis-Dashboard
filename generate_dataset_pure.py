import csv
import random
import math

random.seed(42)

num_students = 600

first_names = ["Aarav", "Ananya", "Rohan", "Priya", "Aditya", "Sneha", "Rahul", "Kavya", "Vikram", "Isha",
               "Siddharth", "Meera", "Arjun", "Tanvi", "Karan", "Riya", "Dev", "Pooja", "Amit", "Neha",
               "Varun", "Shruti", "Manish", "Divya", "Akash", "Anushka", "Nikhil", "Simran", "Yash", "Kriti"]
last_names = ["Sharma", "Verma", "Patel", "Gupta", "Singh", "Kumar", "Rao", "Joshi", "Mehta", "Nair",
              "Chopra", "Deshmukh", "Reddy", "Mishra", "Bhat", "Agarwal", "Shah", "Kulkarni", "Malhotra", "Saxena"]

branches_weighted = [
    ("Computer Science", 0.25),
    ("Electronics & Comm", 0.20),
    ("Information Tech", 0.20),
    ("Electrical Eng", 0.15),
    ("Mechanical Eng", 0.10),
    ("Civil Eng", 0.10)
]

def choice_weighted(options):
    r = random.random()
    cum = 0
    for val, weight in options:
        cum += weight
        if r <= cum:
            return val
    return options[-1][0]

rows = []
for i in range(1, num_students + 1):
    student_id = f"STU2024{str(i).zfill(3)}"
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    gender = random.choice(["Male", "Female"])
    branch = choice_weighted(branches_weighted)
    semester = f"Semester {random.randint(1, 8)}"
    
    parent_edu = choice_weighted([("High School", 0.20), ("Bachelor", 0.45), ("Master", 0.25), ("Doctorate", 0.10)])
    internet = choice_weighted([("Yes", 0.88), ("No", 0.12)])
    extracurricular = choice_weighted([("High", 0.30), ("Medium", 0.50), ("Low", 0.20)])
    
    # Attendance between 52% and 99.5%
    att = round(random.gauss(82, 10), 1)
    att = max(52.0, min(99.5, att))
    
    # Study hours per week 6 to 38
    study_hrs = int(round(random.gauss(20, 7)))
    study_hrs = max(6, min(38, study_hrs))
    
    # Midterm score 35 to 99
    midterm = 0.4 * att + 1.2 * study_hrs + random.gauss(15, 8)
    midterm = round(max(35.0, min(99.0, midterm)), 1)
    
    # Assignment score 42 to 100
    assignment = 0.5 * att + 0.8 * study_hrs + random.gauss(20, 6)
    assignment = round(max(42.0, min(100.0, assignment)), 1)
    
    # Final Exam score 32 to 99.5
    final_score = 0.45 * midterm + 0.35 * assignment + 0.2 * att + random.gauss(0, 5)
    final_score = round(max(32.0, min(99.5, final_score)), 1)
    
    # CGPA calculation (10.0 scale)
    cgpa = (0.4 * final_score + 0.3 * midterm + 0.3 * assignment) / 10.0
    cgpa = round(max(4.10, min(9.85, cgpa)), 2)
    
    if cgpa >= 8.5 and att >= 80.0:
        status = "Academic Distinction"
        perf_cat = "High Performer"
    elif cgpa >= 6.0 and att >= 65.0:
        status = "Pass"
        perf_cat = "Average Performer"
    elif att < 65.0 or cgpa < 5.5:
        status = "At-Risk"
        perf_cat = "Needs Improvement"
    else:
        status = "Pass"
        perf_cat = "Average Performer"
        
    rows.append([
        student_id, name, gender, branch, semester, att, study_hrs,
        midterm, assignment, final_score, cgpa, extracurricular,
        parent_edu, internet, status, perf_cat
    ])

header = [
    "Student_ID", "Student_Name", "Gender", "Branch", "Semester",
    "Attendance_Percentage", "Study_Hours_Per_Week", "Midterm_Score",
    "Assignment_Score", "Final_Exam_Score", "CGPA", "Extracurricular_Activities",
    "Parent_Education_Level", "Internet_Access", "Passing_Status", "Performance_Category"
]

csv_file = "C:/Users/ommis/.gemini/antigravity-ide/scratch/student-performance-dashboard/student_performance_dataset.csv"
with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Dataset generated successfully with {len(rows)} records at {csv_file}")
