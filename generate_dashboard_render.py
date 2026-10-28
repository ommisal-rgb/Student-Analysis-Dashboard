import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
df = pd.read_csv("C:/Users/ommis/.gemini/antigravity-ide/scratch/student-performance-dashboard/student_performance_dataset.csv")

# Set up figure with clean background
plt.style.use('default')
fig = plt.figure(figsize=(16, 9), facecolor='#F8FAFC')
gs = fig.add_gridspec(3, 3, height_ratios=[0.9, 2.3, 2.5], hspace=0.38, wspace=0.25)

# Color Palette
navy = '#0F172A'
teal = '#0D9488'
indigo = '#4F46E5'
amber = '#D97706'
rose = '#E11D48'

# Header Banner (Row 0 - Top Header)
ax_header = fig.add_subplot(gs[0, :])
ax_header.axis('off')
ax_header.add_patch(plt.Rectangle((0, 0.25), 1, 0.75, color='#1E293B', transform=ax_header.transAxes, zorder=1))
ax_header.text(0.02, 0.68, "Student Performance Analytics Dashboard", color='white', fontsize=19, fontweight='bold', zorder=2)
ax_header.text(0.02, 0.38, "Executive Academic Intelligence & Student Performance Monitoring | Tableau Public 2024.1", color='#94A3B8', fontsize=11, zorder=2)
ax_header.text(0.80, 0.52, "[Filter: All Branches | Semesters 1-8]", color='#38BDF8', fontsize=9.5, bbox=dict(boxstyle='round,pad=0.4', facecolor='#0F172A', edgecolor='#38BDF8'), zorder=2)

# KPI Cards Overlay in lower half of header zone (Row 0 bottom)
total_students = len(df)
avg_cgpa = df['CGPA'].mean()
avg_att = df['Attendance_Percentage'].mean()
pass_rate = (df['Passing_Status'] != 'At-Risk').mean() * 100

ax_header.text(0.08, 0.0, f"TOTAL STUDENTS\n{total_students:,}", ha='center', va='bottom', fontsize=10, fontweight='bold', color=navy, bbox=dict(boxstyle='round,pad=0.5', facecolor='#EFF6FF', edgecolor='#BFDBFE'), zorder=3)
ax_header.text(0.35, 0.0, f"AVERAGE CGPA\n{avg_cgpa:.2f} / 10.0", ha='center', va='bottom', fontsize=10, fontweight='bold', color=teal, bbox=dict(boxstyle='round,pad=0.5', facecolor='#F0FDF4', edgecolor='#BBF7D0'), zorder=3)
ax_header.text(0.63, 0.0, f"AVG ATTENDANCE\n{avg_att:.1f}%", ha='center', va='bottom', fontsize=10, fontweight='bold', color=indigo, bbox=dict(boxstyle='round,pad=0.5', facecolor='#EEF2FF', edgecolor='#C7D2FE'), zorder=3)
ax_header.text(0.90, 0.0, f"PASS RATE\n{pass_rate:.1f}%", ha='center', va='bottom', fontsize=10, fontweight='bold', color='#059669', bbox=dict(boxstyle='round,pad=0.5', facecolor='#ECFDF5', edgecolor='#A7F3D0'), zorder=3)

# Chart 1: Avg CGPA by Branch (Row 1 Left)
ax_branch = fig.add_subplot(gs[1, 0])
ax_branch.set_facecolor('#FFFFFF')
for spine in ax_branch.spines.values(): spine.set_color('#E2E8F0')
branch_cgpa = df.groupby('Branch')['CGPA'].mean().sort_values(ascending=True)
bars = ax_branch.barh(branch_cgpa.index, branch_cgpa.values, color=indigo, height=0.55)
ax_branch.set_title("Avg CGPA by Department / Branch", fontsize=11, fontweight='bold', color=navy, pad=10)
ax_branch.set_xlim(0, 10)
for bar in bars:
    ax_branch.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height()/2, f'{bar.get_width():.2f}', va='center', fontsize=9, fontweight='bold', color='#334155')

