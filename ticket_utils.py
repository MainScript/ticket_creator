from barcode import Code39
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont


def create_ticket(number: str, name: str):
    """
    Creates a ticket with the given number and name.
    """
    filename = "output/" + number + ".png"
    with open(filename, "wb") as f:
        barcode = Code39(number, writer=ImageWriter(),
                         add_checksum=False).write(f)
        template = Image.open("template.png")
        barcode = Image.open(filename)
        template.paste(barcode, (1500, 250))
        draw = ImageDraw.Draw(template).text(
            (1500, 50), name, (255, 255, 255), font=ImageFont.truetype("Roboto-Regular.ttf", 50))
        template.save(filename)
    f.close()
