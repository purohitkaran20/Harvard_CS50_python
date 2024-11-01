"""
In this code all you have to do is to take input name from the user and generate a
pdf which have a tshirt (as given in the image in below folder) and the name of the user should
be printed, on tshirt, as "NAME tool CS50" and on the top of the pdf in the b lank space should
say, "CS50 Shirtificate"
So how will you do it.
1. write a code to get name from user, and store it in a variable.
2. Using the fpdf library, create a pdf, in which the size of page is A4,
    inser the tshit in that, page, and write the above test.
3. Figure out how to do the above steps.
"""

from fpdf import FPDF

def main():
    name = input("INPUT: ")
    generate_pdf(name)

def generate_pdf(name):
    pdf = FPDF()
    pdf.add_page()
    # pdf.set_title("20000 Leagues Under the Seas")
    pdf.set_font("helvetica", "B", 40)
    pdf.cell(0, 50, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.image("shirtificate.png", x=0, y=90)
    pdf.cell(0, 200, f"{name} took CS50", align='C')

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
