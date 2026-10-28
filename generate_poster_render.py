import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Set up canvas with A4 proportions (8.27 x 11.69 inches)
fig = plt.figure(figsize=(8.27, 11.69), dpi=300, facecolor='#CBD5E1')
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

# Outer Page Background (#F1F5F9)
ax.add_patch(patches.Rectangle((0.03, 0.02), 0.94, 0.96, color='#F1F5F9', zorder=1))

# Top Outer Title
ax.text(0.5, 0.945, "Student Performance Cohort Analysis", color='#4338CA', fontsize=18, fontweight='bold', family='sans-serif', ha='center', zorder=2)

# Main Dashboard Card Container (Mokkup.ai Frame)
ax.add_patch(patches.FancyBboxPatch((0.06, 0.05), 0.88, 0.86, boxstyle="round,pad=0.015", facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1, zorder=2))

# Header Bar inside Dashboard Frame
ax.text(0.12, 0.88, "Tableau Public BI", color='#0F172A', fontsize=11, fontweight='bold', zorder=3)
ax.text(0.88, 0.88, "STUDENT PERFORMANCE & RETENTION COHORT ANALYSIS", color='#1E293B', fontsize=9.5, fontweight='bold', ha='right', zorder=3)
ax.plot([0.08, 0.92], [0.865, 0.865], color='#F1F5F9', linewidth=1.5, zorder=3)

# Filters / Metadata Row Box
ax.add_patch(patches.FancyBboxPatch((0.08, 0.795), 0.84, 0.058, boxstyle="round,pad=0.008", facecolor='#FAFAFA', edgecolor='#F1F5F9', linewidth=1, zorder=3))

labels = ["STUDENT NAME", "ROLL / REG. NO", "BRANCH & SEMESTER", "ACADEMIC COHORT", "DEPARTMENT SCOPE"]
values = ["Advita Bhonde", "23003045", "CSE / Sem 6", "2023 - 2026", "All Engineering"]
x_coords = [0.10, 0.28, 0.46, 0.65, 0.82]

for l, v, x in zip(labels, values, x_coords):
    ax.text(x, 0.835, l, color='#64748B', fontsize=6.5, fontweight='bold', zorder=4)
    ax.text(x, 0.81, v, color='#0F172A', fontsize=8.5, fontweight='bold', zorder=4)

# SECTION 1: Cohort Heatmap Table Box
ax.add_patch(patches.FancyBboxPatch((0.08, 0.46), 0.84, 0.315, boxstyle="round,pad=0.008", facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1, zorder=3))

# Header of Heatmap Card
ax.add_patch(patches.Rectangle((0.08, 0.74), 0.84, 0.035, color='#F8FAFC', zorder=4))
ax.text(0.10, 0.752, "Cohort Retention & Academic Progression Heatmap", color='#334155', fontsize=9, fontweight='bold', zorder=5)
ax.text(0.90, 0.752, "Average CGPA by Branch Cohort over Semesters", color='#64748B', fontsize=7.5, ha='right', zorder=5)

# Heatmap Table Headers
cols = ["Branch Cohort", "Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6"]
col_x = [0.12, 0.26, 0.38, 0.50, 0.62, 0.74, 0.86]

for c, x in zip(cols, col_x):
    ha_val = 'left' if c == "Branch Cohort" else 'center'
    ax.text(x, 0.718, c, color='#475569', fontsize=8, fontweight='bold', ha=ha_val, zorder=4)

# Heatmap Grid Rows & Colors
row_names = ["CS Cohort", "IT Cohort", "ECE Cohort", "EEE Cohort", "Mech Cohort", "Civil Cohort"]
matrix_data = [
    ["8.41 CGPA", "8.58 CGPA", "8.35 CGPA", "8.50 CGPA", "8.87 CGPA", "8.78 CGPA"],
    ["8.65 CGPA", "8.48 CGPA", "8.55 CGPA", "8.95 CGPA", "8.98 CGPA", "--"],
    ["8.09 CGPA", "8.18 CGPA", "8.06 CGPA", "8.45 CGPA", "--", "--"],
    ["7.70 CGPA", "7.82 CGPA", "8.11 CGPA", "--", "--", "--"],
    ["7.36 CGPA", "7.55 CGPA", "--", "--", "--", "--"],
    ["6.95 CGPA", "--", "--", "--", "--", "--"]
]

