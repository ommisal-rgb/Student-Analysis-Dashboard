import os
import base64
from playwright.sync_api import sync_playwright

def image_to_base64(img_path):
    with open(img_path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')

def main():
    workspace_dir = os.path.dirname(os.path.abspath(__file__))
    dashboard_img_path = os.path.join(workspace_dir, "dashboard_screenshot.png")
    
    if os.path.exists(dashboard_img_path):
        db_b64 = image_to_base64(dashboard_img_path)
    else:
        db_b64 = ""

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Student Performance Analysis - Tableau Dashboard Summary</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 15mm 15mm 15mm 15mm;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Times New Roman', Times, Georgia, serif;
    font-size: 10.5pt;
    line-height: 1.35;
    color: #000000;
    background: #ffffff;
  }}

  .page {{
    width: 100%;
    position: relative;
  }}

  .page-break {{
    page-break-before: always;
  }}

  /* Main Title Styling */
  .doc-title {{
    text-align: center;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 20pt;
    font-weight: bold;
    color: #1F4E79;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 0;
    margin-bottom: 4px;
  }}

  .doc-subtitle {{
    text-align: center;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 12pt;
    font-weight: bold;
    color: #000000;
    margin-bottom: 16px;
  }}

  /* Top Info Table */
  .info-table {{
    width: 65%;
    margin: 0 auto 18px auto;
    border-collapse: collapse;
    font-size: 10pt;
  }}

  .info-table td {{
    border: 1px solid #000000;
    padding: 5px 12px;
  }}

  .info-table .label-col {{
    font-weight: bold;
    width: 35%;
    background-color: #ffffff;
  }}

  .info-table .val-col {{
    width: 65%;
  }}

  /* Section Headings */
  h2.section-heading {{
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 11.5pt;
    font-weight: bold;
    color: #000000;
    margin-top: 14px;
    margin-bottom: 6px;
  }}

  /* Paragraph Text */
  p.section-p {{
    text-align: justify;
    margin-bottom: 8px;
    font-size: 10.5pt;
  }}

  .source-text {{
    font-size: 10.5pt;
    margin-bottom: 10px;
  }}

  /* Bullet List */
  ul.bullet-list {{
    margin-left: 20px;
    margin-bottom: 12px;
  }}

  ul.bullet-list li {{
    margin-bottom: 4px;
    font-size: 10.5pt;
    text-align: justify;
  }}

  /* Design Table */
  table.design-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
    margin-bottom: 12px;
    font-size: 9.5pt;
  }}

  table.design-table th, table.design-table td {{
    border: 1px solid #000000;
    padding: 6px 8px;
    vertical-align: top;
    text-align: left;
  }}

  table.design-table th {{
    font-weight: bold;
    background-color: #ffffff;
  }}

  .obs-item {{
    margin-bottom: 7px;
    text-align: justify;
    font-size: 10.5pt;
  }}

  .obs-label {{
    font-weight: bold;
  }}

  /* Dashboard Image Container on Page 3 */
  .dashboard-container {{
    text-align: center;
    margin-top: 10px;
  }}

  .dashboard-img {{
    width: 100%;
    max-height: 240mm;
    object-fit: contain;
    border: 1px solid #cccccc;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  }}

</style>
</head>
<body>

  <!-- PAGE 1 -->
  <div class="page">
    <h1 class="doc-title">STUDENT PERFORMANCE ANALYSIS</h1>
    <div class="doc-subtitle">Tableau Dashboard Summary</div>

    <table class="info-table">
      <tr>
        <td class="label-col">Student</td>
        <td class="val-col">Advita Bhonde</td>
      </tr>
      <tr>
        <td class="label-col">UID</td>
        <td class="val-col">23003045</td>
      </tr>
      <tr>
        <td class="label-col">Branch</td>
        <td class="val-col">ETC</td>
      </tr>
    </table>

    <h2 class="section-heading">1. Overview</h2>
    <p class="section-p">
      This assessment presents an interactive Tableau dashboard developed using the Student Performance dataset. 
      The dashboard converts academic observations from 600 engineering students across various departments into concise visual 
      summaries of overall grade distribution, cumulative GPA (CGPA), attendance patterns, study hours, semester progression trends, 
      and the relationship between class attendance and academic achievement.
    </p>

    <h2 class="section-heading">2. Dataset Description</h2>
    <p class="section-p">
      The Student Performance Dataset is a comprehensive academic repository containing 600 records across 6 engineering branches 
      (CSE, IT, ECE, ME, CE, EE) and 8 semesters. It encompasses 16 key demographic, behavioral, and academic performance attributes, 
      including CGPA, attendance percentage, weekly study hours, midterm, assignment, and final exam scores, extracurricular participation, 
      internet access, and passing status classifications. It is ideal for exploratory data analysis and interactive visual reporting.
    </p>
    <p class="source-text"><strong>Dataset Source:</strong> <em>Academic Student Performance Repository – Tableau Project</em></p>

    <h2 class="section-heading">3. Objective</h2>
    <ul class="bullet-list">
      <li>Explore the distribution of student performance categories and passing statuses across the cohort.</li>
      <li>Compare average CGPA, attendance percentage, and weekly study hours across engineering branches.</li>
      <li>Identify broad semester-wise academic progression and grade stabilization patterns.</li>
      <li>Examine the relationship between attendance percentage, study hours, and final CGPA.</li>
      <li>Present multiple academic metrics in a single, interactive, easy-to-understand Tableau dashboard.</li>
    </ul>

    <h2 class="section-heading">4. Dashboard Design</h2>
    <p class="section-p">
      The dashboard uses a combination of categorical, comparison, trend, distribution, and relationship visualizations. This 
      allows both high-level executive understanding and detailed branch-level comparison within one unified Tableau view.
    </p>

    <table class="design-table">
      <thead>
        <tr>
          <th style="width: 26%;">Visualization</th>
          <th style="width: 36%;">Purpose</th>
          <th style="width: 38%;">Main Insight Supported</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>KPI Highlights Cards</td>
          <td>Displays key cohort summary metrics (Total Students, Avg CGPA, Avg Attendance, Pass Rate).</td>
          <td>Cohort shows strong overall results with 600 students, 7.41 average CGPA, and 81.8% average attendance.</td>
        </tr>
        <tr>
          <td>Average CGPA by Branch</td>
          <td>Ranks branches by cumulative academic performance.</td>
          <td>Electrical, Mechanical, and Computer Science branches lead with ~7.47 average CGPA.</td>
        </tr>
        <tr>
          <td>Academic Progress Trend</td>
          <td>Shows semester average CGPA progression from Semester 1 to 8.</td>
          <td>Performance peaks early in Semester 2 (7.54) and stabilizes around 7.40 in upper semesters.</td>
        </tr>
        <tr>
          <td>Attendance vs CGPA</td>
          <td>Scatter plot examining the correlation between two key variables.</td>
          <td>Higher attendance is strongly associated with higher CGPA; &gt;85% attendance yields an avg 8.12 CGPA.</td>
        </tr>
        <tr>
          <td>Passing Status Distribution</td>
          <td>Donut chart illustrating overall ratio of academic statuses.</td>
          <td>12.0% of students achieve Academic Distinction, 83.7% Pass, and 4.3% are At-Risk.</td>
        </tr>
        <tr>
          <td>Study Hours by Risk Tier</td>
          <td>Compares weekly study hours against risk classifications.</td>
          <td>Distinction performers average 22+ hours/week, whereas at-risk students study &lt;10 hours/week.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PAGE 2 -->
  <div class="page page-break">
    <h2 class="section-heading">5. Key Observations</h2>
    
    <p class="obs-item">
      <span class="obs-label">Performance categories:</span> The status distribution shows Pass as the largest category in the displayed dashboard (83.7%), followed by Academic Distinction (12.0%). At-Risk students represent a small portion (4.3%) requiring academic monitoring.
    </p>
    
    <p class="obs-item">
      <span class="obs-label">Attendance impact:</span> Class attendance shows average values concentrated around 81.8%, with top performers maintaining over 85% attendance and securing an average CGPA of 8.12. Attendance below 65% resulted in a 78% risk category conversion rate.
    </p>

    <p class="obs-item">
      <span class="obs-label">Branch comparison:</span> The branch comparison highlights consistent performance across engineering streams. Computer Science and Information Technology lead distinction rates at 14.2% and 13.8% respectively, supported by high assignment submission scores.
    </p>

    <p class="obs-item">
      <span class="obs-label">Study hours & activity balance:</span> Weekly study hours range from 5 to 30 hours. Students dedicating 18–25 study hours per week combined with active extracurricular participation achieved higher exam scores (avg 78.4) than isolated study routines.
    </p>

    <p class="obs-item">
      <span class="obs-label">Academic progress trend:</span> The semester trend rises from Semester 1 to peak in Semester 2 (avg 7.54 CGPA) before stabilizing steadily around the 7.40 range from Semester 4 through Semester 8.
    </p>

    <p class="obs-item">
      <span class="obs-label">Attendance–CGPA relationship:</span> The scatter plot indicates a strong positive relationship: students with higher attendance percentages consistently achieve upper-tier CGPAs (8.0–10.0), while lower attendance correlates directly with reduced grade point averages.
    </p>

    <h2 class="section-heading">6. Data Science / Tableau Techniques Demonstrated</h2>
    <ul class="bullet-list">
      <li>Data aggregation using custom calculated measures such as average CGPA, weighted attendance rate, and pass percentage.</li>
      <li>Categorical analysis and segmentation using calculated fields for risk levels and distinction tiers.</li>
      <li>Ranking and Top-N branch comparison using dynamic bar charts and treemaps.</li>
      <li>Longitudinal time-based analysis across 8 academic semesters using line trend visualizations.</li>
      <li>Bivariate exploratory analysis using an attendance-vs-CGPA scatter plot.</li>
      <li>Dashboard composition: multiple coordinated worksheets arranged into a single unified analytical view.</li>
      <li>Use of appropriate visual encoding (color gradients, KPI cards, and box plots) to communicate distributions, comparisons, and correlations effectively.</li>
    </ul>

    <h2 class="section-heading">7. Conclusion</h2>
    <p class="section-p">
      The Tableau dashboard provides a compact visual summary of student performance observations and demonstrates how data visualization can transform a large, multi-variable dataset into actionable insights. The dashboard makes it easier to compare engineering branches, identify seasonal/semester grade progression, understand performance distributions, and explore relationships between behavioral and academic variables. Overall, the work demonstrates the use of Tableau as a practical tool for institutional analytics, exploratory data analysis, and data-driven storytelling.
    </p>
  </div>

  <!-- PAGE 3 -->
  <div class="page page-break">
    <h2 class="section-heading" style="text-align: center; font-size: 14pt; margin-top: 0; margin-bottom: 12px; color: #1F4E79;">
      Tableau Interactive Dashboard Visual
    </h2>
    <div class="dashboard-container">
      <img src="{db_b64}" class="dashboard-img" alt="Tableau Dashboard Screenshot" />
    </div>
  </div>

</body>
</html>
"""

    html_file = os.path.join(workspace_dir, "Student_Performance_Dashboard_Summary.html")
    pdf_file = os.path.join(workspace_dir, "Student_Performance_Dashboard_Summary.pdf")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Saved HTML to {html_file}")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file:///{html_file.replace('\\', '/')}")
        page.pdf(
            path=pdf_file,
            format="A4",
            print_background=True,
            margin={
                "top": "15mm",
                "bottom": "15mm",
                "left": "15mm",
                "right": "15mm"
            }
        )
        browser.close()
    print(f"Successfully generated PDF: {pdf_file}")

if __name__ == "__main__":
    main()
