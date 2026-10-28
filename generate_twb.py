import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

twb_content = """<?xml version='1.0' encoding='utf-8' ?>

<!-- Tableau Workbook - Student Performance Dashboard -->
<workbook originalversion='18.1' source-build='2024.1.0' version='2024.1' xmlns:user='http://www.tableausoftware.com/xml/user'>
  <document-format-change-manifest>
    <AutoCreateAndUpdateDPIAwareness />
    <SheetIdentifierTracking />
    <WindowsPersistSimpleIdentifiers />
  </document-format-change-manifest>

  <preferences>
    <preference name='ui.encoding.shelf.height' value='24' />
    <preference name='ui.shelf.height' value='26' />
  </preferences>

  <datasources>
    <datasource inline='true' name='federated.student_performance' version='18.1'>
      <connection class='federated'>
        <named-connections>
          <named-connection caption='student_performance_dataset' name='textscan.student_performance'>
            <connection class='textscan' directory='.' filename='student_performance_dataset.csv' password='' server='' />
          </named-connection>
        </named-connections>
        <relation connection='textscan.student_performance' name='student_performance_dataset.csv' table='[student_performance_dataset#csv]' type='table'>
          <columns character-set='UTF-8' header='yes' locale='en_US' separator=','>
            <column datatype='string' name='Student_ID' ordinal='0' />
            <column datatype='string' name='Student_Name' ordinal='1' />
            <column datatype='string' name='Gender' ordinal='2' />
            <column datatype='string' name='Branch' ordinal='3' />
            <column datatype='string' name='Semester' ordinal='4' />
            <column datatype='real' name='Attendance_Percentage' ordinal='5' />
            <column datatype='integer' name='Study_Hours_Per_Week' ordinal='6' />
            <column datatype='real' name='Midterm_Score' ordinal='7' />
            <column datatype='real' name='Assignment_Score' ordinal='8' />
            <column datatype='real' name='Final_Exam_Score' ordinal='9' />
            <column datatype='real' name='CGPA' ordinal='10' />
            <column datatype='string' name='Extracurricular_Activities' ordinal='11' />
            <column datatype='string' name='Parent_Education_Level' ordinal='12' />
            <column datatype='string' name='Internet_Access' ordinal='13' />
            <column datatype='string' name='Passing_Status' ordinal='14' />
            <column datatype='string' name='Performance_Category' ordinal='15' />
          </columns>
        </relation>
        <metadata-records>
          <metadata-record class='column'>
            <remote-name>Student_ID</remote-name>
            <remote-type>129</remote-type>
            <local-name>[Student_ID]</local-name>
            <parent-name>[student_performance_dataset.csv]</parent-name>
            <type-name>string</type-name>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Student_Name</remote-name>
            <remote-type>129</remote-type>
            <local-name>[Student_Name]</local-name>
            <parent-name>[student_performance_dataset.csv]</parent-name>
            <type-name>string</type-name>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Gender</remote-name>
            <remote-type>129</remote-type>
            <local-name>[Gender]</local-name>
            <parent-name>[student_performance_dataset.csv]</parent-name>
            <type-name>string</type-name>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Branch</remote-name>
            <remote-type>129</remote-type>
            <local-name>[Branch]</local-name>
            <parent-name>[student_performance_dataset.csv]</parent-name>
            <type-name>string</type-name>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Semester</remote-name>
            <remote-type>129</remote-type>
            <local-name>[Semester]</local-name>
            <parent-name>[student_performance_dataset.csv]</parent-name>
            <type-name>string</type-name>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Attendance_Percentage</remote-name>
            <remote-type>5</remote-type>
            <local-name>[Attendance_Percentage]</local-name>
            <parent-name>[student_performance_dataset.csv]</parent-name>
            <type-name>real</type-name>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Study_Hours_Per_Week</remote-name>
            <remote-type>20</remote-type>
            <local-name>[Study_Hours_Per_Week]</local-name>
            <parent-name>[student_performance_dataset.csv]</parent-name>
            <type-name>integer</type-name>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>CGPA</remote-name>
            <remote-type>5</remote-type>
            <local-name>[CGPA]</local-name>
            <parent-name>[student_performance_dataset.csv]</parent-name>
            <type-name>real</type-name>
          </metadata-record>
          <metadata-record class='column'>
            <remote-name>Passing_Status</remote-name>
            <remote-type>129</remote-type>
            <local-name>[Passing_Status]</local-name>
            <parent-name>[student_performance_dataset.csv]</parent-name>
            <type-name>string</type-name>
          </metadata-record>
        </metadata-records>
      </connection>
      <aliases enabled='yes' />
      <column caption='Student ID' datatype='string' name='[Student_ID]' role='dimension' type='nominal' />
      <column caption='Student Name' datatype='string' name='[Student_Name]' role='dimension' type='nominal' />
      <column caption='Gender' datatype='string' name='[Gender]' role='dimension' type='nominal' />
      <column caption='Branch' datatype='string' name='[Branch]' role='dimension' type='nominal' />
      <column caption='Semester' datatype='string' name='[Semester]' role='dimension' type='nominal' />
      <column caption='Attendance Percentage' datatype='real' name='[Attendance_Percentage]' role='measure' type='quantitative' default-format='n#,##0.0"%"' />
      <column caption='Study Hours Per Week' datatype='integer' name='[Study_Hours_Per_Week]' role='measure' type='quantitative' default-format='n#,##0' />
      <column caption='Midterm Score' datatype='real' name='[Midterm_Score]' role='measure' type='quantitative' default-format='n#,##0.0' />
      <column caption='Assignment Score' datatype='real' name='[Assignment_Score]' role='measure' type='quantitative' default-format='n#,##0.0' />
      <column caption='Final Exam Score' datatype='real' name='[Final_Exam_Score]' role='measure' type='quantitative' default-format='n#,##0.0' />
      <column caption='CGPA' datatype='real' name='[CGPA]' role='measure' type='quantitative' default-format='n#,##0.00' />
      <column caption='Extracurricular Activities' datatype='string' name='[Extracurricular_Activities]' role='dimension' type='nominal' />
      <column caption='Parent Education Level' datatype='string' name='[Parent_Education_Level]' role='dimension' type='nominal' />
      <column caption='Internet Access' datatype='string' name='[Internet_Access]' role='dimension' type='nominal' />
      <column caption='Passing Status' datatype='string' name='[Passing_Status]' role='dimension' type='nominal' />
      <column caption='Performance Category' datatype='string' name='[Performance_Category]' role='dimension' type='nominal' />

      <!-- Calculated Fields -->
      <column caption='Total Students Enrolled' datatype='integer' name='[Calculated_Total_Students]' role='measure' type='quantitative' default-format='n#,##0'>
        <calculation class='tableau' formula='COUNT([Student_ID])' />
      </column>
      <column caption='Average CGPA' datatype='real' name='[Calculated_Avg_CGPA]' role='measure' type='quantitative' default-format='n#,##0.00'>
        <calculation class='tableau' formula='AVG([CGPA])' />
      </column>
      <column caption='Average Attendance Rate' datatype='real' name='[Calculated_Avg_Attendance]' role='measure' type='quantitative' default-format='p0.0%'>
        <calculation class='tableau' formula='AVG([Attendance_Percentage]) / 100.0' />
      </column>
      <column caption='Academic Pass Rate %' datatype='real' name='[Calculated_Pass_Rate]' role='measure' type='quantitative' default-format='p0.0%'>
        <calculation class='tableau' formula='SUM(IF [Passing_Status] &lt;&gt; &apos;At-Risk&apos; THEN 1 ELSE 0 END) / COUNT([Student_ID])' />
      </column>
      <column caption='Distinction Rate %' datatype='real' name='[Calculated_Distinction_Rate]' role='measure' type='quantitative' default-format='p0.0%'>
        <calculation class='tableau' formula='SUM(IF [Passing_Status] = &apos;Academic Distinction&apos; THEN 1 ELSE 0 END) / COUNT([Student_ID])' />
      </column>

      <layout dim-ordering='alphabetic' dim-percentage='0.5' measure-ordering='alphabetic' measure-percentage='0.5' show-structure='true' />
    </datasource>
  </datasources>

  <worksheets>
    <!-- KPI 1: Total Students Enrolled -->
    <worksheet name='KPI_Total_Students'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='12' fontcolor='#1E293B'>TOTAL STUDENTS ENROLLED</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>

    <!-- KPI 2: Average CGPA -->
    <worksheet name='KPI_Avg_CGPA'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='12' fontcolor='#1E293B'>AVERAGE CGPA (10.0 SCALE)</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>

    <!-- KPI 3: Average Attendance Rate -->
    <worksheet name='KPI_Avg_Attendance'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='12' fontcolor='#1E293B'>AVERAGE ATTENDANCE RATE</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>

    <!-- KPI 4: Academic Pass Rate -->
    <worksheet name='KPI_Pass_Rate'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='12' fontcolor='#1E293B'>ACADEMIC PASS RATE (%)</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>

    <!-- Chart 1: Average CGPA & Scores by Branch -->
    <worksheet name='Bar_Branch_CGPA'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='14' fontcolor='#0F172A'>Average CGPA &amp; Final Score Comparison across Branches</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>

    <!-- Chart 2: Academic Progress Trend across Semesters -->
    <worksheet name='Line_Semester_Trend'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='14' fontcolor='#0F172A'>Academic Performance Progression (Semester 1 to 8)</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>

    <!-- Chart 3: Attendance vs CGPA Correlation -->
    <worksheet name='Scatter_Attendance_vs_CGPA'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='14' fontcolor='#0F172A'>Attendance Percentage vs CGPA Correlation Matrix</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>

    <!-- Chart 4: Grade & Performance Distribution -->
    <worksheet name='Donut_Grade_Distribution'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='14' fontcolor='#0F172A'>Student Academic Status &amp; Performance Breakdown</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>

    <!-- Chart 5: Study Hours & Extracurricular Impact -->
    <worksheet name='Stacked_StudyHours_Performance'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='14' fontcolor='#0F172A'>Impact of Weekly Study Hours &amp; Extracurriculars on Scores</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>

    <!-- Chart 6: Score Distribution across Gender & Parent Education -->
    <worksheet name='Box_Gender_Score_Distribution'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='14' fontcolor='#0F172A'>Score Distribution by Gender &amp; Parent Education Level</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>

    <!-- Chart 7: Department Enrollment & Distinction Treemap -->
    <worksheet name='Treemap_Department_Enrollment'>
      <layout-options>
        <title>
          <formatted-text>
            <run fontname='Tableau Bold' fontsize='14' fontcolor='#0F172A'>Department Enrollment Volume &amp; Academic Distinction Counts</run>
          </formatted-text>
        </title>
      </layout-options>
      <table />
    </worksheet>
  </worksheets>

  <dashboards>
    <dashboard name='Student Performance Dashboard'>
      <style />
      <size maxheight='1080' maxwidth='1920' minheight='800' minwidth='1200' preset-index='0' type='preset' />
      <zones>
        <zone h='100000' id='1' type-name='layout-basic' w='100000' x='0' y='0'>
          <!-- Header Zone -->
          <zone h='9000' id='2' name='Title' type-name='title' w='100000' x='0' y='0'>
            <formatted-text>
              <run fontname='Tableau Bold' fontsize='22' fontcolor='#0F172A'>Student Performance Analytics Dashboard</run>
              <run fontname='Tableau' fontsize='12' fontcolor='#475569'> | Comprehensive Academic Intelligence &amp; Student Retention Monitoring</run>
            </formatted-text>
          </zone>
          
          <!-- KPI Zone -->
          <zone h='16000' id='3' type-name='layout-flow' w='100000' x='0' y='9000'>
            <zone h='16000' id='4' name='KPI_Total_Students' w='25000' x='0' y='9000' />
            <zone h='16000' id='5' name='KPI_Avg_CGPA' w='25000' x='25000' y='9000' />
            <zone h='16000' id='6' name='KPI_Avg_Attendance' w='25000' x='50000' y='9000' />
            <zone h='16000' id='7' name='KPI_Pass_Rate' w='25000' x='75000' y='9000' />
          </zone>

          <!-- Row 1 Charts -->
          <zone h='37000' id='8' type-name='layout-flow' w='100000' x='0' y='25000'>
            <zone h='37000' id='9' name='Bar_Branch_CGPA' w='50000' x='0' y='25000' />
            <zone h='37000' id='10' name='Line_Semester_Trend' w='50000' x='50000' y='25000' />
          </zone>

          <!-- Row 2 Charts -->
          <zone h='38000' id='11' type-name='layout-flow' w='100000' x='0' y='62000'>
            <zone h='38000' id='12' name='Scatter_Attendance_vs_CGPA' w='33333' x='0' y='62000' />
            <zone h='38000' id='13' name='Donut_Grade_Distribution' w='33333' x='33333' y='62000' />
            <zone h='38000' id='14' name='Stacked_StudyHours_Performance' w='33334' x='66666' y='62000' />
          </zone>
        </zone>
      </zones>
    </dashboard>
  </dashboards>
</workbook>
"""

twb_path = "C:/Users/ommis/.gemini/antigravity-ide/scratch/student-performance-dashboard/Student_Performance_Dashboard.twb"
with open(twb_path, "w", encoding="utf-8") as f:
    f.write(twb_content)

print(f"Tableau workbook created successfully at {twb_path}")
