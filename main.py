from ticket_utils import *
import PySimpleGUI as psg

if __name__ == "__main__":
    # create GUI
    layout_create = [
        [psg.Text("Name:")],
        [psg.InputText()],
        [psg.Text("Number:")],
        [psg.InputText()],
        [psg.Checkbox("Helper?", default=False)],
        [psg.Button("Create Ticket")]
    ]

    # create a layout to check the database for existing entries using number or name
    layout_check = [
        [psg.Text("Number:")],
        [psg.InputText()],
        [psg.Button("Check")]
    ]

    layout = [
        [psg.Frame("Create Ticket", layout_create)],
        [psg.Frame("Check Database", layout_check)]
    ]
    window = psg.Window("Ticket Generator", layout)
    # event loop
    while True:
        event, values = window.read()
        if event == "Create Ticket":
            if create_ticket(values[1], values[0], values[2]):
                psg.popup("Ticket created!")
            else:
                psg.popup("Ticket already exists!")
        elif event == psg.WIN_CLOSED:
            break
        elif event == "Check":
            if check_db(values[3]):
                psg.popup("Ticket exists!")
            else:
                psg.popup("Ticket does not exist!")
    window.close()
