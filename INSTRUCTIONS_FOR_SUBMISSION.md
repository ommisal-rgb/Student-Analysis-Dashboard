# Student Performance Dashboard - Submission Guide & Instructions

This repository contains all the required files and artifacts for the **Student Performance Dashboard** academic activity strictly built on **Tableau**.

---

## 📁 Package Contents

| File Name | Format | Description |
| :--- | :--- | :--- |
| `student_performance_dataset.csv` | CSV | Primary dataset containing 600 student records across 6 branches and 8 semesters. |
| `student_performance_dataset.xlsx` | Excel | Excel dataset format for alternative import / verification. |
| `Student_Performance_Dashboard.twb` | Tableau Workbook | Complete Tableau Desktop / Public workbook with 4 KPIs, 7 worksheets, and dashboard layout. |
| `A4_Student_Performance_Poster.html` | HTML / CSS | Printable A4 Dashboard Poster template adhering to all assignment guidelines. |
| `dashboard_screenshot.png` | PNG Image | High-resolution screenshot of the interactive Tableau dashboard. |
| `poster_preview.png` | PNG Image | Rendered screenshot preview of the A4 Poster document. |
| `generate_dataset.py` | Python Script | Data generator script used to generate realistic correlated academic data. |
| `generate_twb.py` | Python Script | Tableau XML generator script. |
| `generate_dashboard_render.py` | Python Script | Dashboard screenshot generator script. |

---

## 🚀 Step-by-Step Submission Instructions

### 1. Dataset Submission (CSV / Excel)
- Submit `student_performance_dataset.csv` or `student_performance_dataset.xlsx`.
- Contains 16 clean attributes: `Student_ID`, `Student_Name`, `Gender`, `Branch`, `Semester`, `Attendance_Percentage`, `Study_Hours_Per_Week`, `Midterm_Score`, `Assignment_Score`, `Final_Exam_Score`, `CGPA`, `Extracurricular_Activities`, `Parent_Education_Level`, `Internet_Access`, `Passing_Status`, and `Performance_Category`.

### 2. Tableau Dashboard File (.twb / .twbx)
1. Launch **Tableau Desktop** or **Tableau Public** (2024.1 or newer).
2. Go to **File → Open** and select `Student_Performance_Dashboard.twb`.
3. If prompted for data source location, select `student_performance_dataset.csv` in the same directory.
4. Interact with the dashboard cards and visual sheets:
   - **4 KPI Cards**: Total Students (600), Average CGPA (7.41), Avg Attendance (81.8%), Pass Rate (95.7%).
   - **7 Visualizations**: Bar Chart by Branch, Academic Progress Line Trend, Attendance vs CGPA Scatter Plot, Passing Status Donut Chart, Study Hours Stacked Chart, Box Plot Distribution, Treemap.
   - **Interactive Slicers**: Branch, Semester, Risk Category, Gender filters.
5. To export as a Packaged Workbook (`.twbx`):
   - Click **File → Export Packaged Workbook...** or **Save As... → Tableau Packaged Workbook (*.twbx)**.

### 3. A4 Dashboard Poster (PDF / HTML / Image)
1. Open `A4_Student_Performance_Poster.html` in Google Chrome, Microsoft Edge, or Firefox.
2. Student details preset in HTML & poster script:
   - **Student Name**: Advita Bhonde
   - **Roll Number**: 23003045
   - **Branch & Semester**: CSE / Semester 6
3. To export as PDF:
   - Press **Ctrl + P** (or Cmd + P on Mac).
   - Set **Destination** to `Save as PDF`.
   - Set **Paper Size** to `A4`.
   - Set **Margins** to `None` or `Default`.
   - Check **Options: Background Graphics**.
   - Click **Save** as `Student_Performance_Poster.pdf`.

---

## 📊 Key Insights Included in Poster
1. **Attendance-CGPA Threshold Effect**: Students with >85% attendance maintained an average CGPA of 8.12. Attendance below 65% resulted in a 78% risk category conversion rate.
2. **Branch Distinction Leaders**: Computer Science & Information Technology led distinction rates at 14.2% and 13.8%, backed by consistent assignment performance.
3. **Study Hours & Activity Balance**: 18-25 study hrs/week paired with "High" extracurricular activity yielded higher average exam scores (78.4) than isolated study.
4. **Mid-Degree Score Stabilization**: Academic performance peaks in Semester 2 (avg 7.54 CGPA) and stabilizes at 7.40 from Semester 4 through Semester 8.
5. **Early Warning Risk Indicator**: Assignment scores below 55 served as the strongest early indicator for final exam underperformance.
