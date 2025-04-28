import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Step 1: Read the data
file_path = 'sample_data.csv'  
df = pd.read_csv(r"C:\Users\hp\Downloads\sample_data.csv")

# Step 2: Analyze the data
summary = {
    'Total Employees': len(df),
    'Average Age': df['Age'].mean(),
    'Average Salary': df['Salary'].mean(),
    'Departments': ', '.join(df['Department'].unique())
}

# Step 3: Create a PDF Report
pdf_file = 'sample_report.pdf'
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

# Title
c.setFont('Helvetica-Bold', 20)
c.drawString(200, height - 50, "Employee Data Report")

# Summary
c.setFont('Helvetica', 12)
y = height - 100
for key, value in summary.items():
    c.drawString(50, y, f"{key}: {value}")
    y -= 20

# Table Header
y -= 30
c.setFont('Helvetica-Bold', 14)
c.drawString(50, y, "Name")
c.drawString(150, y, "Age")
c.drawString(250, y, "Salary")
c.drawString(350, y, "Department")
y -= 20

# Table Content
c.setFont('Helvetica', 12)
for index, row in df.iterrows():
    c.drawString(50, y, str(row['Name']))
    c.drawString(150, y, str(row['Age']))
    c.drawString(250, y, str(row['Salary']))
    c.drawString(350, y, str(row['Department']))
    y -= 20
    if y < 50:
        c.showPage()
        y = height - 50

c.save()

print(f"Report generated: {pdf_file}")
