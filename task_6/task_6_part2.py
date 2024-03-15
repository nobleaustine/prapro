# Part 2:
# Pick an open-source software on GitHub
# Write a script that showcases the basic usage of the software


import csv
from fpdf import FPDF
from fpdf.fonts import FontFace


# defining header and footer
class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 15)
        width = self.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


# opening txt file to create csv
with open("time_table.txt", encoding="utf8") as csv_file:
    data = list(csv.reader(csv_file, delimiter=","))

# creating object and setting up heading
pdf = FPDF(orientation="L", unit="mm", format="A4")
pdf.add_page()

pdf.set_xy(0, 0)
pdf.set_font("helvetica", size=20, style="B")
pdf.cell(60, 10, "    ", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.multi_cell(
    270, 10, "IMSC CS VI SEMESTER TIME TABLE", align="C", new_x="LMARGIN", new_y="NEXT"
)
pdf.cell(60, 10, "    ", new_x="LMARGIN", new_y="NEXT", align="C")

# updating to a table
with pdf.table() as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

# printing the output
pdf.output("time_table.pdf")