colors_matrix = [
    ['#0D9488', '#14B8A6', '#0D9488', '#0F766E', '#0D9488', '#14B8A6'],
    ['#14B8A6', '#0D9488', '#14B8A6', '#0F766E', '#0D9488', None],
    ['#2DD4BF', '#14B8A6', '#14B8A6', '#0D9488', None, None],
    ['#2DD4BF', '#2DD4BF', '#14B8A6', None, None, None],
    ['#5EEAD4', '#2DD4BF', None, None, None, None],
    ['#99F6E4', None, None, None, None, None]
]

row_y = [0.675, 0.635, 0.595, 0.555, 0.515, 0.475]

for r_idx, (r_name, r_y) in enumerate(zip(row_names, row_y)):
    ax.text(0.12, r_y, r_name, color='#334155', fontsize=8, fontweight='bold', ha='left', va='center', zorder=4)
    for c_idx in range(6):
        val = matrix_data[r_idx][c_idx]
        cell_color = colors_matrix[r_idx][c_idx]
        cx = col_x[c_idx + 1]
        
        if cell_color is not None:
            text_col = '#0F172A' if cell_color in ['#2DD4BF', '#5EEAD4', '#99F6E4'] else '#FFFFFF'
            ax.add_patch(patches.FancyBboxPatch((cx - 0.05, r_y - 0.016), 0.10, 0.032, boxstyle="round,pad=0.002", facecolor=cell_color, edgecolor='none', zorder=4))
            ax.text(cx, r_y, val, color=text_col, fontsize=7.5, fontweight='bold', ha='center', va='center', zorder=5)
        elif val == "--":
            ax.text(cx, r_y, "--", color='#94A3B8', fontsize=8, ha='center', va='center', zorder=4)

# SECTION 2: Bottom Split (Area Chart & Stacked Bar Chart)

# Left: Area Chart Box
ax.add_patch(patches.FancyBboxPatch((0.08, 0.09), 0.405, 0.35, boxstyle="round,pad=0.008", facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1, zorder=3))

ax.add_patch(patches.Rectangle((0.08, 0.405), 0.405, 0.035, color='#F8FAFC', zorder=4))
ax.text(0.10, 0.417, "Academic Progress w.r.t. Attendance Tier", color='#334155', fontsize=8.5, fontweight='bold', zorder=5)

# Area Chart Axis & Fills inside subplot
ax_area = fig.add_axes([0.11, 0.16, 0.35, 0.22])
ax_area.patch.set_alpha(0.0)

x = np.linspace(1, 6, 100)
y_high = 7.5 + 0.3 * np.sin(x) + 0.2 * x
y_mid = 6.0 + 0.25 * np.sin(x) + 0.15 * x
y_low = 4.5 + 0.2 * np.sin(x) + 0.1 * x

ax_area.fill_between(x, y_high, color='#38BDF8', alpha=0.8, label='>85% Attendance')
ax_area.fill_between(x, y_mid, color='#2563EB', alpha=0.8, label='65-85% Attendance')
ax_area.fill_between(x, y_low, color='#1D4ED8', alpha=0.9, label='<65% Attendance')

ax_area.plot(x, y_high, color='#38BDF8', linewidth=1.5)
ax_area.plot(x, y_mid, color='#60A5FA', linewidth=1.5)
ax_area.plot(x, y_low, color='#1D4ED8', linewidth=1.5)

ax_area.set_xticks([1, 2, 3, 4, 5, 6])
ax_area.set_xticklabels(['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5', 'Sem 6'], fontsize=7, color='#64748B')
ax_area.set_yticks([0, 5, 7.5, 10])
ax_area.set_yticklabels(['0', '5.0', '7.5', '10.0'], fontsize=7, color='#64748B')
ax_area.spines['top'].set_visible(False)
ax_area.spines['right'].set_visible(False)
ax_area.spines['left'].set_color('#CBD5E1')
ax_area.spines['bottom'].set_color('#CBD5E1')

# Legend below area chart
ax.add_patch(patches.Rectangle((0.11, 0.11), 0.015, 0.015, color='#38BDF8', zorder=5))
ax.text(0.13, 0.117, ">85%", color='#475569', fontsize=7, fontweight='bold', va='center', zorder=5)

ax.add_patch(patches.Rectangle((0.22, 0.11), 0.015, 0.015, color='#2563EB', zorder=5))
ax.text(0.24, 0.117, "65-85%", color='#475569', fontsize=7, fontweight='bold', va='center', zorder=5)

ax.add_patch(patches.Rectangle((0.34, 0.11), 0.015, 0.015, color='#1D4ED8', zorder=5))
ax.text(0.36, 0.117, "<65%", color='#475569', fontsize=7, fontweight='bold', va='center', zorder=5)