# Chart 2: Academic Progression Trend (Row 1 Right)
ax_trend = fig.add_subplot(gs[1, 1:])
ax_trend.set_facecolor('#FFFFFF')
for spine in ax_trend.spines.values(): spine.set_color('#E2E8F0')
sem_order = [f"Semester {i}" for i in range(1, 9)]
sem_stats = df.groupby('Semester')[['CGPA', 'Final_Exam_Score', 'Attendance_Percentage']].mean().reindex(sem_order)
ax_trend.plot(sem_stats.index, sem_stats['CGPA'], marker='o', linewidth=2.5, color=teal, label='Avg CGPA (10.0 scale)')
ax_trend.set_title("Academic Performance Progression (Semesters 1 to 8)", fontsize=11, fontweight='bold', color=navy, pad=10)
ax_trend.set_ylim(5, 10)
ax_trend.grid(True, linestyle='--', alpha=0.5)
ax_trend.tick_params(axis='x', rotation=15)
ax_trend.legend(loc='lower right', frameon=True, fontsize=9)

# Chart 3: Attendance vs CGPA Scatter (Row 2 Left)
ax_scatter = fig.add_subplot(gs[2, 0])
ax_scatter.set_facecolor('#FFFFFF')
for spine in ax_scatter.spines.values(): spine.set_color('#E2E8F0')
scatter = ax_scatter.scatter(df['Attendance_Percentage'], df['CGPA'], c=df['CGPA'], cmap='Blues', alpha=0.75, edgecolors='none', s=24)
ax_scatter.axvline(65, color=rose, linestyle='--', linewidth=1.5, label='At-Risk Threshold (65%)')
ax_scatter.set_title("Attendance % vs CGPA Correlation", fontsize=11, fontweight='bold', color=navy, pad=10)
ax_scatter.set_xlabel("Attendance %", fontsize=9)
ax_scatter.set_ylabel("CGPA", fontsize=9)
ax_scatter.legend(loc='upper left', fontsize=8)

# Chart 4: Passing Status Donut (Row 2 Middle)
ax_donut = fig.add_subplot(gs[2, 1])
ax_donut.set_facecolor('#FFFFFF')
for spine in ax_donut.spines.values(): spine.set_color('#E2E8F0')
status_counts = df['Passing_Status'].value_counts()
colors = ['#10B981', '#3B82F6', '#EF4444']
wedges, texts, autotexts = ax_donut.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=colors, textprops=dict(color=navy, fontsize=8.5))
plt.setp(autotexts, size=8.5, weight="bold", color="white")
centre_circle = plt.Circle((0,0), 0.55, fc='white')
ax_donut.add_artist(centre_circle)
ax_donut.set_title("Academic Status Distribution", fontsize=11, fontweight='bold', color=navy, pad=10)

# Chart 5: Extracurricular Impact (Row 2 Right)
ax_study = fig.add_subplot(gs[2, 2])
ax_study.set_facecolor('#FFFFFF')
for spine in ax_study.spines.values(): spine.set_color('#E2E8F0')
extra_cgpa = df.groupby(['Extracurricular_Activities'])['CGPA'].mean().reindex(['High', 'Medium', 'Low'])
bars_extra = ax_study.bar(extra_cgpa.index, extra_cgpa.values, color=[amber, teal, indigo], width=0.5)
ax_study.set_title("CGPA by Extracurricular Level", fontsize=11, fontweight='bold', color=navy, pad=10)
ax_study.set_ylim(0, 10)
for bar in bars_extra:
    ax_study.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, f'{bar.get_height():.2f}', ha='center', fontsize=9, fontweight='bold', color=navy)

plt.subplots_adjust(top=0.94, bottom=0.06, left=0.06, right=0.95)
output_path = "C:/Users/ommis/.gemini/antigravity-ide/scratch/student-performance-dashboard/dashboard_screenshot.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Re-rendered dashboard screenshot saved to {output_path}")
