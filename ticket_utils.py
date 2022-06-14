from barcode import Code39
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
from db_utils import *


def create_ticket(number: str, name: str, helper: bool = False):
    """
    Creates a ticket with the given number and name.
    """
    if helper:
        if number == "0":
            number = name.lower()
            number_arr = number.split(" ")
            number = number_arr[-1] + " " + number_arr[0]
            number = number.replace(" ", "")
            number = number[:8]

    if not add_to_db(name, number, helper):
        return False
    filename = "output/" + number + ".png"
    with open(filename, "wb") as f:
        if helper:
            barcode = Code39(number + "helf", writer=ImageWriter(),
                             add_checksum=False).write(f, text="")
        else:
            barcode = Code39(number, writer=ImageWriter(),
                             add_checksum=False).write(f, text="")
        template = Image.open("template.png")
        barcode = Image.open(filename)
        template.paste(barcode, (1400, 250))
        ImageDraw.Draw(template).text(
            (1500, 50), name, (255, 255, 255), font=ImageFont.truetype("Roboto-Regular.ttf", 45))
        if helper:
            ImageDraw.Draw(template).text(
                (1500, 100), "Helfer:in", (255, 255, 255), font=ImageFont.truetype("Roboto-Regular.ttf", 45))
        template.save(filename)
    f.close()

    return True


def check_db(number: str):
    """
    Checks if a ticket with the given number and name exists.
    """
    return does_exist(number)