# Right: Stacked Bar Chart Box
ax.add_patch(patches.FancyBboxPatch((0.515, 0.09), 0.405, 0.35, boxstyle="round,pad=0.008", facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1, zorder=3))

ax.add_patch(patches.Rectangle((0.515, 0.405), 0.405, 0.035, color='#F8FAFC', zorder=4))
ax.text(0.535, 0.417, "Academic Cohort Distribution Over Time", color='#334155', fontsize=8.5, fontweight='bold', zorder=5)

# Stacked Bar Subplot
ax_bar = fig.add_axes([0.545, 0.16, 0.35, 0.22])
ax_bar.patch.set_alpha(0.0)

q_categories = ['Q1', 'Q2', 'Q3', 'Q4']
b_q1 = np.array([100.0, 47.63, 31.25, 26.38])
b_q2 = np.array([0.0, 52.37, 36.42, 21.61])
b_q3 = np.array([0.0, 0.0, 32.23, 28.46])
b_q4 = np.array([0.0, 0.0, 0.0, 23.55])

w = 0.55
ax_bar.bar(q_categories, b_q1, width=w, color='#38BDF8', label='Q1 Cohort')
ax_bar.bar(q_categories, b_q2, width=w, bottom=b_q1, color='#2563EB', label='Q2 Cohort')
ax_bar.bar(q_categories, b_q3, width=w, bottom=b_q1+b_q2, color='#1D4ED8', label='Q3 Cohort')
ax_bar.bar(q_categories, b_q4, width=w, bottom=b_q1+b_q2+b_q3, color='#1E40AF', label='Q4 Cohort')

ax_bar.set_yticks([0, 30, 60, 100])
ax_bar.set_yticklabels(['0M', '10M', '20M', '30M'], fontsize=7, color='#64748B')
ax_bar.tick_params(axis='x', colors='#64748B', labelsize=7)
ax_bar.spines['top'].set_visible(False)
ax_bar.spines['right'].set_visible(False)
ax_bar.spines['left'].set_color('#CBD5E1')
ax_bar.spines['bottom'].set_color('#CBD5E1')

# Bar Labels
ax_bar.text(0, 50, "100.00%", ha='center', va='center', color='white', fontsize=6.5, fontweight='bold')
ax_bar.text(1, 23, "47.63%", ha='center', va='center', color='white', fontsize=6.5, fontweight='bold')
ax_bar.text(1, 74, "52.37%", ha='center', va='center', color='white', fontsize=6.5, fontweight='bold')
ax_bar.text(2, 15, "31.25%", ha='center', va='center', color='white', fontsize=6, fontweight='bold')
ax_bar.text(2, 49, "36.42%", ha='center', va='center', color='white', fontsize=6, fontweight='bold')
ax_bar.text(2, 84, "32.23%", ha='center', va='center', color='white', fontsize=6, fontweight='bold')

# Legend below bar chart
ax.add_patch(patches.Rectangle((0.545, 0.11), 0.015, 0.015, color='#38BDF8', zorder=5))
ax.text(0.565, 0.117, "Q1 Acquired", color='#475569', fontsize=7, fontweight='bold', va='center', zorder=5)

ax.add_patch(patches.Rectangle((0.675, 0.11), 0.015, 0.015, color='#2563EB', zorder=5))
ax.text(0.695, 0.117, "Q2 Acquired", color='#475569', fontsize=7, fontweight='bold', va='center', zorder=5)

ax.add_patch(patches.Rectangle((0.805, 0.11), 0.015, 0.015, color='#1D4ED8', zorder=5))
ax.text(0.825, 0.117, "Q3 Acquired", color='#475569', fontsize=7, fontweight='bold', va='center', zorder=5)

# Footer Note inside Dashboard Card Frame
ax.plot([0.08, 0.92], [0.075, 0.075], color='#E2E8F0', linewidth=1, zorder=3)
ax.text(0.08, 0.06, "Designed with Tableau BI Standards | Academic Submission", color='#64748B', fontsize=7, zorder=4)
ax.text(0.92, 0.06, "Student: Advita Bhonde (Roll No: 23003045)", color='#4338CA', fontsize=7.5, fontweight='bold', ha='right', zorder=4)

plt.savefig("poster_preview.png", bbox_inches='tight', pad_inches=0.1, dpi=300)
print("Poster preview rendered in Mokkup style to poster_preview.png")
