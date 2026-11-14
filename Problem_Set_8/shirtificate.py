from fpdf import FPDF

class PDF:

    def __init__(self, name):
        if name == "":
            name = "John Harvard"
        self._name = name

    def shirtificate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font("helvetica", style="B", size=64)
        pdf.cell(None, 8, "CS50 Shirtificate", center=True)

        pdf.image("shirtificate.png", x=1, y=60)

        pdf.set_text_color(255,255,255)
        pdf.set_font(size=32)
        pdf.cell(None, 200, f"{self._name} took CS50", center=True)

        pdf.output("shirtificate.pdf")

def main():
    user_name = input("Name on the shirt: ").title()

    x = PDF(user_name)
    x.shirtificate()


if __name__ == "__main__":
    main()
    #pdf.add_page()
    #pdf.set_font("Times", size=12)
    #pdf.output("new-tuto2.pdf")
